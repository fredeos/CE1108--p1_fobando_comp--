from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from shutil import rmtree
from typing import Callable, Optional

from parser_driver import parse_and_build_ast
from semantic_analyzer import SemanticAnalyzer
from symbol_table import DATA_BASE


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TMP_CASES_DIR = PROJECT_ROOT / "examples" / "_semantic_smoke_tmp"


@dataclass
class SemanticCase:
    name: str
    source: str
    should_pass: bool
    validator: Optional[Callable] = None


def _assert(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def validate_symbol_layout(result):
    global_scope = result.symbol_table.global_scope

    _assert("g" in global_scope.symbols, "La variable global g debe existir.")
    _assert("sum" in global_scope.symbols, "La funcion sum debe existir.")
    _assert("main" in global_scope.symbols, "La funcion main debe existir.")

    global_var = global_scope.symbols["g"]
    sum_function = global_scope.symbols["sum"]

    _assert(global_var.segment == "global", "g debe asignarse al segmento global.")
    _assert(global_var.address == DATA_BASE, "g debe iniciar en la base de datos global.")

    _assert(sum_function.segment == "code", "Las funciones deben tener direccion de codigo.")
    _assert(sum_function.address is not None, "La funcion sum debe tener direccion asignada.")

    sum_scope = next(scope for scope in result.symbol_table.all_scopes if scope.name == "function:sum")
    _assert(sum_scope.symbols["a"].register == "p0", "El parametro a debe ir en p0.")
    _assert(sum_scope.symbols["b"].register == "p1", "El parametro b debe ir en p1.")

    label_kinds = {label.kind for label in result.labels}
    _assert("if_else" in label_kinds and "if_end" in label_kinds, "El if debe registrar labels.")
    _assert("for_start" in label_kinds and "for_end" in label_kinds, "El for debe registrar labels.")
    _assert("while_start" in label_kinds and "while_end" in label_kinds, "El while debe registrar labels.")


def validate_float_result(result):
    main_block_scope = next(
        scope for scope in result.symbol_table.all_scopes
        if scope.name.startswith("block:") and "value" in scope.symbols
    )
    value_symbol = main_block_scope.symbols["value"]
    _assert(str(value_symbol.type_info) == "float", "value debe registrarse como float.")


VALID_CASES = [
    SemanticCase(
        name="valid_symbols_memory_and_labels",
        source=(
            "int g = 1;\n"
            "func float sum(float a, int b){\n"
            "    float total = a + b;\n"
            "    if (true) {\n"
            "        ret total;\n"
            "    } else {\n"
            "        ret 0.0;\n"
            "    }\n"
            "}\n"
            "func void main(){\n"
            "    float value = sum(1.5, 2);\n"
            "    for (int i = 0; i += 1; i < 3) {\n"
            "        value = value + 1.0;\n"
            "    }\n"
            "    while (false) {\n"
            "        break;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=True,
        validator=validate_symbol_layout,
    ),
    SemanticCase(
        name="valid_float_promotions",
        source=(
            "func void main(){\n"
            "    float value = 1 + 2.5;\n"
            "    value = value + 3;\n"
            "}\n"
        ),
        should_pass=True,
        validator=validate_float_result,
    ),
]


INVALID_CASES = [
    SemanticCase(
        name="invalid_undeclared_reference",
        source=(
            "func void main(){\n"
            "    x = 1;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_wrong_argument_count",
        source=(
            "func int add(int a, int b){\n"
            "    ret a + b;\n"
            "}\n"
            "func void main(){\n"
            "    int x = add(1);\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_incompatible_argument",
        source=(
            "func void accept(bool flag){\n"
            "    ret;\n"
            "}\n"
            "func void main(){\n"
            "    accept(1);\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_condition_type",
        source=(
            "func void main(){\n"
            "    if (1) {\n"
            "        ret;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_missing_return",
        source=(
            "func int main(){\n"
            "    if (true) {\n"
            "        ret 1;\n"
            "    }\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_break_outside_loop",
        source=(
            "func void main(){\n"
            "    break;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_float_mod_assignment",
        source=(
            "func void main(){\n"
            "    float value = 1.5;\n"
            "    value %= 1.0;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_address_of_rvalue",
        source=(
            "func void main(){\n"
            "    int *p = &1;\n"
            "}\n"
        ),
        should_pass=False,
    ),
    SemanticCase(
        name="invalid_function_used_as_value",
        source=(
            "func int helper(){\n"
            "    ret 1;\n"
            "}\n"
            "func void main(){\n"
            "    int x = helper;\n"
            "}\n"
        ),
        should_pass=False,
    ),
]


CASES = VALID_CASES + INVALID_CASES


def run_case(case: SemanticCase) -> bool:
    input_path = TMP_CASES_DIR / f"{case.name}.f"
    input_path.write_text(case.source, encoding="utf-8")

    try:
        _, _, ast = parse_and_build_ast(input_path)
        result = SemanticAnalyzer().analyze(ast)
    except SystemExit as exc:
        print(f"[FAIL] {case.name}")
        print(f"       La fase previa aborto inesperadamente con codigo {exc.code}.")
        return False
    except Exception as exc:
        print(f"[FAIL] {case.name}")
        print(f"       Excepcion inesperada: {exc}")
        return False

    if case.should_pass:
        if result.has_errors:
            print(f"[FAIL] {case.name}")
            diagnostic = result.diagnostics[0]
            print(f"       Error inesperado: {diagnostic.code}")
            return False

        try:
            if case.validator is not None:
                case.validator(result)
        except AssertionError as exc:
            print(f"[FAIL] {case.name}")
            print(f"       {exc}")
            return False

        print(f"[OK]   {case.name}")
        return True

    if not result.has_errors:
        print(f"[FAIL] {case.name}")
        print("       Se esperaba al menos un error semantico.")
        return False

    print(f"[OK]   {case.name}")
    print(f"       {result.diagnostics[0].code}")
    return True


def main():
    print("Ejecutando pruebas de humo semanticas...\n")
    if TMP_CASES_DIR.exists():
        rmtree(TMP_CASES_DIR)
    TMP_CASES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        results = [run_case(case) for case in CASES]
    finally:
        if TMP_CASES_DIR.exists():
            rmtree(TMP_CASES_DIR)

    if all(results):
        print("\nTodas las pruebas semanticas pasaron.")
        return

    print("\nAl menos una prueba semantica fallo.")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
