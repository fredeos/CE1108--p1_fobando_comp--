"""Parser ligero para convertir ensamblador FCC en objetos Instruction."""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Optional

from asm_to_bin import Instruction
from clases import INSTRUCTION_CLASSES, NORMAL_REGISTERS, SECURE_PRIMARY, SECURE_REGISTERS, SECURE_SECONDARY


def parse_register(token: str, secure: bool = False) -> str:
    """Valida y normaliza un operando de registro."""

    token = token.strip().lower()
    if secure and re.fullmatch(r"r[0-6]", token):
        # El backend usa r0-r6 como alias temporales del banco seguro escribible.
        return token
    valid_registers = SECURE_REGISTERS if secure else NORMAL_REGISTERS
    if token not in valid_registers:
        bank = "seguro" if secure else "normal"
        raise ValueError(f"'{token}' no es un registro {bank} valido")
    return token


def parse_immediate(token: str) -> int:
    """Convierte un inmediato decimal o hexadecimal a entero."""

    token = token.strip()
    try:
        return int(token, 0)
    except ValueError as exc:
        raise ValueError(f"Inmediato invalido: '{token}'") from exc


def parse_label(line: str) -> Optional[str]:
    """Retorna el nombre de una etiqueta si la linea corresponde a una."""

    match = re.match(r"^([A-Za-z_]\w*):", line.strip())
    return match.group(1) if match else None


def _parse_memory_operand(token: str, secure: bool) -> tuple[str, int, bool]:
    """Extrae base, magnitud e indicador de resta de un operando off(reg)."""

    match = re.fullmatch(r"(-?\d+)\((\w+)\)", token.strip())
    if not match:
        raise ValueError(f"Operando memoria invalido: '{token}'")
    offset = parse_immediate(match.group(1))
    base = parse_register(match.group(2), secure=secure)
    return base, abs(offset), offset < 0


def _build_secure_metadata(op: str) -> tuple[Optional[str], Optional[str]]:
    """Determina las funciones primaria/secundaria para instrucciones seguras."""

    return SECURE_PRIMARY.get(op), SECURE_SECONDARY.get(op)


def parse_instr(line: str) -> Optional[Instruction]:
    """Parsea una linea de ensamblador a un objeto Instruction."""

    line = re.split(r"[;#]", line, maxsplit=1)[0].strip()
    if not line or parse_label(line) is not None:
        return None

    parts = line.split(None, 1)
    op = parts[0].strip()
    raw_operands = parts[1] if len(parts) > 1 else ""
    is_secure = op.startswith("@")
    op_clean = op[1:] if is_secure else op

    instruction_class = INSTRUCTION_CLASSES.get(op_clean)
    if instruction_class is None:
        raise ValueError(f"Instruccion desconocida: {op_clean}")

    uses_secure_bank = (
        op_clean.startswith("p")
        or op_clean.startswith("ldv")
        or op_clean.startswith("stv")
    )

    operands = [operand.strip() for operand in raw_operands.split(",") if operand.strip()]
    rd = rn = rm = sf = imm = None
    op1, op2 = _build_secure_metadata(op_clean)

    match instruction_class:
        case "clase1":
            rd = parse_register(operands[0], secure=uses_secure_bank)
            rn = parse_register(operands[1], secure=uses_secure_bank)
            if op_clean == "seqz":
                rm = "zero"
            else:
                rm = parse_register(operands[2], secure=uses_secure_bank)
        case "clase2":
            rd = parse_register(operands[0], secure=uses_secure_bank)
            rn = parse_register(operands[1], secure=uses_secure_bank)
            imm = parse_immediate(operands[2])
        case "clase3":
            rd = parse_register(operands[0], secure=uses_secure_bank)
            rn, imm, subtract = _parse_memory_operand(operands[1], secure=uses_secure_bank)
        case "clase4":
            pass
        case "claseB":
            rn = parse_register(operands[0], secure=False)
            if op_clean == "beqz":
                rm = "zero"
                imm = parse_immediate(operands[1])
            else:
                rm = parse_register(operands[1], secure=False)
                imm = parse_immediate(operands[2])
        case "claseJ":
            if op_clean == "jal":
                rd = parse_register(operands[0], secure=False)
                imm = parse_immediate(operands[1])
            elif op_clean == "call":
                rd = "ra"
                imm = parse_immediate(operands[0])
            else:
                imm = parse_immediate(operands[0])
        case "claseS":
            if op_clean == "login":
                imm = parse_immediate(operands[0])
        case "claseT":
            if op_clean == "send":
                rd = parse_register(operands[0], secure=True)
                rn = parse_register(operands[1], secure=False)
            else:
                rd = parse_register(operands[0], secure=False)
                rn = parse_register(operands[1], secure=True)
        case "claseE":
            rd = parse_register(operands[0], secure=True)
            rn = parse_register(operands[1], secure=True)
            rm = parse_register(operands[2], secure=True)
            sf = parse_register(operands[3], secure=True)
        case "claseMov":
            rd = parse_register(operands[0], secure=uses_secure_bank)
            if op_clean.endswith("i"):
                imm = parse_immediate(operands[1])
            else:
                rn = parse_register(operands[1], secure=uses_secure_bank)
        case "claseL":
            rd = parse_register(operands[0], secure=uses_secure_bank)
            imm = parse_immediate(operands[1])
        case _:
            raise ValueError(f"Clase de instruccion no soportada: {instruction_class}")

    instruction = Instruction(
        op=op,
        rd=rd,
        rn=rn,
        rm=rm,
        sf=sf,
        imm=imm,
        op1=op1,
        op2=op2,
        is_secure=is_secure,
    )
    if instruction_class == "clase3":
        if uses_secure_bank:
            instruction.use_sub = subtract
        else:
            instruction.s_flag = subtract
    return instruction


def parse_assembly_text(text: str) -> List[Instruction]:
    """Parsea un bloque de ensamblador completo."""

    instructions: List[Instruction] = []
    for raw_line in text.splitlines():
        parsed = parse_instr(raw_line)
        if parsed is not None:
            instructions.append(parsed)
    return instructions


def parse_assembly_file(filepath: str | Path) -> List[Instruction]:
    """Parsea un archivo de ensamblador desde disco."""

    return parse_assembly_text(Path(filepath).read_text(encoding="utf-8"))
