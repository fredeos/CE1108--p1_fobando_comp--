from dataclasses import dataclass
from typing import Optional, List
import struct

@dataclass
class Instruction:
    """
    Handles F32IS instruction components and mnemonic-to-address resolution.
    
    Attributes:
        op (str): Operation name (e.g., 'add', '@mul').
        rd (Optional[int]): Destination register (GPR or Secure sd).
        rn (Optional[int]): First source register (GPR or Secure sn).
        rm (Optional[int]): Second source register (GPR or Secure sm).
        sf (Optional[int]): Fourth register field for PR-type ops.
        imm (Optional[int]): Immediate value or offset.
        is_secure (bool): Specification 'P' bit status.
    """
    op: str
    rd: Optional[int] = None
    rn: Optional[int] = None
    rm: Optional[int] = None
    sf: Optional[int] = None
    imm: Optional[int] = None
    is_secure: bool = False

    def _resolve_regs(self):
        """
        Translates register aliases to physical addresses (0-31 or 0-7).
        Must be executed prior to encode().
        """
        # Identify if the instruction targets the Secure Register Bank (PR, PI, or T types)
        secure_ops = ["padd", "psub", "pmul", "paddi", "psubi", "send", "recv"]
        is_secure_instr = self.op.strip("@") in secure_ops

        # Resolve Destination Register (rd)
        if self.rd is not None and isinstance(self.rd, str):
            # For PR/PI and send/recv, rd maps to the Secure Bank (sd)
            is_rd_secure = is_secure_instr 
            self.rd = F32IS_Encoder.get_reg_addr(self.rd, is_rd_secure)

        # Resolve First Source Register (rn)
        if self.rn is not None and isinstance(self.rn, str):
            # Special case: 'send/recv' use General GPR for rn (5 bits), others use Secure (3 bits)
            is_rn_secure = is_secure_instr and self.op.strip("@") not in ["send", "recv"]
            self.rn = F32IS_Encoder.get_reg_addr(self.rn, is_rn_secure)

        # Resolve Second Source (rm) and Fourth Field (sf)
        # Always mapped as Secure registers if the base instruction is a Secure type
        if self.rm is not None and isinstance(self.rm, str):
            self.rm = F32IS_Encoder.get_reg_addr(self.rm, is_secure_instr)
        
        if self.sf is not None and isinstance(self.sf, str):
            self.sf = F32IS_Encoder.get_reg_addr(self.sf, is_secure_instr)


    def encode(self) -> str:
        """
        Main entry point for 32-bit binary encoding.
        
        This method handles:
        1. Register resolution via _resolve_regs().
        2. Detection of the '@' security prefix to set the 'is_secure' bit.
        3. Dispatching to specific encoding methods based on the instruction type 
           (R, I, M, B, J, PR, PI, T).
        """
        # (Internal logic for type lists and secure bit detection)
        self._resolve_regs()

        tipo_r = ["add", "sub", "mul", "div", "mod", "and", "orr", "xor", "sll", "srl", "mov", "seq"]
        tipo_i = ["addi", "subi", "muli", "divi", "modi", "andi", "orri", "xori", "slli", "srli", "movi", "seqi", "li", "la"]
        tipo_m = ["ldw", "ldh", "ldb", "stw", "sth", "stb"]
        tipo_b = ["beq", "bne"]
        tipo_j = ["jal", "j"]
        tipo_pr = ["padd", "psub", "pmul"]
        tipo_pi = ["paddi", "psubi"]
        tipo_t = ["send", "recv"]
        tipo_sys = ["login", "quit"]

        if self.op.startswith("@"):
            self.is_secure = True
            self.op = self.op[1:] 

        # Type-based dispatching
        if self.op in tipo_r: return F32IS_Encoder.encode_r(self)
        if self.op in tipo_i: return F32IS_Encoder.encode_i(self)
        if self.op in tipo_m: return F32IS_Encoder.encode_m(self)
        if self.op in tipo_b: return F32IS_Encoder.encode_b(self)
        if self.op in tipo_j: return F32IS_Encoder.encode_j(self)
        if self.op in tipo_pr: return F32IS_Encoder.encode_pr(self)
        if self.op in tipo_pi: return F32IS_Encoder.encode_pi(self)
        if self.op in tipo_t: return F32IS_Encoder.encode_t(self)
        if self.op in tipo_sys: return F32IS_Encoder.encode_sys(self)

        return "0" * 32

    def _to_bin(self, value: int, bits: int) -> str:
        """
        Helper to convert integers to binary strings with padding and sign handling.
        Uses two's complement for negative immediate values.
        """
        if value < 0: 
            value = (1 << bits) + value
        return format(value & ((1 << bits) - 1), f'0{bits}b')
    

