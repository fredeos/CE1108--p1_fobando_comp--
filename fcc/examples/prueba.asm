; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 0
    addi sp, sp, 2047
    addi sp, sp, 421
    call 505    # entrada principal | -> main @ 2036
__halt__:    # addr=16
    jmp -1    # -> __halt__ @ 16
llenar:    # addr=20
    addi sp, sp, 8
    stw ra, 0(sp)
    li r0, 10
    stw p0, 4(sp)
    addi r1, sp, 4
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 20
    addi r1, sp, 4
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 30
    addi r1, sp, 4
    li r2, 2
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 40
    addi r1, sp, 4
    li r2, 3
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 0
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
sumar4:    # addr=148
    addi sp, sp, 12
    stw ra, 0(sp)
    li r0, 0
    stw r0, 4(sp)
    stw p0, 8(sp)
    addi r1, sp, 8
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, 0(r1)
    addi r2, sp, 8
    li r3, 1
    muli r3, r3, 4
    add r2, r2, r3
    ldw r1, 0(r2)
    add r0, r0, r1
    stw r0, 4(sp)
    addi r1, sp, 8
    li r2, 2
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, 0(r1)
    ldw r1, 4(sp)
    add r1, r1, r0
    stw r1, 4(sp)
    addi r0, sp, 8
    li r2, 3
    muli r2, r2, 4
    add r0, r0, r2
    ldw r1, 0(r0)
    ldw r0, 4(sp)
    add r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -12
    ret
usar_chars:    # addr=300
    addi sp, sp, 12
    stw ra, 0(sp)
    li r0, 65
    stw p0, 8(sp)
    addi r1, sp, 8
    li r2, 0
    add r1, r1, r2
    stb r0, 0(r1)
    li r0, 66
    addi r1, sp, 8
    li r2, 1
    add r1, r1, r2
    stb r0, 0(r1)
    addi r1, sp, 8
    li r2, 0
    add r1, r1, r2
    ldb r0, 0(r1)
    addi r2, sp, 8
    li r3, 1
    add r2, r2, r3
    ldb r1, 0(r2)
    add r0, r0, r1
    stw r0, 4(sp)
    addi r1, sp, 8
    li r2, 2
    add r1, r1, r2
    ldb r0, 0(r1)
    ldw r1, 4(sp)
    add r1, r1, r0
    stw r1, 4(sp)
    addi r0, sp, 8
    li r2, 3
    add r0, r0, r2
    ldb r1, 0(r0)
    ldw r0, 4(sp)
    add r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -12
    ret
usar_vault:    # addr=468
    addi sp, sp, 16
    stw ra, 0(sp)
    stw p0, 12(sp)
    addi r1, sp, 12
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    ldvw r0, 0(r1)
    addi r0, r0, 2
    stw r0, 8(sp)
    ldw r0, 8(sp)
    muli r0, r0, 3
    addi r1, sp, 12
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    stvw r0, 0(r1)
    addi r1, sp, 12
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    ldvw r0, 0(r1)
    ldw r1, 8(sp)
    add r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -16
    ret
combinar_regs:    # addr=588
    addi sp, sp, 8
    stw ra, 0(sp)
    mov r0, p0
    mov r1, p1
    add r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p0
    sub r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p1
    mul r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p1
    div r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p0
    mod r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p1
    and r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p0
    orr r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p1
    xor r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p0
    sll r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov r1, p1
    srl r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
ops_inmediatas:    # addr=776
    addi sp, sp, 4
    stw ra, 0(sp)
    mov r0, p0
    addi r0, r0, 1
    mov p0, r0
    mov r0, p0
    subi r0, r0, 2
    mov p0, r0
    mov r0, p0
    muli r0, r0, 3
    mov p0, r0
    mov r0, p0
    divi r0, r0, 2
    mov p0, r0
    mov r0, p0
    modi r0, r0, 5
    mov p0, r0
    mov r0, p0
    andi r0, r0, 7
    mov p0, r0
    mov r0, p0
    orri r0, r0, 8
    mov p0, r0
    mov r0, p0
    xori r0, r0, 1
    mov p0, r0
    mov r0, p0
    slli r0, r0, 1
    mov p0, r0
    mov r0, p0
    srli r0, r0, 1
    mov p0, r0
    mov r0, p0
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -4
    ret
