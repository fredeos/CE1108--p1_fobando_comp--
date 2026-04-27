from dataclasses import dataclass
from typing import Optional, List
import re
from asm_to_bin import *
from clases import *


@dataclass
class Label:
    # se crea esta clase para guardar la etiqueta con su respectiva direccion de memoria
    label: str
    dir: int


def parse_register(token: str, seguro: bool = False) -> int:
    token = token.strip().lower()

    if seguro:
        if token not in registros_seguros:
            raise ValueError(f"'{token}' no es un registro seguro válido")
        return token  # retorna 0-7
    else:
        if token not in registros_normales:
            raise ValueError(f"'{token}' no es un registro normal válido")
        return token  # retorna su dirección


def parse_label(instr: str) -> Optional[Label]:
    if not re.match(r'^\w+:\s*(.*)', instr):
        return None

    # separamos el nombre de la etiqueta de lo que queda de la linea
    parts = instr.split(":", 1)
    label = parts[0]
    print(label)





def parse_pseudo(op, operands, labels, opclean) -> Instruction:
    print(1)


def parse_instr(instr: str, labels) -> Optional[Instruction]:
    """
        Parsea una línea de ensamblador y retorna un Instruction, o None si
        la línea es vacía, comentario o etiqueta.
        """
    # Eliminar comentarios en la misma linea de instruccion
    instr = re.split(r'[;#]', instr)[0].strip()

    if not instr:
        return None  # Linea vacía o solo comentario

    if re.match(r'^\w+:\s*(.*)', instr):
        return None  # si ve que es etiqueta

    # 1. Separar la operacion de la instr
    parts = instr.split(None, 1)  # solo dividir en 2
    op = parts[0].strip().lower()  # poner en minusculas por si acaso
    raw_operands = parts[1] if len(parts) > 1 else ""  # los operandos

    # 2. Verificar si tiene @
    is_secure = op.startswith('@')
    op_clean = op[1:] if is_secure else op  # op sin @ para comparar

    # 3. saber si la instruccion usa registros seguros
    es_segura = op_clean.startswith('p') and op_clean not in ("pc",)

    # 4. Revisar si es pseudo instruccion
    if op_clean in pseudo_instr:
        p_instr = parse_pseudo(op, raw_operands, labels, op_clean)  # op con @ si lo tenia
        return p_instr

    # 5. Obtener los operandos en una lista por separado
    operands = [o.strip() for o in raw_operands.split(',')]

    # 6. Colocar los valores de la clase Instruction en None
    op1 = op2 = rd = rn = rm = sf = imm = None

    # 7. Obtener tipo de estructura segun instruccion
    clase = instrucciones.get(op_clean)

    if clase is None:
        print(f"Instrucción desconocida: {op_clean}")
        return None

    match (clase):
        case ("clase1"):
            rd = parse_register(operands[0], seguro=es_segura)
            rn = parse_register(operands[1], seguro=es_segura)
            rm = parse_register(operands[2], seguro=es_segura)

        case ("clase2"):
            rd = parse_register(operands[0], seguro=es_segura)
            rn = parse_register(operands[1], seguro=es_segura)
            imm = operands[2]

        case ("clase3"):
            rd = parse_register(operands[0], seguro=es_segura)
            mem = re.match(r'(-?\d+)\((\w+)\)', operands[1])
            imm = mem.group(1)
            rn = parse_register(mem.group(2), seguro=es_segura)

        case ("claseB"):
            # OCUPA LISTA LABELS
            print("en proceso xd")
        case ("claseJ"):
            # OCUPA LISTA LABELS
            print("en proceso xd")

        case ("claseS"):
            if op_clean == "login":
                imm = operands[0]

        case ("claseT"):
            # send: sd(seguro), rn(normal) — recv: rd(normal), sm(seguro)
            if op_clean == "send":
                rd = parse_register(operands[0], seguro=True)
                rn = parse_register(operands[1], seguro=False)
            else:  # recv
                rd = parse_register(operands[0], seguro=False)
                rn = parse_register(operands[1], seguro=True)

        case ("claseE"):
            rd = parse_register(operands[0], seguro=True)
            rn = parse_register(operands[1], seguro=True)
            rm = parse_register(operands[2], seguro=True)
            sf = parse_register(operands[3], seguro=True)

            op1 = op[1:4]  # agarra de la primera op
            op2 = op[4:7]  # agarra de la segunda op

        case ("claseMov"):
            rd = parse_register(operands[0], seguro=es_segura)
            if op.endswith("i"):
                imm = operands[1]
            else:
                rn = parse_register(operands[1], seguro=es_segura)

        case ("claseL"):
            rd = parse_register(operands[0], seguro=es_segura)
            imm = operands[1]

    return Instruction(op=op, rd=rd, rn=rn, rm=rm, sf=sf, imm=imm, op1=op1, op2=op2)


def parse_assembly_file(filepath: str) -> list[Instruction]:
    """
    Funcion principal, se debe de llamar con el directorio del archivo
    Genera dos pasadas, la primera reconoce etiquetas con la direccion de memoria
    la segunda genera la lista de instrucciones
    """
    labels = []  # lista de etiquetas con su direccion de memoria correspondiente
    instructions = []  # instrucciones parseadas del codigo dado

    with open(filepath, 'r', encoding='utf-8') as f:
        asm = f.readlines()

    print(asm)

    for i in asm:
        raw_line = i.strip()
        label = parse_label(raw_line)
        if label is not None:
            labels.append(label)

    for i in asm:
        raw_line = i.strip()
        instr = parse_instr(raw_line, labels)
        if instr is not None:
            instructions.append(instr)

    return instructions


# --- USO ---
if __name__ == "__main__":
    instrucciones = parse_assembly_file("prueba.asm")
    print("aloooooooooo")

    for i, instr in enumerate(instrucciones):
        print(f"{instr}")
