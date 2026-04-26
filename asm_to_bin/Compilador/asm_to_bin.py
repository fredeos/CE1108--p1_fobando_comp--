from dataclasses import dataclass
from typing import Optional, List
import struct

@dataclass
class Instruction:
    op: str
    rd: Optional[int] = None   # Registro destino (o sd para seguros)
    rn: Optional[int] = None   # Primer registro fuente (o sn)
    rm: Optional[int] = None   # Segundo registro fuente (o sm)
    sf: Optional[int] = None   # Cuarto registro para PR (paddadd, etc)
    imm: Optional[int] = None
    is_secure: bool = False    # El bit 'P' de la especificación

    def _resolve_regs(self):
        """
        Traduce nombres de registros a sus direcciones físicas (0-31 o 0-7).
        Debe llamarse antes de encode().
        """
        # Identificar si la instrucción usa el banco seguro (Tipo PR, PI o T)
        # padd, psub, pmul (PR) / paddi, psubi (PI) / send, recv (T)
        secure_ops = ["padd", "psub", "pmul", "paddi", "psubi", "send", "recv"]
        is_secure_instr = self.op.strip("@") in secure_ops

        # Resolver RD
        if self.rd is not None and isinstance(self.rd, str):
            # En 'send/recv', rd es el registro seguro (sd)
            # En PR/PI, rd es el registro seguro (sd)
            is_rd_secure = is_secure_instr 
            self.rd = F32IS_Encoder.get_reg_addr(self.rd, is_rd_secure)

        # Resolver RN
        if self.rn is not None and isinstance(self.rn, str):
            # En 'send/recv', rn es un registro GENERAL (5 bits)
            # En PR/PI, rn es seguro (3 bits)
            is_rn_secure = is_secure_instr and self.op.strip("@") not in ["send", "recv"]
            self.rn = F32IS_Encoder.get_reg_addr(self.rn, is_rn_secure)

        # Resolver RM y SF (Siempre seguros si la instrucción es PR)
        if self.rm is not None and isinstance(self.rm, str):
            self.rm = F32IS_Encoder.get_reg_addr(self.rm, is_secure_instr)
        
        if self.sf is not None and isinstance(self.sf, str):
            self.sf = F32IS_Encoder.get_reg_addr(self.sf, is_secure_instr)



    def encode(self) -> str:
        """Punto de entrada principal para codificar a binario (32 bits)"""

        self._resolve_regs()

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

        tipo_b = ["beq", "bne"]

        tipo_j = ["jal", "j"]

        tipo_pr = ["padd", "psub", "pmul"]

        tipo_pi = ["paddi", "psubi"]

        tipo_t = ["send", "recv"]
        

        if self.op.startswith("@"):
            self.is_secure = True
            self.op = self.op[1:] # Quitamos el @ para buscar el opcode normal
        
        
        if self.op in tipo_r: return F32IS_Encoder.encode_r(self)
        if self.op in tipo_i: return F32IS_Encoder.encode_i(self)
        if self.op in tipo_m: return F32IS_Encoder.encode_m(self)
        if self.op in tipo_b: return F32IS_Encoder.encode_b(self)
        if self.op in tipo_j: return F32IS_Encoder.encode_j(self)
        if self.op in tipo_pr: return F32IS_Encoder.encode_pr(self)
        if self.op in tipo_pi: return F32IS_Encoder.encode_pi(self)
        if self.op in tipo_t: return F32IS_Encoder.encode_t(self)
        

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


    # Banco de registros (32 registros, 5 bits)
    GPR_MAP = {
        # Control y Argumentos
        "zero": 0, "ra": 1, "sp": 2, "pc": 3, "lr": 4,
        "p0": 5, "p1": 6, "p2": 7, "p3": 8, "p4": 9, "p5": 10, "p6": 11, "p7": 12, "p8": 13,
        
        # Propósito General (r0-r15 mapeados de 14 a 29)
        "r0": 14, "r1": 15, "r2": 16, "r3": 17, "r4": 18, "r5": 19, "r6": 20, "r7": 21,
        "r8": 22, "r9": 23, "r10": 24, "r11": 25, "r12": 26, "r13": 27, "r14": 28, "r15": 29,
        
        # Valores constantes
        "delta": 30, "max": 31
    }

    # Banco seguro de registros (8 registros, 3 bits)
    SECURE_MAP = {
        "ax": 0, "bx": 1, "cx": 2, "dx": 3,
        "ex": 4, "fx": 5, "gx": 6, "hx": 7
    }

    @staticmethod
    def get_reg_addr(name: str, is_secure_field: bool = False) -> int:
        """Convierte el nombre del registro a su dirección binaria."""
        name = name.lower().strip()
        if is_secure_field:
            if name in F32IS_Encoder.SECURE_MAP:
                return F32IS_Encoder.SECURE_MAP[name]
            raise ValueError(f"Registro seguro '{name}' no existe en el banco de 3 bits.")
        else:
            if name in F32IS_Encoder.GPR_MAP:
                return F32IS_Encoder.GPR_MAP[name]
            raise ValueError(f"Registro general '{name}' no existe en el banco de 5 bits.")

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

    @staticmethod
    def encode_b(inst: Instruction) -> str:
        """
        Formato Tipo B: P(1) | opcode(5) | func4(4) | rd(5) | rs1(5) | imm12(12)
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b01000), '05b')
        
        # En Tipo B, func4 suele indicar el tipo de comparación
        # beq: 0000 (comparar si rd == 0 o rd == rs1 según diseño)
        # Por ahora usaremos 0000 como estándar para saltos
        func4 = "0000" 
        
        rd = format(inst.rd or 0, '05b')
        rs1 = format(inst.rn or 0, '05b') # rn actúa como rs1
        
        # El salto suele ser PC-relative. 
        # Usamos complemento a dos para el offset (aquí sí se usa)
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b')
        
        return p + opcode + func4 + rd + rs1 + imm12
    
    @staticmethod
    def encode_j(inst: Instruction) -> str:
        """
        Formato Tipo J: P(1) | opcode(5) | rd(5) | imm21(21)
        """
        p = "1" if inst.is_secure else "0"
        # jal tiene opcode 01001
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b01001), '05b')
        
        rd = format(inst.rd or 0, '05b')
        
        # Inmediato de 21 bits en complemento a dos
        imm_val = inst.imm or 0
        # Máscara de 21 bits: (1 << 21) - 1 = 0x1FFFFF
        imm21 = format(imm_val & 0x1FFFFF, '021b')
        
        return p + opcode + rd + imm21
    
    # Mapeo de registros seguros (ax=0, bx=1, ..., hx=7)
    SECURE_REGS = {
        "ax": 0, "bx": 1, "cx": 2, "dx": 3,
        "ex": 4, "fx": 5, "gx": 6, "hx": 7
    }

    @staticmethod
    def encode_pr(inst: Instruction) -> str:
        """
        Formato Tipo PR: P(1)|opcode(5)|func4(4)|sd(3)|sn(3)|sm(3)|sf(3)|func10(10)
        """
        p = "1" # Siempre 1 para estas extensiones
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00010), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        
        # Registros de 3 bits
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        sm = format(inst.rm or 0, '03b')
        sf = format(inst.sf or 0, '03b')
        
        func10 = "0000000000" # Bits de relleno o funciones extra
        
        return p + opcode + func4 + sd + sn + sm + sf + func10

    @staticmethod
    def encode_pi(inst: Instruction) -> str:
        """
        Formato Tipo PI: P(1)|opcode(5)|func4(4)|sd(3)|sn(3)|imm16(16)
        """
        p = "1"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00011), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        
        # Inmediato más largo (16 bits)
        imm_val = inst.imm or 0
        imm16 = format(imm_val & 0xFFFF, '016b')
        
        return p + opcode + func4 + sd + sn + imm16
    
    @staticmethod
    def encode_t(inst: Instruction) -> str:
        """
        Formato Tipo T: P(1) | opcode(5) | func4(4) | sd(3) | rn(5) | func14(14)
        """
        p = "1" # Estas instrucciones requieren sesión iniciada (Hardware seguro)
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b10000), '05b')
        
        # func4: Diferenciamos entre send (0000) y recv (0001)
        func4 = "0000" if inst.op == "send" else "0001"
        
        sd = format(inst.rd or 0, '03b')  # Registro seguro (ax-hx)
        rn = format(inst.rn or 0, '05b')  # Registro general (ra, sp, r0...)
        
        func14 = "0" * 14 # Bits de control adicionales
        
        return p + opcode + func4 + sd + rn + func14
    

class F32IS_Writer:
    @staticmethod
    def to_bytes(binary_str: str):
        """Convierte una cadena de 32 bits '01...' en un objeto bytes de 4 bytes"""
        # Convertimos la cadena base 2 a un entero de 32 bits
        value = int(binary_str, 2)
        # Lo empaquetamos como Big Endian (el estándar para ISAs usualmente)
        # '>' es Big Endian, 'I' es unsigned int de 32 bits
        return struct.pack('>I', value)

    @staticmethod
    def save_bin(filename: str, instructions: list):
        """Genera un archivo binario puro"""
        with open(filename, 'wb') as f:
            for inst in instructions:
                f.write(F32IS_Writer.to_bytes(inst))
        print(f"Archivo binario guardado como: {filename}")

    @staticmethod
    def save_hex(filename: str, instructions: list):
        """Genera un archivo de texto con formato hexadecimal (Verilog/Intel HEX style)"""
        with open(filename, 'w') as f:
            for inst in instructions:
                value = int(inst, 2)
                # Formato: 8 caracteres hex por instrucción (32 bits)
                f.write(f"{value:08X}\n")
        print(f"Archivo hexadecimal guardado como: {filename}")

# --- Pruebas de instrucciones tipo R (Corregidas con nombres de registros reales F32IS) ---
print(f"\n{'-'*20} TIPO R {'-'*20}")

# 1. mul r1, p0, r1 (r1=15, p0=5)
# Objetivo: R[15] = R[5] * R[15]
# Nota: rm debe ser "r1" (15) para coincidir con el comentario, no "r15" (29)
inst1 = Instruction(op="mul", rd="r1", rn="p0", rm="r1") 
inst1._resolve_regs() 
bin1 = F32IS_Encoder.encode_r(inst1)
print(f"mul r1, p0, r1: {bin1}") 
# Desglose: P(0) | Op(00000) | F4(0100) | rd(01111) | rn(00101) | rm(01111) | F7(0000000)

# 2. add p0, r1, p1 (p0=5, r1=15, p1=6)
inst2 = Instruction(op="add", rd="p0", rn="r1", rm="p1")
inst2._resolve_regs()
bin2 = F32IS_Encoder.encode_r(inst2)
print(f"add p0, r1, p1: {bin2}")
# Desglose: rd=00101, rn=01111, rm=00110

# 3. sub r0, r1, r2 (r0=14, r1=15, r2=16)
# r0 es 14 según tu tabla
inst3 = Instruction(op="sub", rd="r0", rn="r1", rm="r2")
inst3._resolve_regs()
bin3 = F32IS_Encoder.encode_r(inst3)
print(f"sub r0, r1, r2: {bin3}")
# Desglose: rd=01110, rn=01111, rm=10000

# 4. xor r4, r4, r4 (r4=18)
inst4 = Instruction(op="xor", rd="r4", rn="r4", rm="r4")
inst4._resolve_regs()
bin4 = F32IS_Encoder.encode_r(inst4)
print(f"xor r4, r4, r4: {bin4}")
# Desglose: rd=rn=rm=10010

# 5. mov r1, ra (r1=15, ra=1)
# mov suele usar rm=zero (0) internamente
inst_mov = Instruction(op="mov", rd="r1", rn="ra")
inst_mov._resolve_regs()
bin_mov = F32IS_Encoder.encode_r(inst_mov)
print(f"mov r1, ra:    {bin_mov}") 

# 6. seq r1, r2, r3 (r1=15, r2=16, r3=17)
inst_seq = Instruction(op="seq", rd="r1", rn="r2", rm="r3")
inst_seq._resolve_regs()
bin_seq = F32IS_Encoder.encode_r(inst_seq)
print(f"seq r1, r2, r3: {bin_seq}")

# --- Pruebas de instrucciones Tipo I ---
# --- Pruebas de instrucciones tipo I (Corregidas con nombres reales) ---
print(f"\n{'-'*20} TIPO I {'-'*20}")

# 1. addi sp, sp, 8
# sp (2) -> sp (2) + 8
inst_addi = Instruction(op="addi", rd="sp", rn="sp", imm=8)
inst_addi._resolve_regs()
print(f"ADDI (sp, sp, 8):   {F32IS_Encoder.encode_i(inst_addi)}")
# Esperado: rd=00010, rn=00010, imm=000000001000

# 2. li r1, 2 (Mapeado internamente a addi/movi con zero)
# r1 (15) -> zero (0) + 2
inst_li = Instruction(op="li", rd="r1", rn="zero", imm=2)
inst_li._resolve_regs()
print(f"LI   (r1, 2):       {F32IS_Encoder.encode_i(inst_li)}")
# Esperado: rd=01111, rn=00000, imm=000000000010

# 3. xori r5, r5, 0xFFF
# r5 es 19 en tu tabla (r0=14 + 5)
inst_xori = Instruction(op="xori", rd="r5", rn="r5", imm=0xFFF)
inst_xori._resolve_regs()
print(f"XORI (r5, r5, 0xFFF): {F32IS_Encoder.encode_i(inst_xori)}")
# Esperado: rd=10011, rn=10011, imm=111111111111

# 4. subi sp, sp, 8 (Inmediato negativo)
inst_subi = Instruction(op="subi", rd="sp", rn="sp", imm=-8)
inst_subi._resolve_regs()
print(f"SUBI (sp, sp, -8):  {F32IS_Encoder.encode_i(inst_subi)}")
# Nota: El imm12 se codifica en complemento a dos dentro de encode_i

# --- Pruebas de instrucciones tipo M (Load/Store) ---
print(f"\n{'-'*20} TIPO M {'-'*20}")

# 1. stw ra, 0(sp)
# Guardar dirección de retorno (ra=1) en la dirección del stack (sp=2) + 0
inst_stw = Instruction(op="stw", rd="ra", rn="sp", imm=0)
inst_stw._resolve_regs()
print(f"stw ra, 0(sp):  {inst_stw.encode()}")
# Desglose: P(0) Op(00101) S(0) B(0) H(0) W(1) rd(00001) rn(00010) imm(000000000000)

# 2. ldb r1, -4(sp)
# Cargar un byte en r1 (15) desde sp (2) - 4
inst_ldb = Instruction(op="ldb", rd="r1", rn="sp", imm=-4)
inst_ldb._resolve_regs()
print(f"ldb r1, -4(sp): {inst_ldb.encode()}")
# Desglose: S(1) indica resta, B(1) indica byte, imm(000000000100) es abs(4)


# --- PRUEBAS TIPO B (Saltos Condicionales) ---
print(f"\n{'-'*20} TIPO B {'-'*20}")

# 1. beq r1, label (hacia adelante +16 bytes)
# rd: r1 (15), rn: zero (0) por defecto para comparar r1 con zero
inst_beq = Instruction(op="beq", rd="r1", rn="zero", imm=16)
inst_beq._resolve_regs()
print(f"beq r1, forward:  {inst_beq.encode()}")
# Desglose: imm12 es 000000010000 (16 en binario)

# 2. beq r1, label (hacia atrás -8 bytes)
inst_beq_back = Instruction(op="beq", rd="r1", rn="zero", imm=-8)
inst_beq_back._resolve_regs()
print(f"beq r1, backward: {inst_beq_back.encode()}")
# Desglose: imm12 en complemento a dos para -8 es 111111111000

# --- Pruebas de instrucciones tipo J (Saltos Largos) ---
print(f"\n{'-'*20} TIPO J {'-'*20}")

# 1. jal ra, label (ra=1, saltando 1000 bytes)
inst_jal = Instruction(op="jal", rd="ra", imm=1000)
inst_jal._resolve_regs()
print(f"JAL (ra, 1000):  {inst_jal.encode()}")
# Desglose: P(0) | Op(01001) | rd(00001) | imm21(1000 en binario)

# 2. j label (jal zero, offset)
# rd: zero (0), imm: -20 (salto hacia atrás)
inst_j = Instruction(op="j", rd="zero", imm=-20)
inst_j._resolve_regs()
print(f"J (offset -20):  {inst_j.encode()}")
# Desglose: rd(00000) | imm21(complemento a dos para -20)


# --- PRUEBAS SEGURIDAD (PR/PI) ---
print(f"\n{'-'*20} TIPO PR / PI (Secure) {'-'*20}")

# 1. padd ax, bx, cx (Tipo PR)
# Registros de 3 bits: ax=0, bx=1, cx=2. 
# Nota: _resolve_regs detecta que "padd" es una operación segura.
inst_pr = Instruction(op="padd", rd="ax", rn="bx", rm="cx")
inst_pr._resolve_regs()
print(f"PADD (ax, bx, cx):   {inst_pr.encode()}")
# Desglose: P(1) | Op(00010) | F4(0010) | sd(000) | sn(001) | sm(010) | sf(000)

# 2. paddi ax, bx, 100 (Tipo PI)
# Registros de 3 bits + Inmediato de 16 bits.
inst_pi = Instruction(op="paddi", rd="ax", rn="bx", imm=100)
inst_pi._resolve_regs()
print(f"PADDI (ax, bx, 100): {inst_pi.encode()}")
# Desglose: P(1) | Op(00011) | F4(0010) | sd(000) | sn(001) | imm16(100 en bin)

# --- Pruebas de instrucciones tipo T (Transporte Seguro <-> General) ---
print(f"\n{'-'*20} TIPO T {'-'*20}")

# 1. send ax, r0
# ax (Seguro): 0 | r0 (General): 14
inst_send = Instruction(op="send", rd="ax", rn="r0")
inst_send._resolve_regs()
print(f"SEND (ax, r0):  {inst_send.encode()}")
# Desglose: P(1) | Op(10000) | F4(0000) | sd(000) | rn(01110) | F14(0...0)

# 2. recv bx, r1
# bx (Seguro): 1 | r1 (General): 15
inst_recv = Instruction(op="recv", rd="bx", rn="r1")
inst_recv._resolve_regs()
print(f"RECV (bx, r1):  {inst_recv.encode()}")
# Desglose: P(1) | Op(10000) | F4(0001) | sd(001) | rn(01111) | F14(0...0)


# --- PRUEBA DE INSTRUCCIÓN CON @ (Bit P Dinámico) ---
print(f"\n{'-'*20} PRUEBA PREFIJO @ {'-'*20}")

# Caso con @: Activa el bit P de seguridad
# r3=17, r1=15, r2=16
inst_at = Instruction(op="@mul", rd="r3", rn="r1", rm="r2")
bin_at = inst_at.encode() # encode() llama automáticamente a _resolve_regs()

print(f"Instrucción original: @mul r3, r1, r2")
print(f"Binario generado:     {bin_at}")
print(f"Bit P (seguridad):    {bin_at[0]} <--- Debe ser 1")

# Caso sin @: Bit P en 0
inst_no_at = Instruction(op="mul", rd="r3", rn="r1", rm="r2")
bin_no_at = inst_no_at.encode()

print(f"\nInstrucción original: mul r3, r1, r2")
print(f"Binario generado:     {bin_no_at}")
print(f"Bit P (seguridad):    {bin_no_at[0]} <--- Debe ser 0")


# --- 1. Definición del programa ASM ---
program_asm = [
    # __init__
    Instruction(op="movi", rd="r1", imm=4),           # PC 0
    Instruction(op="movi", rd="p0", imm=7),           # PC 4
    Instruction(op="add",  rd="p1", rn="p0", rm="r1"), # PC 8
    Instruction(op="call", imm=8),                    # PC 12 -> Salto a PC 20 (sum)
    Instruction(op="mul",  rd="r1", rn="p0", rm="r1"), # PC 16

    # sum:
    Instruction(op="addi", rd="sp", rn="sp", imm=8),  # PC 20
    Instruction(op="stw",  rd="ra", rn="sp", imm=0),  # PC 24
    Instruction(op="stw",  rd="r1", rn="sp", imm=4),  # PC 28
    
    Instruction(op="li",   rd="r1", imm=2),           # PC 32
    Instruction(op="mul",  rd="r1", rn="p0", rm="r1"), # PC 36
    Instruction(op="add",  rd="p0", rn="r1", rm="p1"), # PC 40
    
    Instruction(op="ldw",  rd="r1", rn="sp", imm=4),  # PC 44
    Instruction(op="ldw",  rd="ra", rn="sp", imm=0),  # PC 48
    Instruction(op="addi", rd="sp", rn="sp", imm=-8), # PC 52
    Instruction(op="ret")                             # PC 56
]

# --- 2. Codificación y Ejecución de la Escritura ---
try:
    # Generamos la lista de strings binarios
    encoded_instructions = [inst.encode() for inst in program_asm]

    # Usamos tu clase F32IS_Writer
    F32IS_Writer.save_bin("sum_program.bin", encoded_instructions)
    F32IS_Writer.save_hex("sum_program.hex", encoded_instructions)

    # Reporte rápido en consola
    print(f"\n{'#'*10} REPORTE FINAL {'#'*10}")
    for i, bin_str in enumerate(encoded_instructions):
        print(f"PC {i*4:02d} | Hex: {int(bin_str, 2):08X} | {program_asm[i].op}")

except Exception as e:
    print(f" Error en el proceso: {e}")