class F32IS_Encoder:
    """
    Encoder constants and mapping for the F32IS Architecture.
    
    This class defines the operational codes (Opcodes), ALU function 
    specifiers (FUNC4), and register file mappings required to 
    translate assembly instructions into machine code.
    """

    # Primary Operation Codes (5 bits)
    # Categorizes instructions into formats (R, I, M, B, J, etc.)
    OPCODES = {
        "add":   0b00000, "sub":  0b00000, "mul":  0b00000, "div":  0b00000,
        "mod":   0b00000, "and":  0b00000, "orr":  0b00000, "xor":  0b00000,
        "sll":   0b00000, "srl":  0b00000, "mov":  0b00000, "seq":  0b00000,
        "addi":  0b00001, "subi": 0b00001, "muli": 0b00001, "divi": 0b00001,
        "modi":  0b00001, "andi": 0b00001, "orri": 0b00001, "xori": 0b00001,
        "slli":  0b00001, "srli": 0b00001, "movi": 0b00001, "seqi": 0b00001,
        "li":    0b00001, "la":   0b00001,
        "padd":  0b00010, "paddi":0b00011,
        "ldw":   0b00100, "ldh":  0b00100, "ldb":  0b00100,
        "stw":   0b00101, "sth":  0b00101, "stb":  0b00101,
        "beq":   0b01000, "jal":  0b01001,
        "send":  0b10000, "recv": 0b10000,
        "login": 0b10001, "quit": 0b10001,
    }

    # ALU Function Specifiers (4 bits)
    # Used by the Control Unit to select the specific operation within the ALU
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

    # General Purpose Register (GPR) Map (5 bits - 32 Registers)
    # Includes control registers, function arguments (p0-p8), 
    # and general-purpose registers (r0-r15)
    GPR_MAP = {
        # Control & Argument Registers
        "zero": 0, "ra": 1, "sp": 2, "pc": 3, "lr": 4,
        "p0": 5, "p1": 6, "p2": 7, "p3": 8, "p4": 9, "p5": 10, "p6": 11, "p7": 12, "p8": 13,
        
        # General Purpose (r0-r15 mapped from 14 to 29)
        "r0": 14, "r1": 15, "r2": 16, "r3": 17, "r4": 18, "r5": 19, "r6": 20, "r7": 21,
        "r8": 22, "r9": 23, "r10": 24, "r11": 25, "r12": 26, "r13": 27, "r14": 28, "r15": 29,
        
        # Hardcoded Constants
        "delta": 30, "max": 31
    }

    # Secure Register Bank Map (3 bits - 8 Registers)
    # Specialized registers used for cryptographic or secure data handling
    SECURE_MAP = {
        "ax": 0, "bx": 1, "cx": 2, "dx": 3,
        "ex": 4, "fx": 5, "gx": 6, "hx": 7
    }

    @staticmethod
    def get_reg_addr(name: str, is_secure_field: bool = False) -> int:
        """
        Translates a register mnemonic into its physical binary address.
        
        Args:
            name (str): The register name (e.g., 'sp', 'ax').
            is_secure_field (bool): If True, look up in the 3-bit Secure bank.
                                   If False, look up in the 5-bit GPR bank.
        Returns:
            int: The physical address of the register.
        """
        name = name.lower().strip()
        if is_secure_field:
            if name in F32IS_Encoder.SECURE_MAP:
                return F32IS_Encoder.SECURE_MAP[name]
            raise ValueError(f"Secure register '{name}' not found in 3-bit bank.")
        else:
            if name in F32IS_Encoder.GPR_MAP:
                return F32IS_Encoder.GPR_MAP[name]
            raise ValueError(f"General register '{name}' not found in 5-bit bank.")

    @staticmethod
    def encode_r(inst: Instruction) -> str:
        """
        Encodes Type-R instructions (Register-to-Register).
        Format: P(1) | Opcode(5) | Func4(4) | rd(5) | rn(5) | rm(5) | Func7(7)
        Total: 32 bits.
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0), '04b')
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        rm = format(inst.rm or 0, '05b')
        func7 = "0000000" # Base padding/extension for Type-R
        
        return p + opcode + func4 + rd + rn + rm + func7

    @staticmethod
    def encode_i(inst: Instruction) -> str:
        """
        Encodes Type-I instructions (Immediate arithmetic/logic).
        Format: P(1) | Opcode(5) | Func4(4) | rd(5) | rn(5) | Immediate(12)
        Total: 32 bits.
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00001), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # Immediate is truncated/masked to 12 bits
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b') 
        
        return p + opcode + func4 + rd + rn + imm12
    
    @staticmethod
    def encode_m(inst: Instruction) -> str:
        """
        Encodes Type-M instructions (Memory Load/Store).
        Format: P(1)|Opcode(5)|S(1)|B(1)|H(1)|W(1)|rd(5)|rn(5)|Immediate12(12)
        
        Fields:
            S: Operation selection (0: addition, 1: subtraction for offset).
            B, H, W: Size control bits (Byte, Half, Word).
            Immediate: 12-bit magnitude (sign is handled by S bit).
        """
        p = "1" if inst.is_secure else "0"
        # Opcode lookup based on first 3 chars (ldw/stw)
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op[:3], 0b00100), '05b')
        
        # Size control flags based on mnemonic suffix
        w = "1" if "w" in inst.op else "0"
        h = "1" if "h" in inst.op else "0"
        b = "1" if "b" in inst.op else "0"
        
        # S bit: 1 if immediate is negative, 0 otherwise
        s = "1" if (inst.imm is not None and inst.imm < 0) else "0"
        
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # 12-bit immediate (absolute value stored in field)
        imm_val = abs(inst.imm or 0)
        imm12 = format(imm_val & 0xFFF, '012b')
        
        return p + opcode + s + b + h + w + rd + rn + imm12

    @staticmethod
    def encode_b(inst: Instruction) -> str:
        """
        Encodes Type-B instructions (Conditional Branches).
        Format: P(1) | Opcode(5) | Func4(4) | rd(5) | rs1(5) | Immediate12(12)
        
        Note:
            Immediate is encoded in two's complement for PC-relative offsets.
            rn is mapped to the rs1 field.
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b01000), '05b')
        
        # Func4 typically defines comparison logic (defaulting to 0000)
        func4 = "0000" 
        
        rd = format(inst.rd or 0, '05b')
        rs1 = format(inst.rn or 0, '05b')
        
        # PC-relative offset in 12-bit two's complement
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b')
        
        return p + opcode + func4 + rd + rs1 + imm12
    
    @staticmethod
    def encode_j(inst: Instruction) -> str:
        """
        Encodes Type-J instructions (Unconditional Jumps/Link).
        Format: P(1) | Opcode(5) | rd(5) | Immediate21(21)
        
        Total: 32 bits.
        The 21-bit immediate allows for a large jump range in two's complement.
        """
        p = "1" if inst.is_secure else "0"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b01001), '05b')
        
        rd = format(inst.rd or 0, '05b')
        
        # 21-bit two's complement immediate
        imm_val = inst.imm or 0
        imm21 = format(imm_val & 0x1FFFFF, '021b')
        
        return p + opcode + rd + imm21
    
    # Secure register mapping (ax=0, bx=1, ..., hx=7)
    # These 3-bit identifiers are used in PR, PI, and T instruction formats.
    SECURE_REGS = {
        "ax": 0, "bx": 1, "cx": 2, "dx": 3,
        "ex": 4, "fx": 5, "gx": 6, "hx": 7
    }

    @staticmethod
    def encode_pr(inst: Instruction) -> str:
        """
        Encodes Type-PR instructions (Secure Register-to-Register).
        Format: P(1)|Opcode(5)|Func4(4)|sd(3)|sn(3)|sm(3)|sf(3)|Func10(10)
        
        Fields:
            sd, sn, sm, sf: 3-bit secure register indices.
            Func10: Padding or auxiliary control bits.
        """
        p = "1" # P-bit is always 1 for secure extensions
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00010), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        
        # Mapping 3-bit registers (Secure Bank)
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        sm = format(inst.rm or 0, '03b')
        sf = format(inst.sf or 0, '03b')
        
        func10 = "0000000000" 
        
        return p + opcode + func4 + sd + sn + sm + sf + func10

    @staticmethod
    def encode_pi(inst: Instruction) -> str:
        """
        Encodes Type-PI instructions (Secure Immediate).
        Format: P(1)|Opcode(5)|Func4(4)|sd(3)|sn(3)|Immediate16(16)
        
        Note:
            Uses a larger 16-bit immediate compared to standard I-types.
        """
        p = "1"
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00011), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        
        # 16-bit immediate value
        imm_val = inst.imm or 0
        imm16 = format(imm_val & 0xFFFF, '016b')
        
        return p + opcode + func4 + sd + sn + imm16
    
    @staticmethod
    def encode_t(inst: Instruction) -> str:
        """
        Encodes Type-T instructions (Transport/Move between banks).
        Format: P(1) | Opcode(5) | Func4(4) | sd(3) | rn(5) | Func14(14)
        
        Logic:
            This type moves data between the 3-bit Secure bank (sd) 
            and the 5-bit General Purpose bank (rn).
        """
        p = "1" # Hardware security bit enabled
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b10000), '05b')
        
        # func4: Differentiates between 'send' (0000) and 'recv' (0001)
        func4 = "0000" if inst.op == "send" else "0001"
        
        sd = format(inst.rd or 0, '03b')  # Secure register index (ax-hx)
        rn = format(inst.rn or 0, '05b')  # GPR index (ra, sp, r0-r15)
        
        func14 = "0" * 14 # Additional control padding
        
        return p + opcode + func4 + sd + rn + func14
    
    @staticmethod
    def encode_sys(inst: Instruction) -> str:
        """
        Format to Login/Quit: P(1) | Opcode(5) | Unused(5) | Immediate21(21)
        Nota: 'login' use the inmidiate for key, 'quit' ignore that.
        """
        p = "0" # Login/Quit son instrucciones de control de estado
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b10001), '05b')
        
        # rd/unused: 5 bits en cero ya que login no escribe en registros
        unused = "00000"
        
        # Inmediato de 21 bits para la llave (0xBEEF0 cabe perfectamente)
        imm_val = inst.imm or 0
        imm21 = format(imm_val & 0x1FFFFF, '021b')
        
        return p + opcode + unused + imm21
    
class F32IS_Writer:
    """
    Handles the physical output generation for the F32IS assembler.
    
    This class converts internal binary strings into finalized file formats,
    ensuring correct byte alignment and endianness for hardware compatibility.
    """

    @staticmethod
    def to_bytes(binary_str: str):
        """
        Converts a 32-bit binary string into a 4-byte object.
        
        Uses Big Endian byte order ('>'), which is the architectural 
        standard for F32IS instruction fetch.
        
        Args:
            binary_str (str): A string of 32 characters ('0' or '1').
        Returns:
            bytes: A 4-byte packed representation of the instruction.
        """
        # Convert base-2 string to a 32-bit integer
        value = int(binary_str, 2)
        # Pack as Big Endian (>) Unsigned Int (I)
        return struct.pack('>I', value)

    @staticmethod
    def save_bin(filename: str, instructions: list):
        """
        Generates a raw binary executable file.
        
        This format is intended for direct loading into physical 
        RAM or Flash memory modules.
        
        Args:
            filename (str): The output path (e.g., 'program.bin').
            instructions (list): List of 32-bit binary strings.
        """
        with open(filename, 'wb') as f:
            for inst in instructions:
                f.write(F32IS_Writer.to_bytes(inst))
        print(f"Binary file successfully saved as: {filename}")

    @staticmethod
    def save_hex(filename: str, instructions: list):
        """
        Generates a text-based hexadecimal file.
        
        Compatible with Verilog $readmemh, Logisim memory loads, 
        and Intel HEX-style debuggers.
        
        Args:
            filename (str): The output path (e.g., 'program.hex').
            instructions (list): List of 32-bit binary strings.
        """
        with open(filename, 'w') as f:
            for inst in instructions:
                value = int(inst, 2)
                # Format: 8-character uppercase hex padding (32 bits)
                f.write(f"{value:08X}\n")
        print(f"Hexadecimal file successfully saved as: {filename}")


"""
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
"""

# ==============================================================================
# 1. DEFINICIÓN DEL PROGRAMA ASM
# ==============================================================================
# Aquí se define la lógica del programa 'sum'.
# El uso de 'sp', 'ra', 'p0', etc., es resuelto automáticamente por .encode()
# ==============================================================================

program_asm = [
    # __init__: Configuración inicial y llamada a función
    Instruction(op="movi", rd="r1", imm=4),           # PC 0
    Instruction(op="movi", rd="p0", imm=7),           # PC 4
    Instruction(op="add",  rd="p1", rn="p0", rm="r1"), # PC 8
    Instruction(op="call", imm=8),                    # PC 12 -> Salto a PC 20 (sum)
    Instruction(op="mul",  rd="r1", rn="p0", rm="r1"), # PC 16

    # sum: Rutina que calcula (a*2)+b gestionando el Stack
    Instruction(op="addi", rd="sp", rn="sp", imm=8),  # PC 20: Abrir marco de pila
    Instruction(op="stw",  rd="ra", rn="sp", imm=0),  # PC 24: Guardar Retorno
    Instruction(op="stw",  rd="r1", rn="sp", imm=4),  # PC 28: Guardar Temporal
    
    Instruction(op="li",   rd="r1", imm=2),           # PC 32: Cargar multiplicador
    Instruction(op="mul",  rd="r1", rn="p0", rm="r1"), # PC 36: a * 2
    Instruction(op="add",  rd="p0", rn="r1", rm="p1"), # PC 40: (a*2) + b
    
    Instruction(op="ldw",  rd="r1", rn="sp", imm=4),  # PC 44: Restaurar Temporal
    Instruction(op="ldw",  rd="ra", rn="sp", imm=0),  # PC 48: Restaurar Retorno
    Instruction(op="addi", rd="sp", rn="sp", imm=-8), # PC 52: Cerrar marco de pila
    Instruction(op="ret")                             # PC 56: Volver a __init__
]

# ==============================================================================
# 2. CODIFICACIÓN Y EJECUCIÓN DE LA ESCRITURA
# ==============================================================================

try:
    # PASO A: Codificar cada objeto Instruction a una cadena binaria de 32 bits
    # Esto dispara internamente el mapeo de registros GPR y Secure.
    encoded_instructions = [inst.encode() for inst in program_asm]

    # PASO B: Persistencia de archivos
    # Se generan archivos compatibles con simuladores (hex) y hardware (bin).
    F32IS_Writer.save_bin("sum_program.bin", encoded_instructions)
    F32IS_Writer.save_hex("sum_program.hex", encoded_instructions)

    # PASO C: Reporte de depuración en consola
    print(f"\n{'#'*10} REPORTE FINAL DE ENSAMBLADO {'#'*10}")
    print(f"{'ADDR':<6} | {'CONTENIDO HEX':<13} | {'OP'}")
    print("-" * 35)
    for i, bin_str in enumerate(encoded_instructions):
        print(f"PC {i*4:02d} | Hex: {int(bin_str, 2):08X} | {program_asm[i].op}")

except Exception as e:
    print(f" Error crítico en el proceso: {e}")

# ==============================================================================
# NOTA: Para instrucciones seguras, use el prefijo '@' en 'op' (ej: "@mul").
# El motor activará automáticamente el bit de seguridad y usará el banco Secure.
# ==============================================================================

# --- Definición del Programa con Sesión Segura ---
program_asm = [
    Instruction(op="addi", rd="r1", rn="r0", imm=4),    # PC 00
    Instruction(op="login", imm=0xBEEF0),               # PC 04
    Instruction(op="li", rd="r2", imm=100),             # PC 08
    Instruction(op="@mul", rd="r3", rn="r1", rm="r2"),  # PC 12
    Instruction(op="send", rd="ax", rn="r0"),           # PC 16
    Instruction(op="send", rd="bx", rn="r3"),           # PC 20
    
    # AQUÍ ESTABA EL ERROR: Cambiamos cx="cx" por rd="cx"
    Instruction(op="paddi", rd="cx", rn="ax", imm=1),   # PC 24
    
    Instruction(op="@psub", rd="dx", rn="bx", rm="cx"), # PC 28
    Instruction(op="quit"),                             # PC 32
    Instruction(op="recv", rd="dx", rn="r4")            # PC 36
]

# --- Proceso de Codificación y Escritura ---
try:
    # PASO A: Codificar cada objeto Instruction a una cadena binaria de 32 bits
    # Se encarga de manejar el bit P (@), los opcodes de login/quit y el banco SECURE.
    encoded_instructions = [inst.encode() for inst in program_asm]

    # PASO B: Persistencia de archivos
    # Generamos la salida para el simulador y el binario para el hardware real.
    F32IS_Writer.save_bin("secure_session.bin", encoded_instructions)
    F32IS_Writer.save_hex("secure_session.hex", encoded_instructions)

    # PASO C: Reporte de depuración en consola
    # Este reporte ayuda a verificar que los saltos de PC (de 4 en 4) y los HEX sean correctos.
    print(f"\n{'#'*15} F32IS SECURE SESSION REPORT {'#'*15}")
    print(f"{'PC ADDR':<8} | {'HEX CONTENT':<13} | {'ASM MNEMONIC'}")
    print("-" * 45)
    
    for i, bin_str in enumerate(encoded_instructions):
        hex_val = f"{int(bin_str, 2):08X}"
        # Mostramos la operación original del objeto para comparar
        original_op = program_asm[i].op 
        print(f"0x{i*4:02X}     | {hex_val}    | {original_op}")

    print(f"\n{'#'*18} ASSEMBLY COMPLETE {'#'*18}")

except Exception as e:
    # Captura errores de registros mal escritos o inmediatos fuera de rango
    print(f" Critical error during assembly: {e}")