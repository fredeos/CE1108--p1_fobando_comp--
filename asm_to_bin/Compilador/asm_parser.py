import re
from asm_to_bin import *
from clases import *

def parse_register(token: str, seguro: bool = False) -> str:
    token = token.strip().lower()

    if seguro:
        if token not in registros_seguros:
            raise ValueError(f"'{token}' no es un registro seguro válido")
        return token  # retorna 0-7
    else:
        if token not in registros_normales:
            raise ValueError(f"'{token}' no es un registro normal válido")
        return token  # retorna su dirección

def parse_immediate(token: str) -> int:
    token = token.strip()
    try:
        return int(token, 0)  # int(x, 0) detecta automáticamente hex (0x...) o decimal
    except ValueError:
        raise ValueError(f"Inmediato inválido: '{token}'")

def parse_label(instr: str):
    if not re.match(r'^\w+:\s*(.*)', instr):
        return None, None

    # separamos el nombre de la etiqueta de lo que queda de la linea
    parts = instr.split(":", 1)
    label = parts[0] # nombre de la etiqueta
    dpart = parts[1].split("=", 1) # separa lo que queda de la linea con =
    dir = dpart[1] # se consigue el num de memoria
    return label, dir

def parse_instr(instr: str) -> Optional[Instruction]:
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
            if op_clean == "seqz":
                rm = "zero"
            else:
                rm = parse_register(operands[2], seguro=es_segura)

        case ("clase2"):
            rd = parse_register(operands[0], seguro=es_segura)
            rn = parse_register(operands[1], seguro=es_segura)
            imm = parse_immediate(operands[2])

        case ("clase3"):
            rd = parse_register(operands[0], seguro=es_segura)
            mem = re.match(r'(-?\d+)\((\w+)\)', operands[1])
            imm = parse_immediate(mem.group(1))
            rn = parse_register(mem.group(2), seguro=es_segura)

        case ("claseB"):
            rn = parse_register(operands[0], seguro=es_segura)
            if op_clean == "beqz":
                rm = "zero"
                imm = parse_immediate(operands[1])
            else:
                rm = parse_register(operands[1], seguro=es_segura)
                imm = parse_immediate(operands[2])

        case ("claseJ"):
            if op_clean == "jal":
                rd = parse_register(operands[0], seguro=es_segura)
                imm = parse_immediate(operands[1])
            else:
                imm = parse_immediate(operands[0])

        case ("claseS"):
            if op_clean == "login":
                imm = parse_immediate(operands[0])

        case ("claseT"):
            if op_clean == "send":
                rd = parse_register(operands[0], seguro=True)
                rn = parse_register(operands[1], seguro=False)
            else:
                rd = parse_register(operands[0], seguro=False)
                rn = parse_register(operands[1], seguro=True)

        case ("claseE"):
            rd = parse_register(operands[0], seguro=True)
            rn = parse_register(operands[1], seguro=True)
            rm = parse_register(operands[2], seguro=True)
            sf = parse_register(operands[3], seguro=True)
            op1 = op[1:4]
            op2 = op[4:7]

        case ("claseMov"):
            rd = parse_register(operands[0], seguro=es_segura)
            if op_clean.endswith("i"):
                imm = parse_immediate(operands[1])
            else:
                rn = parse_register(operands[1], seguro=es_segura)

        case ("claseL"):
            rd = parse_register(operands[0], seguro=es_segura)
            imm = parse_immediate(operands[1])

    return Instruction(op=op, rd=rd, rn=rn, rm=rm, sf=sf, imm=imm, op1=op1, op2=op2)


def parse_assembly_file(filepath: str) -> list[Instruction]:
    """
    Funcion principal, se debe de llamar con el directorio del archivo
    Genera dos pasadas, la primera reconoce etiquetas con la direccion de memoria
    la segunda genera la lista de instrucciones
    """
    #labels = {}  # diccionario de etiquetas con su direccion de memoria correspondiente
    instructions = []  # instrucciones parseadas del codigo dado

    with open(filepath, 'r', encoding='utf-8') as f:
        asm = f.readlines()

    """for i in asm:
        raw_line = i.strip()
        label, dir = parse_label(raw_line)
        if label is not None:
            labels[label] = dir

    print(labels)"""
    for i in asm:
        raw_line = i.strip()
        instr = parse_instr(raw_line)
        if instr is not None:
            instructions.append(instr)

    return instructions


# --- USO ---
if __name__ == "__main__":
    instrucciones = parse_assembly_file("prueba.asm")
    for i, instr in enumerate(instrucciones):
        print(f"[{i}] {instr}")

    encoded_instructions = [inst.encode() for inst in instrucciones]

    # PASO B: Persistencia de archivos
    # Generamos la salida para el simulador y el binario para el hardware real.
    F32IS_Writer.save_bin("with_parser.bin", encoded_instructions)
    F32IS_Writer.save_hex("with_parser.hex", encoded_instructions)

    # PASO C: Reporte de depuración en consola
    # Este reporte ayuda a verificar que los saltos de PC (de 4 en 4) y los HEX sean correctos.
    print(f"\n{'#' * 15} F32IS SECURE SESSION REPORT {'#' * 15}")
    print(f"{'PC ADDR':<8} | {'HEX CONTENT':<13} | {'ASM MNEMONIC'}")
    print("-" * 45)

    for i, bin_str in enumerate(encoded_instructions):
        hex_val = f"{int(bin_str, 2):08X}"
        # Mostramos la operación original del objeto para comparar
        original_op = instrucciones[i].op
        print(f"0x{i * 4:02X}     | {hex_val}    | {original_op}")

    print(f"\n{'#' * 18} ASSEMBLY COMPLETE {'#' * 18}")
