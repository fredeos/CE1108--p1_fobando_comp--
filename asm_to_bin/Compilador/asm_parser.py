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


def parse_label(instr: str) -> Optional[Label]:
    print(1)

def parse_pseudo(op, operands) -> Instruction:
    print(1)

def parse_clase1():
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
    raw_operands = parts[1] if len(parts) > 1 else "" # los operandos

    is_secure = op.startswith('@')
    op_clean = op[1:] if is_secure else op  # op sin @ para comparar

    # 2. Revisar si es pseudo instruccion
    if op_clean in pseudo_instr:
        p_instr = parse_pseudo(op, raw_operands, labels, op_clean)  # op con @ si lo tenia
        return p_instr

    operands = [o.strip() for o in raw_operands.split(',')]
    op1 = op2 = rd = rn = rm = sf = imm = None

    # . Obtener tipo de estructura segun instruccion
    clase = instrucciones.get(op_clean)

    if clase is None:
        print(f"Instrucción desconocida: {op_clean}")
        return None

    match(clase):
        case("clase1"):
            rd = operands[0]
            rn = operands[1]
            rm = operands[2]
        case("clase2"):
            rd = operands[0]
            rn = operands[1]
            imm = operands[2]
        case("clase3"):
            rd = operands[0]
            # separar imm(rn)
            mem = re.match(r'(-?\d+)\((\w+)\)', operands[1])
            imm = mem.group(1)
            rn = mem.group(2)
        case ("claseB"):
            print("en proceso xd")
        #case ("claseJ"):

        #case ("claseS"):

        #case ("claseT"):

        #case ("claseE"):

        #case ("claseMov"):

    return Instruction(op=op, rd=rd, rn=rn, rm=rm, sf=sf, imm=imm)


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