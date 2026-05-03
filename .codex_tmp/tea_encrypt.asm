; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 624
    call 117    # entrada principal | -> main @ 476
__halt__:    # addr=8
    jmp -1    # -> __halt__ @ 8
tea_encrypt:    # addr=12
    addi sp, sp, 28
    stw ra, +0(sp)
    mov p0, zero
    login 0xBEEF0
    beqz lr, 107    # -> tea_encrypt_secure_exit_1 @ 460
    @stw p0, +24(sp)
    @addi r1, sp, 24
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    @stw r0, +20(sp)
    @addi r1, sp, 24
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    @stw r0, +16(sp)
    pmovi bx, 158
    @stw r0, +12(sp)
    pmovi bx, 0
    @stw r0, +8(sp)
    pmovi bx, 0
    @stw r0, +4(sp)
    @ldw r0, +12(sp)
    @slli r0, r0, 8
    porri bx, bx, 55
    @stw r0, +12(sp)
    @ldw r0, +12(sp)
    @slli r0, r0, 8
    porri bx, bx, 121
    @stw r0, +12(sp)
    @ldw r0, +12(sp)
    @slli r0, r0, 8
    porri bx, bx, 185
    @stw r0, +12(sp)
tea_encrypt_while_cond_2:    # addr=156
    @ldw r0, +4(sp)
    pmovi cx, 32
    @bge r0, r1, 55    # -> tea_encrypt_while_end_3 @ 388
    @ldw r0, +12(sp)
    @ldw r1, +8(sp)
    padd cx, cx, bx
    @stw r1, +8(sp)
    @ldw r1, +16(sp)
    pmovi bx, 4
    pmovi ex, 0
    pmovi fx, 0
    pmuli fx, fx, 4
    padd ex, ex, fx
    ldvw dx, +0(ex)
    pslladd cx, cx, bx, dx
    @ldw r0, +16(sp)
    @ldw r2, +8(sp)
    padd bx, bx, dx
    @ldw r2, +16(sp)
    pmovi ex, 5
    pmovi gx, 0
    pmovi hx, 1
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor cx, cx, bx, dx
    @ldw r0, +20(sp)
    padd bx, bx, cx
    @stw r0, +20(sp)
    @ldw r0, +20(sp)
    pmovi cx, 4
    pmovi ex, 0
    pmovi fx, 2
    pmuli fx, fx, 4
    padd ex, ex, fx
    ldvw dx, +0(ex)
    pslladd bx, bx, cx, dx
    @ldw r1, +20(sp)
    @ldw r2, +8(sp)
    padd cx, cx, dx
    @ldw r2, +20(sp)
    pmovi ex, 5
    pmovi gx, 0
    pmovi hx, 3
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor bx, bx, cx, dx
    @ldw r1, +16(sp)
    padd cx, cx, bx
    @stw r1, +16(sp)
    pmovi cx, 1
    @ldw r0, +4(sp)
    padd bx, bx, cx
    @stw r0, +4(sp)
    @jmp -58    # -> tea_encrypt_while_cond_2 @ 156
tea_encrypt_while_end_3:    # addr=388
    @ldw r0, +20(sp)
    @addi r1, sp, 24
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    @ldw r0, +16(sp)
    @addi r1, sp, 24
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    pmovi bx, 0
    recv p0, bx
    quit
    ldw ra, +0(sp)
    addi sp, sp, -28
    ret
tea_encrypt_secure_exit_1:    # addr=460
    quit
    ldw ra, +0(sp)
    addi sp, sp, -28
    ret
main:    # addr=476
    addi sp, sp, 12
    stw ra, +0(sp)
    li r0, 100
    addi r1, sp, 4
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, +0(r1)
    li r0, 200
    addi r1, sp, 4
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, +0(r1)
    addi r0, sp, 4
    mov p0, r0
    call -133    # -> tea_encrypt @ 12
    mov r0, p0
    addi r1, sp, 4
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, +0(r1)
    la r1, 616
    stw r0, +0(r1)
    addi r1, sp, 4
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, +0(r1)
    la r1, 620
    stw r0, +0(r1)
    ldw ra, +0(sp)
    addi sp, sp, -12
    ret
