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

        # --- Resolve Destination Register (rd) ---
        if self.rd is not None and isinstance(self.rd, str):
            # For PR/PI and send/recv, rd maps to the Secure Bank (sd)
            # This follows the F32IS specification where rd is a 3-bit field for these types
            is_rd_secure = is_secure_instr 
            self.rd = F32IS_Encoder.get_reg_addr(self.rd, is_rd_secure)

        # --- Resolve First Source Register (rn) ---
        if self.rn is not None and isinstance(self.rn, str):
            # Special logic for T-type (Transfer) instructions:
            # 'send' and 'recv' utilize the General Purpose Bank (5 bits) for rn,
            # while standard secure arithmetic uses the Secure Bank (3 bits).
            is_rn_secure = is_secure_instr and self.op.strip("@") not in ["send", "recv"]
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
        if self.op in tipo_v: return F32IS_Encoder.encode_v(self)  # Added Vault dispatch
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
        "nop": 0b0010, # Defaults to ADD with zero for NOP
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
            "blt": 0b0011, "bge": 0b0100, "ble": 0b0101
        }
        
        # Get the specific condition bits or default to 0000
        func4_val = condiciones.get(inst.op.lower(), 0b0000)
        func4 = format(func4_val, '04b')
        
        # Register Addresses (5-bit GPR bank)
        # rs1 (rn) and rd (rs2) are compared according to the func4 logic
        rd = format(inst.rd or 0, '05b')
        rs1 = format(inst.rn or 0, '05b')
        
        # 12-bit PC-relative offset in Two's Complement
        imm_val = inst.imm or 0
        imm12 = format(imm_val & 0xFFF, '012b')
        
        # Concatenation from MSB (left) to LSB (right)
        return imm12 + rs1 + rd + func4 + opcode + p
    

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
        """
        Encodes Type-F instructions (Function Call/Return).
        
        Hardware Map (32 bits):
        [imm 20:4 (17 bits)] [rd: 14-10] [imm 3:0 (4 bits)] [opcode: 5-1] [P: 0]
        
        Field Description:
        - imm 20:4: Upper bits of the 21-bit PC-relative function offset.
        - rd: Link/Return register (5-bit GPR). Defaults to 'ra' (1).
        - imm 3:0: Lower bits of the function offset.
        - opcode: Fetched from OPCODES (e.g., 'call' -> 0b01001 or 0b01010).
        - P: Security bit (LSB).
        """
        # Security bit (LSB)
        p = "1" if inst.is_secure else "0"
        
        opcode_val = F32IS_Encoder.OPCODES.get(inst.op, 0b01010)
        opcode = format(opcode_val, '05b')
        
        # Link Register (5-bit GPR)
        # Standard convention: ra (r1) for calls.
        rd = format(inst.rd or 1, '05b') 
        
        # 21-bit Immediate Segmentation (Two's Complement):
        # The mask 0x1FFFFF correctly captures the sign for backward calls.
        imm_val = (inst.imm or 0) & 0x1FFFFF
        
        # Split according to J/F-type physical layout
        imm_3_0 = format(imm_val & 0xF, '04b')
        imm_20_4 = format((imm_val >> 4) & 0x1FFFF, '017b')
        
        # Concatenation from MSB (left) to LSB (right)
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
        [func14: 31-18] [rn: 17-13] [sd: 12-10] [func4: 9-6] [opcode: 5-1] [P: 0]
        
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
        
        # Transport Logic & Register Assignment:
        # 'send': GPR (rn) -> Secure (sd)
        # 'recv': Secure (sd) -> GPR (rn)
        if inst.op == "send":
            func4 = "0000"
            sd_val = inst.rd # Destination: Secure Register
            rn_val = inst.rn # Source: GPR
        else: # recv
            func4 = "0001"
            rn_val = inst.rd # Destination: GPR
            sd_val = inst.rn # Source: Secure Register

        # Formatting with specific bank widths
        sd = format(sd_val or 0, '03b')  # 3-bit Secure index
        rn = format(rn_val or 0, '05b')  # 5-bit GPR index
        
        # 14-bit Padding/Control
        func14 = "0" * 14
        
        # Concatenation from MSB (left) to LSB (right)
        # [func14][rn][sd][func4][opcode][p]
        return func14 + rn + sd + func4 + opcode + p
    
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
        
        # Bit 10: Padding para completar la estructura
        bit10 = "0"
        
        # Inmediato de 21 bits (31:11)
        # En 'login', imm es la llave. En 'quit', suele ser 0.
        imm_val = inst.imm or 0
        imm21 = format(imm_val & 0x1FFFFF, '021b')
        
        # Retorno de MSB (izquierda) a LSB (derecha)
        # [31:11] + [10] + [9:6] + [5:1] + [0]
        return imm21 + bit10 + func4 + opcode + p
    
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


"""
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
        op1="add", 
        op2="add", 
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