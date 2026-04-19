from __future__ import annotations

from pathlib import Path
import importlib.util
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENERATED_PATH = PROJECT_ROOT / "generated" / "fcc" / "grammar"


def load_generated_module(module_name: str):
    module_path = GENERATED_PATH / f"{module_name}.py"

    if not module_path.exists():
        sys.exit(f"No se encontro {module_name}.py en {GENERATED_PATH}")

    spec = importlib.util.spec_from_file_location(module_name, module_path)

    if spec is None or spec.loader is None:
        sys.exit(f"No se pudo cargar {module_name}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


parser_module = load_generated_module("FCCParser")
visitor_module = load_generated_module("FCCParserVisitor")

FCCParser = parser_module.FCCParser
FCCParserVisitor = visitor_module.FCCParserVisitor

from ast_nodes import (
    ProgramNode,
    ImportNode,
    SecureAnnotationNode,
    ParameterNode,
    FunctionDeclNode,
    BlockNode,
    VarDeclNode,
    VarDeclaratorNode,
    AssignmentNode,
    IfNode,
    ElifNode,
    WhileNode,
    ForNode,
    ReturnNode,
    ContinueNode,
    BreakNode,
    ExpressionStmtNode,
    IdentifierNode,
    LiteralNode,
    UnaryOpNode,
    BinaryOpNode,
    CallNode,
    IndexAccessNode,
    MemberAccessNode,
)


class ASTBuilder(FCCParserVisitor):

    # UTILIDADES

    @staticmethod
    def make_location(ctx):
        return ctx.start.line, ctx.start.column

    # PROGRAMA

    def visitProgram(self, ctx):
        line, column = self.make_location(ctx)
        declarations = [self.visit(child) for child in ctx.topLevelDecl()]
        return ProgramNode(declarations=declarations, line=line, column=column)

    def visitTopLevelDecl(self, ctx):
        return self.visitChildren(ctx)

    def visitImportStmt(self, ctx):
        line, column = self.make_location(ctx)
        raw_path = ctx.STRING_LITERAL().getText()
        path = raw_path[1:-1]
        return ImportNode(path=path, line=line, column=column)

    def visitSecureAnnotation(self, ctx):
        line, column = self.make_location(ctx)
        return SecureAnnotationNode(
            value=ctx.HEX_LITERAL().getText(),
            line=line,
            column=column
        )

    def visitSecureFunctionDecl(self, ctx):
        secure_node = self.visit(ctx.secureAnnotation())
        function_node = self.visit(ctx.functionDecl())
        function_node.secure = secure_node
        return function_node

    def visitFunctionDecl(self, ctx):
        line, column = self.make_location(ctx)

        return_type = ctx.typeRule().getText()
        name = ctx.functionName().getText()
        params = []

        if ctx.parameterList():
            params = self.visit(ctx.parameterList())

        body = self.visit(ctx.block())

        return FunctionDeclNode(
            return_type=return_type,
            name=name,
            params=params,
            body=body,
            line=line,
            column=column
        )

    def visitParameterList(self, ctx):
        return [self.visit(param) for param in ctx.parameter()]

    def visitParameter(self, ctx):
        line, column = self.make_location(ctx)
        return ParameterNode(
            param_type=ctx.typeRule().getText(),
            name=ctx.IDENTIFIER().getText(),
            line=line,
            column=column
        )

    # BLOQUES Y SENTENCIAS

    def visitBlock(self, ctx):
        line, column = self.make_location(ctx)
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return BlockNode(statements=statements, line=line, column=column)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitVarDecl(self, ctx):
        line, column = self.make_location(ctx)
        return VarDeclNode(
            var_type=ctx.typeRule().getText(),
            declarators=self.visit(ctx.variableDeclaratorList()),
            line=line,
            column=column
        )

    def visitVarDeclNoSemi(self, ctx):
        line, column = self.make_location(ctx)
        return VarDeclNode(
            var_type=ctx.typeRule().getText(),
            declarators=self.visit(ctx.variableDeclaratorList()),
            line=line,
            column=column
        )

    def visitVariableDeclaratorList(self, ctx):
        return [self.visit(decl) for decl in ctx.variableDeclarator()]

    def visitVariableDeclarator(self, ctx):
        line, column = self.make_location(ctx)

        dimensions = []
        for suffix in ctx.arraySuffix():
            if suffix.expression():
                dimensions.append(self.visit(suffix.expression()))
            else:
                dimensions.append(None)

        initializer = None
        if ctx.initializer():
            initializer = self.visit(ctx.initializer())

        return VarDeclaratorNode(
            name=ctx.IDENTIFIER().getText(),
            dimensions=dimensions,
            initializer=initializer,
            line=line,
            column=column
        )

    def visitInitializer(self, ctx):
        return self.visit(ctx.expression())

    def visitAssignmentStmt(self, ctx):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx):
        line, column = self.make_location(ctx)
        return AssignmentNode(
            target=self.visit(ctx.assignable()),
            operator=ctx.assignmentOperator().getText(),
            value=self.visit(ctx.expression()),
            line=line,
            column=column
        )

    def visitReturnStmt(self, ctx):
        line, column = self.make_location(ctx)
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ReturnNode(value=value, line=line, column=column)

    def visitContinueStmt(self, ctx):
        line, column = self.make_location(ctx)
        return ContinueNode(line=line, column=column)

    def visitBreakStmt(self, ctx):
        line, column = self.make_location(ctx)
        return BreakNode(line=line, column=column)

    def visitExprStmt(self, ctx):
        line, column = self.make_location(ctx)
        return ExpressionStmtNode(
            expression=self.visit(ctx.expression()),
            line=line,
            column=column
        )

    # CONTROL DE FLUJO

    def visitIfStmt(self, ctx):
        line, column = self.make_location(ctx)

        condition = self.visit(ctx.expression())

        # el bloque principal del if
        then_block = self.visit(ctx.block())

        # ramas elif
        elif_branches = [self.visit(branch) for branch in ctx.elifBranch()]

        # rama else
        else_block = None
        if ctx.elseBranch():
            else_block = self.visit(ctx.elseBranch())

        return IfNode(
            condition=condition,
            then_block=then_block,
            elif_branches=elif_branches,
            else_block=else_block,
            line=line,
            column=column
        )

    def visitElifBranch(self, ctx):
        line, column = self.make_location(ctx)
        return ElifNode(
            condition=self.visit(ctx.expression()),
            block=self.visit(ctx.block()),
            line=line,
            column=column
        )

    def visitElseBranch(self, ctx):
        return self.visit(ctx.block())

    def visitWhileStmt(self, ctx):
        line, column = self.make_location(ctx)
        return WhileNode(
            condition=self.visit(ctx.expression()),
            body=self.visit(ctx.block()),
            line=line,
            column=column
        )

    def visitForStmt(self, ctx):
        line, column = self.make_location(ctx)

        initializer = self.visit(ctx.forInitializer()) if ctx.forInitializer() else None
        increment = self.visit(ctx.forIncrement()) if ctx.forIncrement() else None
        condition = self.visit(ctx.forCondition()) if ctx.forCondition() else None
        body = self.visit(ctx.block())

        return ForNode(
            initializer=initializer,
            increment=increment,
            condition=condition,
            body=body,
            line=line,
            column=column
        )

    def visitForInitializer(self, ctx):
        return self.visitChildren(ctx)

    def visitForIncrement(self, ctx):
        return self.visitChildren(ctx)

    def visitForCondition(self, ctx):
        return self.visitChildren(ctx)

    # EXPRESIONES

    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    def _visit_left_associative_binary(self, ctx, next_rule_getter):
        nodes = [self.visit(child) for child in next_rule_getter(ctx)]
        if len(nodes) == 1:
            return nodes[0]

        current = nodes[0]
        operator_tokens = [child.getText() for child in ctx.children if child.getText() not in [n.getText() if hasattr(n, "getText") else "" for n in []]]

        op_index = 0
        for i in range(1, len(ctx.children), 2):
            op = ctx.children[i].getText()
            right = nodes[op_index + 1]
            current = BinaryOpNode(
                operator=op,
                left=current,
                right=right,
                line=ctx.start.line,
                column=ctx.start.column
            )
            op_index += 1

        return current

    def visitBitwiseOrExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.bitwiseXorExpression())

    def visitBitwiseXorExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.bitwiseAndExpression())

    def visitBitwiseAndExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.equalityExpression())

    def visitEqualityExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.relationalExpression())

    def visitRelationalExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.shiftExpression())

    def visitShiftExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.additiveExpression())

    def visitAdditiveExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.multiplicativeExpression())

    def visitMultiplicativeExpression(self, ctx):
        return self._build_binary_chain(ctx, ctx.unaryExpression())

    def _build_binary_chain(self, ctx, subexpressions):
        nodes = [self.visit(expr) for expr in subexpressions]
        if len(nodes) == 1:
            return nodes[0]

        current = nodes[0]
        operator_positions = range(1, len(ctx.children), 2)

        for index, child_pos in enumerate(operator_positions):
            operator = ctx.children[child_pos].getText()
            right = nodes[index + 1]
            current = BinaryOpNode(
                operator=operator,
                left=current,
                right=right,
                line=ctx.start.line,
                column=ctx.start.column
            )

        return current

    def visitUnaryExpression(self, ctx):
        line, column = self.make_location(ctx)

        if ctx.postfixExpression():
            return self.visit(ctx.postfixExpression())

        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.unaryExpression())

        return UnaryOpNode(
            operator=operator,
            operand=operand,
            line=line,
            column=column
        )

    def visitPostfixExpression(self, ctx):
        current = self.visit(ctx.primary())

        for suffix in ctx.postfixSuffix():
            if suffix.LPAREN():
                args = []
                if suffix.argumentList():
                    args = self.visit(suffix.argumentList())

                current = CallNode(
                    callee=current,
                    arguments=args,
                    line=suffix.start.line,
                    column=suffix.start.column
                )

            elif suffix.LBRACK():
                current = IndexAccessNode(
                    target=current,
                    index=self.visit(suffix.expression()),
                    line=suffix.start.line,
                    column=suffix.start.column
                )

            elif suffix.DOT():
                current = MemberAccessNode(
                    target=current,
                    member=suffix.IDENTIFIER().getText(),
                    line=suffix.start.line,
                    column=suffix.start.column
                )

        return current

    def visitArgumentList(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitPrimary(self, ctx):
        line, column = self.make_location(ctx)

        if ctx.IDENTIFIER():
            return IdentifierNode(
                name=ctx.IDENTIFIER().getText(),
                line=line,
                column=column
            )

        if ctx.literal():
            return self.visit(ctx.literal())

        return self.visit(ctx.expression())

    def visitLiteral(self, ctx):
        line, column = self.make_location(ctx)

        if ctx.INT_LITERAL():
            return LiteralNode(
                value=ctx.INT_LITERAL().getText(),
                literal_type="int",
                line=line,
                column=column
            )

        if ctx.HEX_LITERAL():
            return LiteralNode(
                value=ctx.HEX_LITERAL().getText(),
                literal_type="hex",
                line=line,
                column=column
            )

        if ctx.STRING_LITERAL():
            return LiteralNode(
                value=ctx.STRING_LITERAL().getText(),
                literal_type="string",
                line=line,
                column=column
            )

        if ctx.CHAR_LITERAL():
            return LiteralNode(
                value=ctx.CHAR_LITERAL().getText(),
                literal_type="char",
                line=line,
                column=column
            )

        if ctx.TRUE():
            return LiteralNode(
                value=True,
                literal_type="bool",
                line=line,
                column=column
            )

        return LiteralNode(
            value=False,
            literal_type="bool",
            line=line,
            column=column
        )