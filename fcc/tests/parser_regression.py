from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys
import tempfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PARSER_DRIVER = PROJECT_ROOT / "src" / "parser_driver.py"


@dataclass
class ParserCase:
    name: str
    source: str
    should_succeed: bool
    expected_text: str


CASES = [
    ParserCase(
        name="import_without_semicolon",
        source='traigase "std/io"\nfunc void main(){}\n',
        should_succeed=True,
        expected_text="Analisis sintactico correcto",
    ),
    ParserCase(
        name="import_with_semicolon_rejected",
        source='traigase "std/io";\nfunc void main(){}\n',
        should_succeed=False,
        expected_text="Error [sintactico]",
    ),
    ParserCase(
        name="main_can_be_called",
        source=(
            "func int main(){\n"
            "    ret 1;\n"
            "}\n"
            "\n"
            "func void caller(){\n"
            "    int value = main();\n"
            "}\n"
        ),
        should_succeed=True,
        expected_text="CallNode",
    ),
    ParserCase(
        name="float_and_real_literals",
        source=(
            "func void main(){\n"
            "    float y = 10.5;\n"
            "    y = y + 1.0;\n"
            "}\n"
        ),
        should_succeed=True,
        expected_text="literal_type='float'",
    ),
    ParserCase(
        name="global_var_and_secure_function",
        source=(
            "int counter;\n"
            "@secure(0xFF)\n"
            "func void main(){\n"
            "    counter = 1;\n"
            "}\n"
        ),
        should_succeed=True,
        expected_text="secure=SecureAnnotationNode",
    ),
    ParserCase(
        name="for_loop_conventional_order",
        source=(
            "func void main(){\n"
            "    for (int i = 0; i < 10; i += 1) {\n"
            "        continue;\n"
            "    }\n"
            "}\n"
        ),
        should_succeed=True,
        expected_text="ForNode",
    ),
    ParserCase(
        name="nested_blocks_if_elif_else",
        source=(
            "func void main(){\n"
            "    if (1 < 2) {\n"
            "        int x = 0;\n"
            "    } elif (2 < 3) {\n"
            "        int y = 1;\n"
            "    } else {\n"
            "        int z = 2;\n"
            "    }\n"
            "}\n"
        ),
        should_succeed=True,
        expected_text="IfNode",
    ),
    ParserCase(
        name="missing_semicolon",
        source=(
            "func void main(){\n"
            "    int x = 1\n"
            "    ret x;\n"
            "}\n"
        ),
        should_succeed=False,
        expected_text='se esperaba ";" al final de la sentencia.',
    ),
    ParserCase(
        name="missing_block_closure",
        source=(
            "func void main(){\n"
            "    if (1 < 2) {\n"
            "        int x = 0;\n"
            "    else {\n"
            "        int y = 1;\n"
            "    }\n"
            "}\n"
        ),
        should_succeed=False,
        expected_text='token inesperado "else".',
    ),
    ParserCase(
        name="malformed_real_reported_as_lexical_error",
        source=(
            "func void main(){\n"
            "    float y = 10.5.3;\n"
            "}\n"
        ),
        should_succeed=False,
        expected_text='Error [lexico] en linea 2: numero real "10.5.3" mal formado.',
    ),
    ParserCase(
        name="unexpected_top_level_statement",
        source=(
            "if (1 < 2) {\n"
            "    int x = 0;\n"
            "}\n"
        ),
        should_succeed=False,
        expected_text='Error [sintactico] en linea 1',
    ),
]


def run_case(case: ParserCase) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        input_path = Path(temp_dir) / f"{case.name}.f"
        input_path.write_text(case.source, encoding="utf-8")

        result = subprocess.run(
            [sys.executable, str(PARSER_DRIVER), str(input_path)],
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT.parent),
        )

    output = (result.stdout + result.stderr).strip()
    success = result.returncode == 0

    passed = success == case.should_succeed and case.expected_text in output
    return passed, output


def main():
    failures = []

    for case in CASES:
        passed, output = run_case(case)
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {case.name}")

        if not passed:
            failures.append((case, output))

    if failures:
        print("\nDetalles de fallos:\n")
        for case, output in failures:
            print(f"Caso: {case.name}")
            print(f"Esperaba exito: {case.should_succeed}")
            print(f"Texto esperado: {case.expected_text}")
            print("Salida:")
            print(output or "<sin salida>")
            print("-" * 60)
        sys.exit(1)

    print(f"\nTodas las pruebas del parser pasaron ({len(CASES)} casos).")


if __name__ == "__main__":
    main()
