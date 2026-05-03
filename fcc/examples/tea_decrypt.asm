; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 468
    call 104    # entrada principal | -> main @ 424
__halt__:    # addr=8
    jmp -1    # -> __halt__ @ 8
tea_decrypt:    # addr=12
    addi sp, sp, 24
    stw ra, +0(sp)
    mov p0, zero
    login 0xBEEF0
    beqz lr, 94    # -> tea_decrypt_secure_exit_1 @ 408
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
    send bx, delta
    @slli r0, r0, 5
    @stw r0, +8(sp)
    pmovi bx, 0
    @stw r0, +4(sp)
tea_decrypt_for_cond_2:    # addr=104
    @ldw r0, +4(sp)
    pmovi cx, 32
    @bge r0, r1, 55    # -> tea_decrypt_for_end_4 @ 336
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
    psub cx, cx, bx
    @stw r1, +12(sp)
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
    psub bx, bx, cx
    @stw r0, +16(sp)
    send bx, delta
    @ldw r1, +8(sp)
    psub cx, cx, bx
    @stw r1, +8(sp)
tea_decrypt_for_update_3:    # addr=316
    pmovi cx, 1
    @ldw r0, +4(sp)
    padd bx, bx, cx
    @stw r0, +4(sp)
    @jmp -58    # -> tea_decrypt_for_cond_2 @ 104
tea_decrypt_for_end_4:    # addr=336
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
tea_decrypt_secure_exit_1:    # addr=408
    quit
    ldw ra, +0(sp)
    addi sp, sp, -24
    ret
main:    # addr=424
    addi sp, sp, 4
    stw ra, +0(sp)
    la r0, 460
    mov p0, r0
    call -108    # -> tea_decrypt @ 12
    mov r0, p0
    ldw ra, +0(sp)
    addi sp, sp, -4
    ret
