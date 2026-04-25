from __future__ import annotations

from contextlib import redirect_stdout, redirect_stderr
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from shutil import rmtree
from typing import Callable, Optional

from ast_nodes import (
    BinaryOpNode,
    CallNode,
    ExpressionStmtNode,
    ForNode,
    FunctionDeclNode,
    IdentifierNode,
    ImportNode,
    ProgramNode,
    VarDeclNode,
)
from parser_driver import parse_and_build_ast

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TMP_CASES_DIR = PROJECT_ROOT / "examples" / "_parser_smoke_tmp"


@dataclass
class ParserCase:
    name: str
    source: str
    should_pass: bool
    validator: Optional[Callable[[ProgramNode], None]] = None


def _assert(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def validate_import(ast: ProgramNode):
    _assert(len(ast.declarations) >= 2, "Se esperaban al menos dos declaraciones.")
    _assert(isinstance(ast.declarations[0], ImportNode), "El import debe quedar en el AST.")
    _assert(ast.declarations[0].path == "std/core", "La ruta del import no coincide.")


def validate_main_call(ast: ProgramNode):
    caller = next(
        decl for decl in ast.declarations
        if isinstance(decl, FunctionDeclNode) and decl.name == "caller"
    )
    _assert(len(caller.body.statements) == 1, "La funcion caller debe tener una sola sentencia.")

    stmt = caller.body.statements[0]
    _assert(isinstance(stmt, ExpressionStmtNode), "main(); debe ser una sentencia de expresion.")
    _assert(isinstance(stmt.expression, CallNode), "main(); debe construirse como CallNode.")
    _assert(isinstance(stmt.expression.callee, IdentifierNode), "El callee debe ser un identificador.")
    _assert(stmt.expression.callee.name == "main", "La llamada debe apuntar a main.")


def validate_for_shape(ast: ProgramNode):
    main_fn = next(
        decl for decl in ast.declarations
        if isinstance(decl, FunctionDeclNode) and decl.name == "main"
    )
    loop = next(stmt for stmt in main_fn.body.statements if isinstance(stmt, ForNode))

    _assert(isinstance(loop.initializer, VarDeclNode), "El for debe iniciar con una declaracion.")
    _assert(loop.increment.operator == "+=", "La segunda clausula del for debe ser la actualizacion.")
    _assert(isinstance(loop.condition, BinaryOpNode), "La tercera clausula del for debe ser la condicion.")
    _assert(loop.condition.operator == "<", "La condicion del for debe conservar el operador relacional.")


CASES = [
    ParserCase(
        name="valid_import_without_semicolon",
        source=(
            'traigase "std/core"\n'
            "func void main(){\n"
            "    ret;\n"
            "}\n"
        ),
        should_pass=True,
        validator=validate_import,
    ),
    ParserCase(
        name="valid_main_call",
        source=(
            "func void caller(){\n"
            "    main();\n"
            "}\n"
            "func void main(){\n"
            "    ret;\n"
            "}\n"
        ),
        should_pass=True,
        validator=validate_main_call,
    ),
    ParserCase(
        name="valid_for_language_shape",
        source=(
            "func void main(){\n"
            "    for (int i = 0; i += 1; i < 10) {\n"
            "        ret;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=True,
        validator=validate_for_shape,
    ),
    ParserCase(
        name="valid_float_and_if",
        source=(
            "func void main(){\n"
            "    float y = 10.5;\n"
            "    if (y > 1.0) {\n"
            "        y = 2.5;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=True,
    ),
    ParserCase(
        name="invalid_for_classic_order",
        source=(
            "func void main(){\n"
            "    for (int i = 0; i < 10; i += 1) {\n"
            "        ret;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=False,
    ),
    ParserCase(
        name="invalid_missing_semicolon",
        source=(
            "func void main(){\n"
            "    int x = 1\n"
            "    ret x;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    ParserCase(
        name="invalid_missing_block_brace",
        source=(
            "func void main(){\n"
            "    if (x < 5){\n"
            "        x = 1.5;\n"
            "    else {\n"
            "        x = 2;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=False,
    ),
    ParserCase(
        name="invalid_bad_real_literal",
        source=(
            "func void main(){\n"
            "    float y = 10.5.3;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    ParserCase(
        name="invalid_top_level_if",
        source=(
            "if (x < 5) {\n"
            "    x = 1;\n"
            "}\n"
        ),
        should_pass=False,
    ),
]


def run_case(case: ParserCase) -> bool:
    input_path = TMP_CASES_DIR / f"{case.name}.f"
    input_path.write_text(case.source, encoding="utf-8")

    captured = StringIO()

    try:
        with redirect_stdout(captured), redirect_stderr(captured):
            _, _, ast = parse_and_build_ast(input_path)
    except SystemExit:
        output = captured.getvalue().strip()

        if case.should_pass:
            print(f"[FAIL] {case.name}")
            if output:
                print(f"       {output.splitlines()[0]}")
            return False

        print(f"[OK]   {case.name}")
        if output:
            print(f"       {output.splitlines()[0]}")
        return True
    except Exception as exc:
        print(f"[FAIL] {case.name}")
        print(f"       Excepcion inesperada: {exc}")
        return False

    if not case.should_pass:
        print(f"[FAIL] {case.name}")
        print("       Se esperaba un error sintactico o lexico, pero el analisis fue exitoso.")
        return False

    try:
        if case.validator is not None:
            case.validator(ast)
    except AssertionError as exc:
        print(f"[FAIL] {case.name}")
        print(f"       {exc}")
        return False

    print(f"[OK]   {case.name}")
    return True


def main():
    print("Ejecutando pruebas de humo del parser...\n")
    if TMP_CASES_DIR.exists():
        rmtree(TMP_CASES_DIR)
    TMP_CASES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        results = [run_case(case) for case in CASES]
    finally:
        if TMP_CASES_DIR.exists():
            rmtree(TMP_CASES_DIR)

    if all(results):
        print("\nTodas las pruebas del parser pasaron.")
        return

    print("\nAl menos una prueba del parser fallo.")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
