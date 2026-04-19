from pathlib import Path
import importlib.util
import sys
from pprint import pprint

try:
    from antlr4 import FileStream, CommonTokenStream
    from antlr4.error.ErrorListener import ErrorListener
except ModuleNotFoundError as exc:
    if exc.name == "antlr4":
        sys.exit(
            "Error: falta instalar antlr4-python3-runtime. "
            "Ejecuta: python -m pip install -r fcc/requirements.txt"
        )
    raise


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


lexer_module = load_generated_module("FCCLexer")
parser_module = load_generated_module("FCCParser")

FCCLexer = lexer_module.FCCLexer
FCCParser = parser_module.FCCParser

from ast_builder import ASTBuilder


class SyntaxErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        print(f"Error [sintactico] en linea {line}, columna {column}: {msg}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python fcc/src/ast_driver.py <archivo_fuente>")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f'Error: no existe el archivo "{input_path}".')
        sys.exit(1)

    input_stream = FileStream(str(input_path), encoding="utf-8")

    lexer = FCCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = FCCParser(tokens)

    parser.removeErrorListeners()
    error_listener = SyntaxErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.has_error:
        sys.exit(1)

    builder = ASTBuilder()
    ast = builder.visit(tree)

    print("AST construido correctamente:\n")
    pprint(ast)


if __name__ == "__main__":
    main()