; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 1340
    call 235    # entrada principal | -> main @ 948
__halt__:    # addr=8
    jmp -1    # -> __halt__ @ 8
tea_delta32:    # addr=12
    addi sp, sp, 8
    stw ra, +0(sp)
    li r0, 158
    stw r0, +4(sp)
    ldw r0, +4(sp)
    slli r0, r0, 8
    orri r0, r0, 55
    stw r0, +4(sp)
    ldw r0, +4(sp)
    slli r0, r0, 8
    orri r0, r0, 121
    stw r0, +4(sp)
    ldw r0, +4(sp)
    slli r0, r0, 8
    orri r0, r0, 185
    stw r0, +4(sp)
    ldw r0, +4(sp)
    mov p0, r0
    ldw ra, +0(sp)
    addi sp, sp, -8
    ret
tea_encrypt_vault:    # addr=96
    addi sp, sp, 32
    stw ra, +0(sp)
    mov p0, zero
    login 0xBEEF0
    beqz lr, 97    # -> tea_encrypt_vault_secure_exit_1 @ 504
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
    @call -40    # -> tea_delta32 @ 12
    send bx, p0
    @stw r0, +12(sp)
    pmovi bx, 0
    @stw r0, +8(sp)
    pmovi bx, 0
    @stw r0, +4(sp)
tea_encrypt_vault_while_cond_2:    # addr=196
    @ldw r0, +4(sp)
    pmovi cx, 32
    @bge r0, r1, 56    # -> tea_encrypt_vault_while_end_3 @ 432
    @ldw r0, +12(sp)
    @ldw r1, +8(sp)
    padd cx, cx, bx
    @stw r1, +8(sp)
    @ldw r1, +16(sp)
    pmovi bx, 4
    @stw p1, +28(sp)
    @addi r3, sp, 28
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
    @addi r5, sp, 28
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
    @addi r3, sp, 28
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
    @addi r5, sp, 28
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
    @jmp -59    # -> tea_encrypt_vault_while_cond_2 @ 196
tea_encrypt_vault_while_end_3:    # addr=432
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
    addi sp, sp, -32
    ret
tea_encrypt_vault_secure_exit_1:    # addr=504
    quit
    ldw ra, +0(sp)
    addi sp, sp, -32
    ret
tea_decrypt_vault:    # addr=520
    addi sp, sp, 32
    stw ra, +0(sp)
    mov p0, zero
    login 0xBEEF0
    beqz lr, 98    # -> tea_decrypt_vault_secure_exit_4 @ 932
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
    @call -146    # -> tea_delta32 @ 12
    send bx, p0
    @stw r0, +12(sp)
    @ldw r0, +12(sp)
    @slli r0, r0, 5
    @stw r0, +8(sp)
    pmovi bx, 0
    @stw r0, +4(sp)
tea_decrypt_vault_while_cond_5:    # addr=624
    @ldw r0, +4(sp)
    pmovi cx, 32
    @bge r0, r1, 56    # -> tea_decrypt_vault_while_end_6 @ 860
    @ldw r0, +20(sp)
    pmovi cx, 4
    @stw p1, +28(sp)
    @addi r3, sp, 28
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
    @addi r5, sp, 28
    pmovi hx, 3
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor bx, bx, cx, dx
    @ldw r1, +16(sp)
    psub cx, cx, bx
    @stw r1, +16(sp)
    @ldw r1, +16(sp)
    pmovi bx, 4
    @addi r3, sp, 28
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
    @addi r5, sp, 28
    pmovi hx, 1
    pmuli hx, hx, 4
    padd gx, gx, hx
    ldvw fx, +0(gx)
    psrladd dx, dx, ex, fx
    pxorxor cx, cx, bx, dx
    @ldw r0, +20(sp)
    psub bx, bx, cx
    @stw r0, +20(sp)
    @ldw r0, +12(sp)
    @ldw r1, +8(sp)
    psub cx, cx, bx
    @stw r1, +8(sp)
    pmovi cx, 1
    @ldw r0, +4(sp)
    padd bx, bx, cx
    @stw r0, +4(sp)
    @jmp -59    # -> tea_decrypt_vault_while_cond_5 @ 624
tea_decrypt_vault_while_end_6:    # addr=860
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
    addi sp, sp, -32
    ret
tea_decrypt_vault_secure_exit_4:    # addr=932
    quit
    ldw ra, +0(sp)
    addi sp, sp, -32
    ret
main:    # addr=948
    addi sp, sp, 28
    stw ra, +0(sp)
    login 0xBEEF0
    beqz lr, 87    # -> main_secure_exit_7 @ 1312
    pmovi bx, 100
    @addi r1, sp, 20
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    pmovi bx, 200
    @addi r1, sp, 20
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @stw r0, +0(r1)
    pmovi bx, 1
    @addi r1, sp, 4
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    stvw bx, +0(cx)
    pmovi bx, 2
    @addi r1, sp, 4
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    stvw bx, +0(cx)
    pmovi bx, 3
    @addi r1, sp, 4
    pmovi dx, 2
    pmuli dx, dx, 4
    padd cx, cx, dx
    stvw bx, +0(cx)
    pmovi bx, 4
    @addi r1, sp, 4
    pmovi dx, 3
    pmuli dx, dx, 4
    padd cx, cx, dx
    stvw bx, +0(cx)
    @addi r0, sp, 20
    @addi r1, sp, 4
    recv p0, bx
    recv p1, cx
    @call -258    # -> tea_encrypt_vault @ 96
    send cx, p0
    @addi r1, sp, 20
    @addi r0, sp, 4
    recv p0, cx
    recv p1, bx
    @call -158    # -> tea_decrypt_vault @ 520
    send bx, p0
    @addi r1, sp, 20
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    pmovi r1, 1328
    @stw r0, +0(r1)
    @addi r1, sp, 20
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    pmovi r1, 1332
    @stw r0, +0(r1)
    @addi r1, sp, 20
    pmovi dx, 0
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    pmovi cx, 100
    @bne r0, r1, 15    # -> main_if_else_9 @ 1300
    @addi r1, sp, 20
    pmovi dx, 1
    pmuli dx, dx, 4
    padd cx, cx, dx
    @ldw r0, +0(r1)
    pmovi cx, 200
    @bne r0, r1, 4    # -> main_if_else_11 @ 1284
    pmovi bx, 1
    pmovi r1, 1336
    @stw r0, +0(r1)
    @jmp 3    # -> main_if_end_10 @ 1296
main_if_else_11:    # addr=1284
    pmovi bx, 0
    pmovi r1, 1336
    @stw r0, +0(r1)
main_if_end_10:    # addr=1296
    @jmp 3    # -> main_if_end_8 @ 1312
main_if_else_9:    # addr=1300
    pmovi bx, 0
    pmovi r1, 1336
    @stw r0, +0(r1)
main_if_end_8:    # addr=1312
main_secure_exit_7:    # addr=1312
    quit
    ldw ra, +0(sp)
    addi sp, sp, -28
    ret
