from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List, Any


# NODO BASE

@dataclass
class ASTNode:
    line: int = 0
    column: int = 0


# PROGRAMA Y ALTO NIVEL

@dataclass
class ProgramNode(ASTNode):
    declarations: List[ASTNode] = field(default_factory=list)


@dataclass
class ImportNode(ASTNode):
    path: str = ""


@dataclass
class SecureAnnotationNode(ASTNode):
    value: str = ""


@dataclass
class ParameterNode(ASTNode):
    param_type: str = ""
    name: str = ""


@dataclass
class FunctionDeclNode(ASTNode):
    return_type: str = ""
    name: str = ""
    params: List[ParameterNode] = field(default_factory=list)
    body: Optional["BlockNode"] = None
    secure: Optional[SecureAnnotationNode] = None


# BLOQUES Y SENTENCIAS

@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class VarDeclaratorNode(ASTNode):
    name: str = ""
    dimensions: List[Optional[ASTNode]] = field(default_factory=list)
    initializer: Optional[ASTNode] = None


@dataclass
class VarDeclNode(ASTNode):
    var_type: str = ""
    declarators: List[VarDeclaratorNode] = field(default_factory=list)


@dataclass
class AssignmentNode(ASTNode):
    target: Optional[ASTNode] = None
    operator: str = ""
    value: Optional[ASTNode] = None


@dataclass
class IfNode(ASTNode):
    condition: Optional[ASTNode] = None
    then_block: Optional[BlockNode] = None
    elif_branches: List["ElifNode"] = field(default_factory=list)
    else_block: Optional[BlockNode] = None


@dataclass
class ElifNode(ASTNode):
    condition: Optional[ASTNode] = None
    block: Optional[BlockNode] = None


@dataclass
class WhileNode(ASTNode):
    condition: Optional[ASTNode] = None
    body: Optional[BlockNode] = None


@dataclass
class ForNode(ASTNode):
    initializer: Optional[ASTNode] = None
    increment: Optional[ASTNode] = None
    condition: Optional[ASTNode] = None
    body: Optional[BlockNode] = None


@dataclass
class ReturnNode(ASTNode):
    value: Optional[ASTNode] = None


@dataclass
class ContinueNode(ASTNode):
    pass


@dataclass
class BreakNode(ASTNode):
    pass


@dataclass
class ExpressionStmtNode(ASTNode):
    expression: Optional[ASTNode] = None


# EXPRESIONES

@dataclass
class IdentifierNode(ASTNode):
    name: str = ""


@dataclass
class LiteralNode(ASTNode):
    value: Any = None
    literal_type: str = ""


@dataclass
class UnaryOpNode(ASTNode):
    operator: str = ""
    operand: Optional[ASTNode] = None


@dataclass
class BinaryOpNode(ASTNode):
    operator: str = ""
    left: Optional[ASTNode] = None
    right: Optional[ASTNode] = None


@dataclass
class CallNode(ASTNode):
    callee: Optional[ASTNode] = None
    arguments: List[ASTNode] = field(default_factory=list)


@dataclass
class IndexAccessNode(ASTNode):
    target: Optional[ASTNode] = None
    index: Optional[ASTNode] = None


@dataclass
class MemberAccessNode(ASTNode):
    target: Optional[ASTNode] = None
    member: str = ""