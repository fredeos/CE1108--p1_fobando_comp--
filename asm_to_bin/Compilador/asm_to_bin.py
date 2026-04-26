from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Instruction:
    op: str
    rd: Optional[int] = None   # Registro destino (o sd para seguros)
    rn: Optional[int] = None   # Primer registro fuente (o sn)
    rm: Optional[int] = None   # Segundo registro fuente (o sm)
    sf: Optional[int] = None   # Cuarto registro para PR (paddadd, etc)
    imm: Optional[int] = None
    is_secure: bool = False    # El bit 'P' de la especificación

    def encode(self) -> str:
        """Punto de entrada principal para codificar a binario (32 bits)"""
       # Lista completa de instrucciones Tipo R según el ISA
        tipo_r = [
            "add", "sub", "mul", "div", "mod", 
            "and", "orr", "xor", "sll", "srl", 
            "mov", "seq"
        ]
        tipo_i = ["addi", "subi", "muli", "divi", "modi", "andi", "orri",
                   "xori", "slli", "srli", "movi", "seqi", "li", "la"
        ]

        tipo_m = ["ldw", "ldh", "ldb", "stw", "sth", "stb"]
        
        if self.op in tipo_r:
            return F32IS_Encoder.encode_r(self)
        if self.op in tipo_i:
            return F32IS_Encoder.encode_i(self)
        if self.op in tipo_m: 
            return F32IS_Encoder.encode_m(self)
        

        # ... más tipos adelante
        return "0" * 32

    def _to_bin(self, value: int, bits: int) -> str:
        """Helper para convertir enteros a binario con signo/relleno"""
        if value < 0: # Manejo de negativos para inmediatos
            value = (1 << bits) + value
        return format(value & ((1 << bits) - 1), f'0{bits}b')
    


class F32IS_Encoder:
    OPCODES = {
        "add":  0b00000, "sub":  0b00000, "mul":  0b00000, "div":  0b00000,
        "mod":  0b00000, "and":  0b00000, "orr":  0b00000, "xor":  0b00000,
        "sll":  0b00000, "srl":  0b00000, "mov":  0b00000, "seq":  0b00000,
        "addi": 0b00001, "subi": 0b00001, "muli": 0b00001, "divi": 0b00001,
        "modi": 0b00001, "andi": 0b00001, "orri": 0b00001, "xori": 0b00001,
        "slli": 0b00001, "srli": 0b00001, "movi": 0b00001, "seqi": 0b00001,
        "li":   0b00001, "la":   0b00001,
        "padd": 0b00010, "paddi":0b00011,
        "ldw":  0b00100, "ldh": 0b00100, "ldb": 0b00100,
        "stw":  0b00101, "sth": 0b00101, "stb": 0b00101,
        "beq":  0b01000, "jal":  0b01001,
        "send": 0b10000, "recv":0b10000,
        "login":0b10001, "quit":0b10001,
    }

    # Especificación de operación para ALU primaria
    FUNC4_ALU = {
        "sll": 0b0000, "slli": 0b0000,
        "srl": 0b0001, "srli": 0b0001,
        "add": 0b0010, "addi": 0b0010, "movi": 0b0010, "li": 0b0010, "la": 0b0010,
        "sub": 0b0011, "subi": 0b0011,
        "mul": 0b0100, "muli": 0b0100,
        "div": 0b0101, "divi": 0b0101,
        "mod": 0b0110, "modi": 0b0110,
        "and": 0b0111, "andi": 0b0111,
        "orr": 0b1000, "orri": 0b1000,
        "xor": 0b1001, "xori": 0b1001,
        "seq": 0b1010, "seqi": 0b1010,
    }

    @staticmethod
    def encode_r(inst: Instruction) -> str:
        # P | opcode | func4 | rd | rn | rm | func7
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0), '04b')
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        rm = format(inst.rm or 0, '05b')
        func7 = "0000000" # Valor base para Tipo R
        
        return p + opcode + func4 + rd + rn + rm + func7

    @staticmethod
    def encode_i(inst: Instruction) -> str:
        """
        Formato Tipo I: P(1) | opcode(5) | func4(4) | rd(5) | rn(5) | imm12(12)
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00001), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # El inmediato es de 12 bits
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b') 
        
        return p + opcode + func4 + rd + rn + imm12
    
    @staticmethod
    def encode_m(inst: Instruction) -> str:
        """
        Formato Tipo M: P(1)|opcode(5)|S(1)|B(1)|H(1)|W(1)|rd(5)|rn(5)|imm12(12)
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op[:3], 0b00100), '05b')
        
        # Bits de control de tamaño
        w = "1" if "w" in inst.op else "0"
        h = "1" if "h" in inst.op else "0"
        b = "1" if "b" in inst.op else "0"
        
        # S: Selección operación (0: suma, 1: resta)
        # Por defecto 0, a menos que el inmediato sea negativo
        s = "1" if (inst.imm is not None and inst.imm < 0) else "0"
        
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # Inmediato de 12 bits (siempre positivo en el campo, el signo va en S)
        imm_val = abs(inst.imm or 0)
        imm12 = format(imm_val & 0xFFF, '012b')
        
        return p + opcode + s + b + h + w + rd + rn + imm12
    