comparaciones:    # addr=924
    addi sp, sp, 24
    stw ra, 0(sp)
    mov r0, p0
    mov r2, p1
    seq r1, r0, r2
    stw r1, 20(sp)
    mov r1, p0
    seqi r0, r1, 5
    stw r0, 16(sp)
    mov r0, p1
    seqi r1, r0, 0
    seqz r1, r1
    stw r1, 12(sp)
    ldw r1, 16(sp)
    seqz r1, r1
    stw r1, 8(sp)
    mov r1, p0
    stw r1, 4(sp)
    mov r1, p0
    mov r0, p1
    bne r1, r0, 4    # -> comparaciones_if_else_2 @ 1024
    ldw r1, 4(sp)
    addi r1, r1, 1
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_1 @ 1024
comparaciones_if_else_2:    # addr=1024
comparaciones_if_end_1:    # addr=1024
    mov r1, p0
    mov r0, p1
    beq r1, r0, 4    # -> comparaciones_if_else_4 @ 1052
    ldw r1, 4(sp)
    addi r1, r1, 2
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_3 @ 1052
comparaciones_if_else_4:    # addr=1052
comparaciones_if_end_3:    # addr=1052
    mov r1, p0
    mov r0, p1
    bge r1, r0, 4    # -> comparaciones_if_else_6 @ 1080
    ldw r1, 4(sp)
    addi r1, r1, 3
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_5 @ 1080
comparaciones_if_else_6:    # addr=1080
comparaciones_if_end_5:    # addr=1080
    mov r1, p0
    mov r0, p1
    ble r1, r0, 4    # -> comparaciones_if_else_8 @ 1108
    ldw r1, 4(sp)
    addi r1, r1, 4
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_7 @ 1108
comparaciones_if_else_8:    # addr=1108
comparaciones_if_end_7:    # addr=1108
    mov r1, p0
    mov r0, p1
    bgt r1, r0, 4    # -> comparaciones_if_else_10 @ 1136
    ldw r1, 4(sp)
    addi r1, r1, 5
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_9 @ 1136
comparaciones_if_else_10:    # addr=1136
comparaciones_if_end_9:    # addr=1136
    mov r1, p0
    mov r0, p1
    blt r1, r0, 4    # -> comparaciones_if_else_12 @ 1164
    ldw r1, 4(sp)
    addi r1, r1, 6
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_11 @ 1164
comparaciones_if_else_12:    # addr=1164
comparaciones_if_end_11:    # addr=1164
    ldw r1, 20(sp)
    beqz r1, 4    # -> comparaciones_if_else_14 @ 1188
    ldw r1, 4(sp)
    addi r1, r1, 7
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_13 @ 1188
comparaciones_if_else_14:    # addr=1188
comparaciones_if_end_13:    # addr=1188
    ldw r1, 12(sp)
    beqz r1, 4    # -> comparaciones_if_else_16 @ 1212
    ldw r1, 4(sp)
    addi r1, r1, 8
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_15 @ 1212
comparaciones_if_else_16:    # addr=1212
comparaciones_if_end_15:    # addr=1212
    ldw r1, 8(sp)
    beqz r1, 4    # -> comparaciones_if_else_18 @ 1236
    ldw r1, 4(sp)
    addi r1, r1, 9
    stw r1, 4(sp)
    jmp 0    # -> comparaciones_if_end_17 @ 1236
