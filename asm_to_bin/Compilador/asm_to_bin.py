from dataclasses import dataclass
from typing import Optional, List
import struct
@dataclass
class Instruction:
    """
    Represents a decoded or to-be-encoded F32IS instruction.

    This class manages the internal components of the F32IS ISA, including 
    the mapping of mnemonics to physical register addresses (5-bit GPR or 3-bit Secure)
    and the handling of functional units for secure arithmetic extensions.

    Attributes:
        op (str): Mnemonic of the operation (e.g., 'add', '@mul', 'pslladd').
        rd (Optional[int]): Destination register address. Maps to GPR 'rd' (5-bit) 
            or Secure 'sd' (3-bit).
        rn (Optional[int]): First source register address. Maps to GPR 'rn' (5-bit) 
            or Secure 'sn' (3-bit).
        rm (Optional[int]): Second source register address. Maps to GPR 'rm' (5-bit) 
            or Secure 'sm' (3-bit).
        sf (Optional[int]): Fourth register address (3-bit), specifically used 
            as the second accumulator/operand in PR-type secure operations.
        imm (Optional[int]): A 16-bit immediate value or branch offset.
        op1 (Optional[int]): Primary functional unit code (func4). Defines the 
            main ALU operation.
        op2 (Optional[int]): Secondary functional unit code (func3). Defines the 
            arithmetic extension (e.g., secondary addition or XOR in PR-type).
        is_secure (bool): Status of the 'P' (Protection) bit. If True, indicates 
            conditional execution based on an active secure session.
    """
    op: str
    rd: Optional[int] = None
    rn: Optional[int] = None
    rm: Optional[int] = None
    sf: Optional[int] = None
    imm: Optional[int] = None
    op1: Optional[int] = None
    op2: Optional[int] = None
    is_secure: bool = False


    def _resolve_regs(self):
        """
        Translates register aliases to physical addresses (0-31 or 0-7).
        Must be executed prior to encode().
        """

        # 1. Base ISA Definitions for Secure Arithmetic Extensions
        # These are combined to identify PR (Physical-Register) type instructions
        primarias = ["sll", "srl", "add", "sub", "mul", "div", "mod", "and", "orr", "xor", "seq"]
        secundarias = ["add", "xor"]

        # Generate PR combinations (e.g., pslladd, pxorxor)
        combos_pr = [f"p{p}{s}" for p in primarias for s in secundarias]

        # 2. Definition of Secure Operations (PI, V, T, and simple PR types)
        # Includes immediate operations, vault memory access, and transfer instructions
        otras_seguras = [
            "padd", "psub", "pmul", "pdiv", "pmod", "pand", "porr", "pxor", "pseq", "pmov",
            "paddi", "psubi", "pmuli", "pdivi", "pmodi", "pandi", "porri", "pxori", "pseqi", "pmovi",
            "send", "recv", "ldvw", "ldvh", "ldvb", "stvw", "stvh", "stvb"
        ]

        # Final aggregate set of instructions that utilize the Secure Register Bank
        secure_ops = list(set(combos_pr + otras_seguras))

        # Check if the current operation (ignoring the '@' prefix) belongs to the secure set
        is_secure_instr = self.op.strip("@") in secure_ops

        op_clean = self.op.strip("@")

        # --- Resolve Destination Register (rd) ---
        if self.rd is not None and isinstance(self.rd, str):
            # Es Seguro si la instrucción es segura, EXCEPTO en 'recv'
            # (En 'recv rd, sm', el destino 'rd' es el Banco General)
            is_rd_secure = is_secure_instr and op_clean != "recv"
            self.rd = F32IS_Encoder.get_reg_addr(self.rd, is_rd_secure)

        # --- Resolve First Source Register (rn) ---
        if self.rn is not None and isinstance(self.rn, str):
            # Es Seguro si la instrucción es segura, EXCEPTO en 'send'
            # (En 'send sd, rn', el origen 'rn' es el Banco General)
            is_rn_secure = is_secure_instr and op_clean != "send"
            self.rn = F32IS_Encoder.get_reg_addr(self.rn, is_rn_secure)

        # --- Resolve Second Source (rm) and Fourth Field (sf) ---
        # These fields are exclusive to PR-type (Secure-to-Secure) instructions.
        # They always resolve to the Secure Bank addresses (0-7).
        if self.rm is not None and isinstance(self.rm, str):
            self.rm = F32IS_Encoder.get_reg_addr(self.rm, is_secure_instr)
        
        if self.sf is not None and isinstance(self.sf, str):
            self.sf = F32IS_Encoder.get_reg_addr(self.sf, is_secure_instr)


    def encode(self) -> str:
        """
        Main entry point for 32-bit binary encoding.
        
        This method handles:
        1. Security prefix detection ('@') to set the 'is_secure' (P) bit.
        2. Register resolution via _resolve_regs() for both GPR and Secure banks.
        3. Dispatching to specific encoding methods based on the F32IS ISA categories.
        """

        # 1. Security bit detection and mnemonic cleaning
        # If the operation starts with '@', it is marked as a protected instruction (P=1)
        if self.op.startswith("@"):
            self.is_secure = True
            self.op = self.op[1:] 

        # 2. Register Resolution
        # Translates names like 'ax' or 'r1' into physical addresses before encoding
        self._resolve_regs()

        # --- Integer Extensions (Standard I-Extension) ---
        tipo_r = ["add", "sub", "mul", "div", "mod", "and", "orr", "xor", "sll", "srl", "mov", "seq", "ret", "nop"]
        tipo_i = ["addi", "subi", "muli", "divi", "modi", "andi", "orri", "xori", "slli", "srli", "movi", "seqi", "li", "la"]
        tipo_m = ["ldw", "ldh", "ldb", "stw", "sth", "stb"]
        tipo_b = ["beq", "bne", "bgt", "blt", "bge", "ble", "beqz"]
        tipo_j = ["jal", "jmp"]
        tipo_f = ["call"]

        # --- Security Extensions (S-Extension) ---
        # Type PR: Secure arithmetic operations (Register-Register)
        tipo_pr = [
            "padd", "psub", "pmul", "pdiv", "pmod", "pand", "porr", "pxor", "pseq", "pmov",
            "paddadd", "pxorxor", "pslladd", "psrladd"
        ]

        # Type PI: Secure immediate operations (Register-Immediate)
        tipo_pi = [
            "paddi", "psubi", "pmuli", "pdivi", "pmodi", "pandi", "porri", "pxori", "pseqi", "pmovi",
            "pla", "pli"
        ]
        
        # Type V: Vault memory operations (Secure Load/Store)
        tipo_v = ["ldvw", "ldvh", "ldvb", "stvw", "stvh", "stvb"]
        
        # Type T: Transfer operations between GPR and Secure banks
        tipo_t = ["send", "recv"]
        
        # Type SYS: System/Security control instructions
        tipo_sys = ["login", "quit"]

        # 3. Type-based Dispatching
        # Routes the instruction to the appropriate binary formatting method
        if self.op in tipo_r: return F32IS_Encoder.encode_r(self)
        if self.op in tipo_i: return F32IS_Encoder.encode_i(self)
        if self.op in tipo_m: return F32IS_Encoder.encode_m(self)
        if self.op in tipo_b: return F32IS_Encoder.encode_b(self)
        if self.op in tipo_j: return F32IS_Encoder.encode_j(self)
        if self.op in tipo_f: return F32IS_Encoder.encode_f(self)
        if self.op in tipo_pr: return F32IS_Encoder.encode_pr(self)
        if self.op in tipo_pi: return F32IS_Encoder.encode_pi(self)
        if self.op in tipo_v: return F32IS_Encoder.encode_v(self)
        if self.op in tipo_t: return F32IS_Encoder.encode_t(self)
        if self.op in tipo_sys: return F32IS_Encoder.encode_s(self)

        # Fallback for unrecognized operations
        return "0" * 32

    def _to_bin(self, value: int, bits: int) -> str:
        """
        Converts an integer to a binary string with a specified bit-width.
        
        This helper handles:
        1. Two's Complement: Automatically calculates the representation for 
           negative immediate values (e.g., branch offsets or subi).
        2. Masking: Ensures the value is truncated to the 'bits' length using 
           a bitwise AND, preventing overflow into adjacent instruction fields.
        3. Padding: Guarantees the output string is exactly 'bits' long by 
           prepending leading zeros.

        Args:
            value (int): The integer value to convert (register index or immediate).
            bits (int): The target width of the field (e.g., 3, 5, or 16 bits).

        Returns:
            str: A bit-string of length 'bits'.
        """
        # Manual Two's Complement adjustment for negative integers
        if value < 0: 
            value = (1 << bits) + value
            
        # Apply mask to keep only the required number of bits and format as binary
        mask = (1 << bits) - 1
        return format(value & mask, f'0{bits}b')
    


