; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 464
    call 103    # entrada principal | -> main @ 420
__halt__:    # addr=8
    jmp -1    # -> __halt__ @ 8
tea_encrypt:    # addr=12
    addi sp, sp, 24
    stw ra, +0(sp)
    mov p0, zero
    login 0xBEEF0
    beqz lr, 93    # -> tea_encrypt_secure_exit_1 @ 404
    @stw p0, +20(sp)
    @addi r1, sp, 20
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    @stw r0, +16(sp)
    @addi r1, sp, 20
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    @stw r0, +12(sp)
    pmovi bx, 0
    @stw r0, +8(sp)
    pmovi bx, 0
    @stw r0, +4(sp)
tea_encrypt_for_cond_2:    # addr=100
    @ldw r0, +4(sp)
    pmovi cx, 32
    @bge r0, r1, 55    # -> tea_encrypt_for_end_4 @ 332
    send bx, delta
    @ldw r1, +8(sp)
    padd cx, cx, bx
    @stw r1, +8(sp)
    @ldw r1, +12(sp)
    pmovi bx, 4
    pmovi ex, 0
    pmovi fx, 0
    pmuli fx, fx, 4
    padd ex, ex, fx
    ldvw dx, +0(ex)
    pslladd cx, cx, bx, dx
    @ldw r0, +12(sp)
    @ldw r2, +8(sp)
    padd bx, bx, dx
    @ldw r2, +12(sp)
    pmovi ex, 5
    pmovi gx, 0
    pmovi hx, 1
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor cx, cx, bx, dx
    @ldw r0, +16(sp)
    padd bx, bx, cx
    @stw r0, +16(sp)
    @ldw r0, +16(sp)
    pmovi cx, 4
    pmovi ex, 0
    pmovi fx, 2
    pmuli fx, fx, 4
    padd ex, ex, fx
    ldvw dx, +0(ex)
    pslladd bx, bx, cx, dx
    @ldw r1, +16(sp)
    @ldw r2, +8(sp)
    padd cx, cx, dx
    @ldw r2, +16(sp)
    pmovi ex, 5
    pmovi gx, 0
    pmovi hx, 3
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor bx, bx, cx, dx
    @ldw r1, +12(sp)
    padd cx, cx, bx
    @stw r1, +12(sp)
tea_encrypt_for_update_3:    # addr=312
    pmovi cx, 1
    @ldw r0, +4(sp)
    padd bx, bx, cx
    @stw r0, +4(sp)
    @jmp -58    # -> tea_encrypt_for_cond_2 @ 100
tea_encrypt_for_end_4:    # addr=332
    @ldw r0, +16(sp)
    @addi r1, sp, 20
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    @ldw r0, +12(sp)
    @addi r1, sp, 20
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    pmovi bx, 0
    recv p0, bx
    quit
    ldw ra, +0(sp)
    addi sp, sp, -24
    ret
tea_encrypt_secure_exit_1:    # addr=404
    quit
    ldw ra, +0(sp)
    addi sp, sp, -24
    ret
main:    # addr=420
    addi sp, sp, 4
    stw ra, +0(sp)
    la r0, 456
    mov p0, r0
    call -107    # -> tea_encrypt @ 12
    mov r0, p0
    ldw ra, +0(sp)
    addi sp, sp, -4
    ret