comparaciones_if_else_18:    # addr=1236
comparaciones_if_end_17:    # addr=1236
    ldw r1, 4(sp)
    mov p0, r1
    ldw ra, 0(sp)
    addi sp, sp, -24
    ret
mezclar:    # addr=1256
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x21
    beqz lr, 11    # -> mezclar_secure_exit_19 @ 1320
    send bx, p0
    send cx, p1
    send dx, p2
    pxorxor bx, bx, cx, dx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
mezclar_secure_exit_19:    # addr=1320
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
segura_regs:    # addr=1336
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x22
    beqz lr, 38    # -> segura_regs_secure_exit_20 @ 1508
    send bx, p0
    send cx, p1
    padd bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p0
    psub bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p1
    pmul bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p1
    pdiv bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p0
    pmod bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p1
    pand bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p0
    porr bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    send cx, p1
    pxor bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
segura_regs_secure_exit_20:    # addr=1508
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
segura_inmediatas:    # addr=1524
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x23
    beqz lr, 36    # -> segura_inmediatas_secure_exit_21 @ 1688
    pmovi bx, 5
    @stw r0, 4(sp)
    send bx, p0
    @ldw r1, 4(sp)
    padd bx, bx, cx
    recv p0, bx
    send bx, p0
    paddi bx, bx, 1
    recv p0, bx
    send bx, p0
    psubi bx, bx, 2
    recv p0, bx
    send bx, p0
    pmuli bx, bx, 3
    recv p0, bx
    send bx, p0
    pdivi bx, bx, 2
    recv p0, bx
    send bx, p0
    pmodi bx, bx, 5
    recv p0, bx
    send bx, p0
    pandi bx, bx, 7
    recv p0, bx
    send bx, p0
    porri bx, bx, 8
    recv p0, bx
    send bx, p0
    pxori bx, bx, 1
    recv p0, bx
    send bx, p0
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
segura_inmediatas_secure_exit_21:    # addr=1688
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
suma_segura3:    # addr=1704
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x24
    beqz lr, 11    # -> suma_segura3_secure_exit_22 @ 1768
    send bx, p0
    send cx, p1
    send dx, p2
    paddadd bx, bx, cx, dx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
suma_segura3_secure_exit_22:    # addr=1768
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
desplaza_seguro:    # addr=1784
    addi sp, sp, 12
    stw ra, 0(sp)
    mov p0, zero
    login 0x25
    beqz lr, 16    # -> desplaza_seguro_secure_exit_23 @ 1868
    send bx, p0
    send cx, p1
    send dx, p2
    pslladd bx, bx, cx, dx
    @stw r0, 8(sp)
    @ldw r0, 8(sp)
    send cx, p1
    send dx, p2
    psrladd bx, bx, cx, dx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -12
    ret
desplaza_seguro_secure_exit_23:    # addr=1868
    quit
    ldw ra, 0(sp)
    addi sp, sp, -12
    ret
comparar_seguro:    # addr=1884
    addi sp, sp, 16
    stw ra, 0(sp)
    mov p0, zero
    login 0x26
    beqz lr, 29    # -> comparar_seguro_secure_exit_24 @ 2020
    send bx, p0
    send dx, p1
    pseq cx, bx, dx
    @stw r1, 12(sp)
    send cx, p0
    pseqi bx, cx, 7
    @stw r0, 8(sp)
    send bx, p0
    send cx, p1
    padd bx, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 12(sp)
    @beqz r0, 4    # -> comparar_seguro_if_else_26 @ 1972
    @ldw r0, 4(sp)
    paddi bx, bx, 1
    @stw r0, 4(sp)
    @jmp 0    # -> comparar_seguro_if_end_25 @ 1972
comparar_seguro_if_else_26:    # addr=1972
comparar_seguro_if_end_25:    # addr=1972
    @ldw r0, 8(sp)
    @beqz r0, 4    # -> comparar_seguro_if_else_28 @ 1996
    @ldw r0, 4(sp)
    paddi bx, bx, 2
    @stw r0, 4(sp)
    @jmp 0    # -> comparar_seguro_if_end_27 @ 1996