# --- Pruebas de instrucciones tipo R ---
print(f"\n{'-'*20} TIPO R {'-'*20}")

# 1. mul r1, p0, r1 (R[15] = R[5] * R[15])
# Basado en la línea 15 del ejemplo 'sum'
inst1 = Instruction(op="mul", rd=15, rn=5, rm=15)
bin1 = F32IS_Encoder.encode_r(inst1)
print(f"mul r1, p0, r1: {bin1}") 
# Desglose esperado: P(0) | Op(00000) | F4(0100) | rd(01111) | rn(00101) | rm(01111) | F7(0000000)

# 2. add p0, r1, p1 (R[5] = R[15] + R[6])
# Basado en la línea 16 del ejemplo 'sum'
inst2 = Instruction(op="add", rd=5, rn=15, rm=6)
bin2 = F32IS_Encoder.encode_r(inst2)
print(f"add p0, r1, p1: {bin2}")
# Desglose esperado: P(0) | Op(00000) | F4(0010) | rd(00101) | rn(01111) | rm(00110) | F7(0000000)

# 3. sub r0, r1, r2 (R[14] = R[15] - R[16])
# Operación aritmética general
inst3 = Instruction(op="sub", rd=14, rn=15, rm=16)
bin3 = F32IS_Encoder.encode_r(inst3)
print(f"sub r0, r1, r2: {bin3}")
# Desglose esperado: P(0) | Op(00000) | F4(0011) | rd(01110) | rn(01111) | rm(10000) | F7(0000000)

# 4. xor r4, r4, r4 (Limpiar registro r4)
inst4 = Instruction(op="xor", rd=18, rn=18, rm=18)
bin4 = F32IS_Encoder.encode_r(inst4)
print(f"xor r4, r4, r4: {bin4}")
# Desglose esperado: P(0) | Op(00000) | F4(1001) | rd(10010) | rn(10010) | rm(10010) | F7(0000000)

# 1. mov r1, ra (Mover ra al registro r1)
# ra es 1, r1 es 15
inst_mov = Instruction(op="mov", rd=15, rn=1)
bin_mov = F32IS_Encoder.encode_r(inst_mov)
print(f"mov r1, ra: {bin_mov}") 
# Nota: rm será 0 (registro zero) por defecto en tu clase, lo cual es correcto.

# 2. seq rd, rn, rm (Set if equal)
# Comparar si r2 == r3 y guardar resultado en r1
inst_seq = Instruction(op="seq", rd=15, rn=16, rm=17)
bin_seq = F32IS_Encoder.encode_r(inst_seq)
print(f"seq rd, rn, rm: {bin_seq}")

# --- Pruebas de instrucciones Tipo I ---

print(f"\n{'-'*20} TIPO I {'-'*20}")

# 1. addi sp, sp, 8
# rd: sp (2), rn: sp (2), imm: 8
# Formato: P(0) | Op(00001) | F4(0010) | rd(00010) | rn(00010) | imm12(000000001000)
inst_addi = Instruction(op="addi", rd=2, rn=2, imm=8)
print(f"ADDI (sp, sp, 8): {F32IS_Encoder.encode_i(inst_addi)}")

# 2. li r1, 2 (Mapeado a movi)
# rd: r1 (15), rn: zero (0), imm: 2
# Formato: P(0) | Op(00001) | F4(0010) | rd(01111) | rn(00000) | imm12(000000000010)
inst_li = Instruction(op="li", rd=15, imm=2)
print(f"LI   (r1, 2):    {F32IS_Encoder.encode_i(inst_li)}")

# 3. xori r5, r5, 0xFFF
# rd: r19 (19), rn: r19 (19), imm: 4095
inst_xori = Instruction(op="xori", rd=19, rn=19, imm=0xFFF)
print(f"XORI (r5, r5, -1): {F32IS_Encoder.encode_i(inst_xori)}")


# --- Pruebas de instrucciones tipo M ---
print(f"\n{'-'*20} TIPO M {'-'*20}")

# 1. stw ra, 0(sp) -> Guardar word de ra(1) en sp(2) + 0
# P(0) | Op(00101) | S(0) B(0) H(0) W(1) | rd(00001) | rn(00010) | imm(000000000000)
inst_stw = Instruction(op="stw", rd=1, rn=2, imm=0)
print(f"stw ra, 0(sp): {inst_stw.encode()}")

# 2. ldb r1, -4(sp) -> Cargar byte en r1(15) desde sp(2) - 4
# P(0) | Op(00100) | S(1) B(1) H(0) W(0) | rd(01111) | rn(00010) | imm(000000000100)
inst_ldb = Instruction(op="ldb", rd=15, rn=2, imm=-4)
print(f"ldb r1, -4(sp): {inst_ldb.encode()}")