class F32IS_Encoder:
    """
    Encoder constants and mapping for the F32IS Architecture.
    
    This class defines the operational codes (Opcodes), ALU function 
    specifiers (FUNC4), and register file mappings required to 
    translate assembly instructions into machine code.
    """

    # Primary Operation Codes (5 bits)
    # These codes identify the instruction format (R, I, M, B, J, T, S)
    # used by the Control Unit to route signals.
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
        "beq":   0b01000, "jal":  0b01001, "jmp": 0b01001,
        "send":  0b10000, "recv": 0b10000,
        "login": 0b10001, "quit": 0b10001,
        "nop": 0b00000, "call": 0b01001, "ret": 0b00000,
    }

    # ALU Function Specifiers (4 bits)
    # Mapped to the 'func4' field (bits 9-6). Used by the ALU to 
    # execute the specific arithmetic or logic operation.
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
        "nop": 0b0010,
        "mov": 0b0010, 
        "ret": 0b0010,
    }

    # Secondary Arithmetic Specifiers (3 bits)
    # Mapped to 'func3' (bits 24-22). Specifically used for PR-Type 
    # compound operations (e.g., pslladd where 'add' is the secondary func).
    FUNC3_SECURE = {
        "add": 0b000,
        "xor": 0b001,
    }

    # General Purpose Register (GPR) Map (5 bits - 32 Registers)
    # Standard register file accessible by non-protected instructions.
    GPR_MAP = {
        # Control & Linkage
        "zero": 0, "ra": 1, "sp": 2, "pc": 3, "lr": 4,
        # Argument/Parameter Passing
        "p0": 5, "p1": 6, "p2": 7, "p3": 8, "p4": 9, "p5": 10, "p6": 11, "p7": 12, "p8": 13,
        # General Purpose r0-r15
        "r0": 14, "r1": 15, "r2": 16, "r3": 17, "r4": 18, "r5": 19, "r6": 20, "r7": 21,
        "r8": 22, "r9": 23, "r10": 24, "r11": 25, "r12": 26, "r13": 27, "r14": 28, "r15": 29,
        # Constants
        "delta": 30, "max": 31
    }

    # Secure Register Bank Map (3 bits - 8 Registers)
    # Protected register file (ax-hx) used by the Secure Arithmetic Extension (S).
    SECURE_MAP = {
        "ax": 0, "bx": 1, "cx": 2, "dx": 3,
        "ex": 4, "fx": 5, "gx": 6, "hx": 7
    }

    @staticmethod
    def get_reg_addr(name: str, is_secure_field: bool = False) -> int:
        """
        Translates a register mnemonic into its physical binary address.

        This method enforces the architectural boundary between the General Purpose 
        Register (GPR) bank and the Secure Register Bank.

        Args:
            name (str): The mnemonic name of the register (e.g., 'r1', 'sp', 'ax').
            is_secure_field (bool): Flag indicating if the instruction expects 
                a 3-bit secure register (PR, PI, V, T types).

        Returns:
            int: The physical address (0-31 for GPR, 0-7 for Secure).

        Raises:
            ValueError: If a register from the wrong bank is used for the 
                specified instruction type.
        """
        name = name.lower().strip()
        
        if is_secure_field:
            # Context: Searching within the 3-bit Secure Bank (ax through hx)
            if name in F32IS_Encoder.SECURE_MAP:
                return F32IS_Encoder.SECURE_MAP[name]
            
            raise ValueError(f"Critical Error: Secure register '{name}' not found in 3-bit bank. "
                             "Ensure you are using ax-hx for secure instructions.")
        else:
            # Context: Searching within the 5-bit GPR Bank (zero through max)
            if name in F32IS_Encoder.GPR_MAP:
                return F32IS_Encoder.GPR_MAP[name]
            
            raise ValueError(f"Critical Error: General register '{name}' not found in 5-bit bank. "
                             "Check if you accidentally used a secure register (ax-hx) in a non-secure instruction.")

    @staticmethod
    def encode_r(inst: Instruction) -> str:
        """
        Encodes Type-R instructions (Register-to-Register).
        
        Hardware Map (32 bits):
        [func7: 31-25] [rm: 24-20] [rn: 19-15] [rd: 14-10] [func4: 9-6] [opcode: 5-1] [P: 0]

        Args:
            inst (Instruction): The instruction object containing resolved GPR addresses.
            
        Returns:
            str: 32-bit binary string.
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        # Core fields mapping
        # Opcode identifies R-type, Func4 identifies the specific ALU operation
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0), '04b')
        
        # Register addresses (GPR Bank - 5 bits each)
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        rm = format(inst.rm or 0, '05b')
        
        # Extension field (MSB padding)
        func7 = "0000000" 
        
        # Concatenation from MSB (left) to LSB (right)
        return func7 + rm + rn + rd + func4 + opcode + p

    @staticmethod
    def encode_i(inst: Instruction) -> str:
        """
        Encodes Type-I instructions (Register-Immediate arithmetic/logic).
        
        Hardware Map (32 bits):
        [imm: 31-20] [rn: 19-15] [rd: 14-10] [func4: 9-6] [opcode: 5-1] [P: 0]

        Args:
            inst (Instruction): Instruction object with resolved GPRs and 12-bit immediate.
            
        Returns:
            str: 32-bit binary string.
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        # Opcode identifies I-type (usually 0b00001), Func4 identifies ALU operation
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b00001), '05b')
        func4 = format(F32IS_Encoder.FUNC4_ALU.get(inst.op, 0b0010), '04b')
        
        # Register addresses (GPR Bank - 5 bits each)
        # rd: Destination register, rn: Source register
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # Immediate value: Truncated to 12 bits for standard I-type format.
        # This uses the lower 12 bits of the integer provided.
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b') 
    
        # Concatenation from MSB (left) to LSB (right)
        # Structure: [imm12] [rn] [rd] [func4] [opcode] [p]
        return imm12 + rn + rd + func4 + opcode + p
    
    @staticmethod
    def encode_m(inst: Instruction) -> str:
        """
        Encodes Type-M instructions (Memory Load/Store).
        
        Hardware Map (32 bits):
        [imm12: 31-20] [rn: 19-15] [rd: 14-10] [W: 9] [H: 8] [B: 7] [S: 6] [opcode: 5-1] [P: 0]
        
        Logic:
        - imm12: 12-bit value. Calculated independently of the S bit using a 0xFFF mask.
        - S bit: Operational control flag. Its value does NOT affect the immediate calculation.
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        # Opcode: ld -> 0b00100, st -> 0b00101
        op_type = inst.op[:2] 
        opcode_val = 0b00100 if op_type == "ld" else 0b00101
        opcode = format(opcode_val, '05b')
        
        # Size flags (Word, Half, Byte)
        w = "1" if "w" in inst.op else "0"
        h = "1" if "h" in inst.op else "0"
        b = "1" if "b" in inst.op else "0"
        
        # S-Bit: Operational control flag. 
        # Independent of the immediate's sign or value.
        s = "1" if getattr(inst, 's_flag', False) else "0"
        
        # Register addresses (5-bit GPR bank)
        rd = format(inst.rd or 0, '05b')
        rn = format(inst.rn or 0, '05b')
        
        # 12-bit Immediate: Calculated via bitwise mask.
        # This ensures that even if the S bit is 1, the immediate remains 
        # purely the 12-bit representation of the offset.
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b')
        
        # Concatenation from MSB (left) to LSB (right)
        # [31:20] + [19:15] + [14:10] + [9] + [8] + [7] + [6] + [5:1] + [0]
        return imm12 + rn + rd + w + h + b + s + opcode + p


    @staticmethod
    def encode_b(inst: Instruction) -> str:
        """
        Encodes Type-B instructions (Conditional Branches).
        
        Hardware Map (32 bits):
        [imm12: 31-20] [rs1: 19-15] [rd: 14-10] [func4: 9-6] [opcode: 5-1] [P: 0]
        
        Jump Condition Specification (func4):
        0000: BEQ (==) | 0001: BNE (!=) | 0010: BGT (>)
        0011: BLT (<)  | 0100: BGE (>=) | 0101: BLE (<=)
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        # Opcode identifies B-type (standardly 0b01000)
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b01000), '05b')
        
        # Mapping for func4 based on the jump condition table provided
        condiciones = {
            "beq": 0b0000, "bne": 0b0001, "bgt": 0b0010,
            "blt": 0b0011, "bge": 0b0100, "ble": 0b0101,
            "beqz": 0b0000,
        }
        
        # Get the specific condition bits or default to 0000
        func4_val = condiciones.get(inst.op.lower(), 0b0000)
        func4 = format(func4_val, '04b')
        
        # Register Addresses (5-bit GPR bank)
        # rs1 (rn) and rd (rs2) are compared according to the func4 logic
        rs1 = format(inst.rn or 0, '05b')
        rs2 = format(inst.rm or 0, '05b')
        
        # 12-bit PC-relative offset in Two's Complement
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b')
        # Divisiones solicitadas:
        # imm11_5: Los 7 bits superiores (del bit 11 al 5)
        imm11_5 = format((imm_val >> 5) & 0x7F, '07b')

        # imm4_0: Los 5 bits inferiores (del bit 4 al 0)
        imm4_0 = format(imm_val & 0x1F, '05b')
        
        # Concatenation from MSB (left) to LSB (right)
        return imm11_5 + rs2 + rs1 + imm4_0 + func4 + opcode + p
    

    @staticmethod
    def encode_j(inst: Instruction) -> str:
        """
        Encodes Type-J instructions (Jump and Link).
        
        Hardware Map (32 bits):
        [imm 20:4 (17 bits)] [rd: 14-10] [imm 3:0 (4 bits)] [opcode: 5-1] [P: 0]
        
        Field Description:
        - imm 20:4: Upper bits of the 21-bit PC-relative offset.
        - rd: Target link register (5-bit GPR).
        - imm 3:0: Lower bits of the 21-bit PC-relative offset.
        - opcode: Instruction identifier (e.g., jal/jmp -> 0b01001).
        - P: Security bit (LSB).
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        # Opcode Retrieval: Fetches from the OPCODES dictionary for consistency.
        # Defaults to 01001 if the instruction belongs to the J-family.
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b01001)
        opcode = format(opcode_val, '05b')
        
        # Destination Register (5-bit GPR bank)
        rd = format(inst.rd or 0, '05b')
        
        # 21-bit Immediate Segmentation:
        # Masking ensures the offset stays within the 21-bit hardware limit.
        imm_val = (inst.imm or 0) & 0x1FFFFF
        
        # Split logic according to F32IS J-Type specification
        imm_3_0 = format(imm_val & 0xF, '04b')           # LSBs
        imm_20_4 = format((imm_val >> 4) & 0x1FFFF, '017b') # MSBs
        
        # Concatenation from MSB (left) to LSB (right)
        return imm_20_4 + rd + imm_3_0 + opcode + p

    @staticmethod
    def encode_f(inst: Instruction) -> str:
        # Bit de seguridad (P) en el bit 0
        p = "1" if inst.is_secure else "0"
        
        # Según la tabla: jal/call = 01001 (decimal 9)
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 9) 
        opcode = format(opcode_val, '05b')
        
        # Registro de destino (rd): ra=1 para call, zero=0 para jmp
        rd_val = inst.rd if inst.rd is not None else 1
        rd = format(rd_val, '05b')
        
        # Inmediato de 21 bits (imm21)
        # El valor representa la distancia de salto (imm = destino - actual)
        imm_val = (inst.imm or 0) & 0x1FFFFF
        
        # Segmentación según el mapa de bits J/F
        imm_3_0 = format(imm_val & 0xF, '04b')           # Bits 9-6
        imm_20_4 = format((imm_val >> 4) & 0x1FFFF, '017b') # Bits 31-15
        
        # Retorna la cadena de 32 bits concatenada
        return imm_20_4 + rd + imm_3_0 + opcode + p
    
    @staticmethod
    def encode_pr(inst: Instruction) -> str:
        """
        Encodes Type-PR instructions (Secure Register-to-Register Compound).
        
        Hardware Map (32 bits):
        [func7: 31-25] [func3: 24-22] [sf: 21-19] [sm: 18-16] [sn: 15-13] [sd: 12-10] [func4: 9-6] [opcode: 5-1] [P: 0]
        
        Field Description:
        - func7: Extension/Padding field.
        - func3: Secondary ALU operation (mapped from inst.op2).
        - sf, sm, sn, sd: 3-bit registers from the Secure Bank (ax-hx).
        - func4: Primary ALU operation (mapped from inst.op1).
        - opcode: Secure PR identifier (typically 0b00010).
        - P: Security bit (forced to 1 for this format).
        """
        # Security bit: Always 1 for Secure Bank instructions
        p = "1" 
        
        # Opcode Retrieval: Fetches from OPCODES table.
        # Standard for PR-type is 0b00010.
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b00010)
        opcode = format(opcode_val, '05b')
        
        # Dual-ALU Operation Mapping:
        # op1 (Primary) maps to the 4-bit func4 field.
        # op2 (Secondary) maps to the 3-bit func3 field.
        f4_val = F32IS_Encoder.FUNC4_ALU.get(inst.op1, 0b0010)
        f3_val = F32IS_Encoder.FUNC3_SECURE.get(inst.op2, 0b000)
        
        func4 = format(f4_val, '04b')
        func3 = format(f3_val, '03b')
        
        # Secure Bank Registers (3 bits each: 0-7 for ax-hx)
        # These must have been resolved by _resolve_regs(is_secure=True)
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        sm = format(inst.rm or 0, '03b')
        sf = format(inst.sf or 0, '03b')
        
        # Padding/Extension field
        func7 = "0000000"
        
        # Concatenation from MSB (left) to LSB (right)
        # [func7][func3][sf][sm][sn][sd][func4][opcode][p]
        return func7 + func3 + sf + sm + sn + sd + func4 + opcode + p

    @staticmethod
    def encode_pi(inst: Instruction) -> str:
        """
        Encodes Type-PI instructions (Secure Register-Immediate).
        
        Hardware Map (32 bits):
        [imm16: 31-16] [sn: 15-13] [sd: 12-10] [func4: 9-6] [opcode: 5-1] [P: 0]
        
        Field Description:
        - imm16: 16-bit immediate value (supports Two's Complement via 0xFFFF mask).
        - sn: Source register from Secure Bank (3-bit, ax-hx).
        - sd: Destination register from Secure Bank (3-bit, ax-hx).
        - func4: Primary ALU operation (mapped from inst.op1).
        - opcode: Secure PI identifier (typically 0b00011).
        - P: Security bit (forced to 1).
        """
        # Security bit: Always 1 for Secure Bank/Instruction operations
        p = "1"
        
        # Opcode Retrieval: Fetches from OPCODES table.
        # Standard for PI-type is 0b00011.
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b00011)
        opcode = format(opcode_val, '05b')
        
        # Operation Mapping:
        # Uses op1 to define the 4-bit func4 field.
        f4_val = F32IS_Encoder.FUNC4_ALU.get(inst.op1, 0b0010)
        func4 = format(f4_val, '04b')
        
        # Secure Bank Registers (3 bits: 0-7 for ax-hx)
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        
        # 16-bit Immediate:
        # Occupies the upper half of the instruction (bits 31 to 16).
        # Masking with 0xFFFF handles signed/unsigned values correctly.
        imm_val = inst.imm or 0
        imm16 = format(imm_val & 0xFFFF, '016b')
        
        # Concatenation from MSB (left) to LSB (right)
        # [imm16][sn][sd][func4][opcode][p]
        return imm16 + sn + sd + func4 + opcode + p
    

    @staticmethod
    def encode_t(inst: Instruction) -> str:
        """
        Encodes Type-T instructions (Secure Bus Transport).
        
        Hardware Map (32 bits):
        DESGLOSE POR INSTRUCCIÓN:

        
        Field Description:
        - func14: Bus control padding or extensions (currently zeros).
        - rn: General Purpose Register (5-bit, r0-r31).
        - sd: Secure Bank Register (3-bit, ax-hx).
        - func4: Transport direction (send: 0000 | recv: 0001).
        - opcode: Transport identifier (standardly 0b10000).
        - P: Security bit (forced to 1 to enable secure bus).
        """
        # Security bit: Forced to 1 to authorize cross-bank movement
        p = "1" 
        
        # Opcode Retrieval: Fetches 'send'/'recv' from the architecture table.
        # Typically maps to 0b10000.
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b10000)
        opcode = format(opcode_val, '05b')

        sd = "000"      #rd send
        rd = "0000"     #rd recv
        rn = "0000"     #rn send
        sm = "000"      #rn recv
        
        # Transport Logic & Register Assignment:
        # 'send': GPR (rn) -> Secure (sd)
        # 'recv': Secure (sd) -> GPR (rn)
        if inst.op == "send":
            func4 = "0000"
            sd_bin = format(inst.rd, '03b') 
            rn_bin = format(inst.rn, '05b')
            func12 = "0" * 12

            return func12 + rn_bin + "00" + sd_bin + func4 + opcode + p

        else: # recv
            func4 = "0001"
            rd_bin = format(inst.rd, '05b') # Destination: GPR 
            sm_bin = format(inst.rn, '03b') # Source: Secure Register
            func13 = "0" * 13

            return func13 + sm_bin + "0" + rd_bin + func4 + opcode + p

    
    @staticmethod
    def encode_s(inst: Instruction) -> str:
        """
        Encodes Type-S instructions (Login/Quit).
        Hardware Map: imm21(31:11) | bit10(0) | func4(9:6) | opcode(5:1) | P(0)
        
        Lógica:
        - login: func4 = 0000. R[lr] <- (imm == KEY)
        - quit:  func4 = 0001. R[lr] <- 0
        """
        # P es 0 para estas instrucciones de control de acceso
        p = "0" 
        
        # Opcode para S (10001)
        opcode = format(F32IS_Encoder.OPCODES.get(inst.op, 0b10001), '05b')
        
        # func4 (9:6): 0000 para login, 0001 para quit
        func4 = "0000" if inst.op == "login" else "0001"
        
        
        # Inmediato de 21 bits (31:11)
        # En 'login', imm es la llave. En 'quit', suele ser 0.
        imm_val = inst.imm or 0
        imm20 = format(imm_val & 0x1FFFFF, '020b')
        
        # Retorno de MSB (izquierda) a LSB (derecha)
        # [31:12] + [00] + [9:6] + [5:1] + [0]
        return imm20 + "00" + func4 + opcode + p


    @staticmethod
    def encode_v(inst: Instruction) -> str:
        """
        Encodes Type-V instructions (Vault / Memory Access).
        
        Hardware Map (32 bits):
        [imm16: 31-16] [sn: 15-13] [sd: 12-10] [W: 9] [H: 8] [B: 7] [S: 6] [opcode: 5-1] [P: 0]
        
        Field Description:
        - imm16: 16-bit immediate (Offset/Address).
        - sn: Source/Base register (3-bit Secure Bank).
        - sd: Destination register (3-bit Secure Bank).
        - W, H, B: Width selectors (Word, Half-word, Byte).
        - S: Operation selection (0: Sum/Add, 1: Sub/Subtract).
        - opcode: Instruction identifier (fetched from OPCODES).
        - P: Security bit (LSB).
        """
        # Security bit
        p = "1" if inst.is_secure else "0"
        
        # Opcode Retrieval
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b00110) # Default Vault opcode
        opcode = format(opcode_val, '05b')
        
        # S (Bit 6): Operación (Suma/Resta para el cálculo de dirección)
        # Se asume que inst.sub_op o similar define si es suma o resta
        s_bit = "1" if getattr(inst, 'use_sub', False) else "0"
        
        # B, H, W (Bits 7, 8, 9): Selección de ancho de datos
        # Estos bits son excluyentes según el tipo de instrucción (ldb, ldh, ldw, etc.)
        b_bit = "1" if "b" in inst.op.lower() else "0"
        h_bit = "1" if "h" in inst.op.lower() else "0"
        w_bit = "1" if "w" in inst.op.lower() else "0"
        
        # Registros del Banco Seguro (3 bits: ax-hx)
        sd = format(inst.rd or 0, '03b')
        sn = format(inst.rn or 0, '03b')
        
        # Inmediato de 16 bits (PC-relative o Absolute Offset)
        imm_val = inst.imm or 0
        imm16 = format(imm_val & 0xFFFF, '016b')
        
        # Concatenación final (MSB -> LSB)
        # [imm16][sn][sd][W][H][B][S][opcode][P]
        return imm16 + sn + sd + w_bit + h_bit + b_bit + s_bit + opcode
    
class F32IS_Writer:
    """
    Handles output generation. 
    Now aligned with ISA: P-bit is Bit 0 (LSB).
    """

    @staticmethod
    def to_bytes(binary_str: str):
        """
        Converts 32-bit string [MSB...P] to 4 bytes.
        P (bit 0) will be in the first byte (Little Endian).
        """
        value = int(binary_str, 2)
        # '<I' asegura que el LSB (donde está P) sea el primer byte del archivo
        return struct.pack('<I', value)

    @staticmethod
    def save_bin(filename: str, instructions: list):
        try:
            with open(filename, 'wb') as f:
                for inst in instructions:
                    f.write(F32IS_Writer.to_bytes(inst))
            print(f" Binary file (P-bit as LSB) saved: {filename}")
        except Exception as e:
            print(f" Error: {e}")

    @staticmethod
    def save_hex(filename: str, instructions: list):
        """
        Generates .hex for Verilog. 
        Example: If P=1 and opcode=00001 (Type I), 
        the last hex digit will be odd.
        """
        try:
            with open(filename, 'w') as f:
                for inst in instructions:
                    value = int(inst, 2)
                    f.write(f"{value:08X}\n")
            print(f" Hex file (P-bit as LSB) saved: {filename}")
        except Exception as e:
            print(f" Error: {e}")


####################################################


# --- PRUEBA DE INSTRUCCIÓN CON @ (Bit P Dinámico) ---
print(f"\n{'-'*20} PRUEBA PREFIJO @ {'-'*20}")

# Caso con @: Activa el bit P de seguridad
# r3=17, r1=15, r2=16
inst_at = Instruction(op="@mul", rd="r3", rn="r1", rm="r2")
bin_at = inst_at.encode() # encode() llama automáticamente a _resolve_regs()

print(f"Instrucción original: @mul r3, r1, r2")
print(f"Binario generado:     {bin_at}")
print(f"Bit P (seguridad):    {bin_at[31]} <--- Debe ser 1")

# Caso sin @: Bit P en 0
inst_no_at = Instruction(op="mul", rd="r3", rn="r1", rm="r2")
bin_no_at = inst_no_at.encode()

print(f"\nInstrucción original: mul r3, r1, r2")
print(f"Binario generado:     {bin_no_at}")
print(f"Bit P (seguridad):    {bin_no_at[31]} <--- Debe ser 0")



# --- Definición del Programa con Sesión Segura ---
program_asm = [
    Instruction(op="addi", rd="r0", rn="r0", imm=0),    # PC 00
    Instruction(op="login", imm=0xBEEF0),               # PC 04
    Instruction(op="li", rd="r2", imm=100),             # PC 08
    Instruction(op="@mul", rd="r3", rn="r1", rm="r2"),  # PC 12
    Instruction(op="send", rd="ax", rn="r0"),           # PC 16
    Instruction(op="send", rd="bx", rn="r3"),           # PC 20
    
    # AQUÍ ESTABA EL ERROR: Cambiamos cx="cx" por rd="cx"
    Instruction(op="paddi", rd="cx", rn="ax", imm=1),   # PC 24
    
    Instruction(op="@psub", rd="dx", rn="bx", rm="cx"), # PC 28
    Instruction(op="quit"),                             # PC 32
    Instruction(op="recv", rd="dx", rn="r4"),           # PC 36
    Instruction(op="nop"),                              # PC 40
    Instruction(op="nop"),                              # PC 44 
    Instruction(op="nop"),                              # PC 48 

    Instruction(
        op="pslladd", 
        rd="ax", 
        rn="bx", 
        rm="cx", 
        sf="dx", 
        op1="sll", 
        op2="add"
    ),

    # 2. PR Compuesta: pxorxor ex, fx, gx, hx
    # op1 (primaria) -> "xor", op2 (secundaria) -> "xor"
    Instruction(
        op="pxorxor", 
        rd="ex", 
        rn="fx", 
        rm="gx", 
        sf="hx", 
        op1="xor", 
        op2="xor"
    ),

    # 3. PR Simple: padd ax, bx, cx
    # Al ser simple, op2 debe mapear a "add" (valor 000) por defecto
    Instruction(
        op="padd", 
        rd="ax", 
        rn="bx", 
        rm="cx", 
        is_secure=True
    ),

    # 4. PI (Inmediato): paddi ax, bx, 500
    # op1 -> "add", op2 no se usa en tipo PI
    Instruction(
        op="paddi", 
        rd="ax", 
        rn="bx", 
        imm=500, 
        op1="add", 
        is_secure=True
    ),
    Instruction(
    op="send",
    rd="ax",   # Mapea a 0 (3-bit)
    rn="r4",   # Mapea a 4 (5-bit) -> Gracias a tu 'not in ["send", "recv"]'
    is_secure=True
    ),
    Instruction(
    op="call",
    rd="ra",        # Mapea a 1
    imm=0x100,      # Inmediato de 21 bits
    is_secure=False
    ),
    Instruction(
    op="ret",
    rd="pc",
    rn="ra",
    is_secure=False
    ),
    Instruction(
    op="mov",
    rd="r0",        # Destino: registro 15 (según el mapeo r0-r15)
    rn="p0",        # Origen: registro 5
    is_secure=False
)

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