comparar_seguro_if_else_28:    # addr=1996
comparar_seguro_if_end_27:    # addr=1996
    @ldw r0, 4(sp)
    recv p0, bx
    quit
    ldw ra, 0(sp)
    addi sp, sp, -16
    ret
comparar_seguro_secure_exit_24:    # addr=2020
    quit
    ldw ra, 0(sp)
    addi sp, sp, -16
    ret
main:    # addr=2036
    addi sp, sp, 32
    stw ra, 0(sp)
    li r0, 0
    stw r0, 12(sp)
    li r0, 0
    stw r0, 8(sp)
    li r0, 1
    addi r1, sp, 16
    li r2, 0
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 2
    addi r1, sp, 16
    li r2, 1
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 3
    addi r1, sp, 16
    li r2, 2
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    li r0, 4
    addi r1, sp, 16
    li r2, 3
    muli r2, r2, 4
    add r1, r1, r2
    stw r0, 0(r1)
    addi r0, sp, 16
    mov p0, r0
    call -537    # -> llenar @ 20
    mov r0, p0
    addi r0, sp, 16
    mov p0, r0
    call -509    # -> sumar4 @ 148
    mov r0, p0
    stw r0, 8(sp)
    li r0, 0
    stw r0, 4(sp)
main_for_cond_29:    # addr=2200
    ldw r0, 4(sp)
    li r1, 4
    bge r0, r1, 13    # -> main_for_end_31 @ 2264
    addi r1, sp, 16
    ldw r2, 4(sp)
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, 0(r1)
    ldw r1, 8(sp)
    add r1, r1, r0
    stw r1, 8(sp)
main_for_update_30:    # addr=2244
    li r1, 1
    ldw r0, 4(sp)
    add r0, r0, r1
    stw r0, 4(sp)
    jmp -16    # -> main_for_cond_29 @ 2200
main_for_end_31:    # addr=2264
main_while_cond_32:    # addr=2264
    ldw r0, 12(sp)
    li r1, 2
    bge r0, r1, 16    # -> main_while_end_33 @ 2340
    ldw r0, 12(sp)
    ldw r1, 8(sp)
    li r2, 3
    mov p0, r0
    mov p1, r1
    mov p2, r2
    call -262    # -> mezclar @ 1256
    mov r2, p0
    ldw r1, 8(sp)
    add r1, r1, r2
    stw r1, 8(sp)
    li r1, 1
    ldw r2, 12(sp)
    add r2, r2, r1
    stw r2, 12(sp)
    jmp -19    # -> main_while_cond_32 @ 2264
main_while_end_33:    # addr=2340
    ldw r2, 8(sp)
    li r1, 50
    ble r2, r1, 6    # -> main_if_else_35 @ 2376
    ldw r2, 8(sp)
    la r1, 0
    addi r1, r1, 2047
    addi r1, r1, 417
    stw r2, 0(r1)
    jmp 14    # -> main_if_end_34 @ 2432
main_if_else_35:    # addr=2376
    ldw r2, 8(sp)
    li r1, 50
    bne r2, r1, 6    # -> main_elif_next_0_36 @ 2412
    li r2, 50
    la r1, 0
    addi r1, r1, 2047
    addi r1, r1, 417
    stw r2, 0(r1)
    jmp 5    # -> main_if_end_34 @ 2432
main_elif_next_0_36:    # addr=2412
    li r2, 0
    la r1, 0
    addi r1, r1, 2047
    addi r1, r1, 417
    stw r2, 0(r1)
main_if_end_34:    # addr=2432
    la r1, 0
    addi r1, r1, 2047
    addi r1, r1, 417
    ldw r2, 0(r1)
    mov p0, r2
    ldw ra, 0(sp)
    addi sp, sp, -32
    ret
