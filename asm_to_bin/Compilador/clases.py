
pseudo_instr = ["call", "beqz", "jmp", "ret", "nop", "seqz"]

instrucciones = {
    # Clase 1 — R y PR (op rd, rn, rm)
    "add": "clase1",   "sub": "clase1",   "mul": "clase1",
    "div": "clase1",   "mod": "clase1",   "and": "clase1",
    "orr": "clase1",   "xor": "clase1",   "sll": "clase1",
    "srl": "clase1",   "seq": "clase1",
    "padd": "clase1",  "psub": "clase1",  "pmul": "clase1",
    "pdiv": "clase1",  "pmod": "clase1",  "pand": "clase1",
    "porr": "clase1",  "pxor": "clase1",  "pseq": "clase1",


    # Clase 2 — I y PI (op rd, rn, imm)
    "addi": "clase2",  "subi": "clase2",  "muli": "clase2",
    "divi": "clase2",  "modi": "clase2",  "andi": "clase2",
    "orri": "clase2",  "xori": "clase2",  "slli": "clase2",
    "srli": "clase2",  "seqi": "clase2",
    "paddi": "clase2", "psubi": "clase2", "pmuli": "clase2",
    "pdivi": "clase2", "pmodi": "clase2", "pandi": "clase2",
    "porri": "clase2", "pxori": "clase2", "pseqi": "clase2",


    # Clase 3 — M y V (op rd, imm(rn))
    "ldw": "clase3",  "ldh": "clase3",  "ldb": "clase3",
    "stw": "clase3",  "sth": "clase3",  "stb": "clase3",
    "ldvw": "clase3", "ldvh": "clase3", "ldvb": "clase3",
    "stvw": "clase3", "stvh": "clase3", "stvb": "clase3",

    # Clase B — (op rn, rm, etiqueta)
    "beq": "claseB",  "bne": "claseB",  "bgt": "claseB",
    "blt": "claseB",  "bge": "claseB",  "ble": "claseB",

    # Clase J — (jal rd, imm)
    "jal": "claseJ",

    # Clase S — (login imm / quit)
    "login": "claseS", "quit": "claseS",

    # Clase T — (op rd, rn)
    "send": "claseT",  "recv": "claseT",

    # Clase E(special) — (op rd, rn, rm, sf)
    "paddadd": "claseE", "pxorxor": "claseE", "pslladd": "claseE", "psrladd": "claseE",

    # Clase Mov
    "mov": "claseMov", "pmov": "claseMov", "movi": "claseMov", "pmovi": "claseMov",

    # Clase L — (li/la rd, imm)
    "li": "claseL", "la": "claseL", "pli": "claseL", "pla": "claseL",
}

registros_normales = {
    "zero", "ra", "sp", "pc", "lr",
    "p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8",
    "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7",
    "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
    "delta", "max"
}

registros_seguros = {"ax", "bx", "cx", "dx", "ex", "fx", "gx", "hx"}
