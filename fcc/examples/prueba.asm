; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 588
    call 67    # entrada principal | -> main @ 272
__halt__:    # addr=8
    jmp 0    # -> __halt__ @ 8
suma:    # addr=12
    addi sp, sp, 8
    stw ra, 0(sp)
    mov r0, p0
    mov r1, p1
    add r0, r0, r1
    stw r0, 4(sp)
    ldw r0, 4(sp)
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
cuadrado:    # addr=68
    addi sp, sp, 4
    stw ra, 0(sp)
    mov r0, p0
    mov r1, p0
    mul r0, r0, r1
    mov p0, r0
    ldw ra, 0(sp)
    addi sp, sp, -4
    ret
    ldw ra, 0(sp)
    addi sp, sp, -4
    ret
ajuste_seguro:    # addr=116
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x21
    beqz lr, 11    # -> ajuste_seguro_secure_exit_1 @ 176
    send ax, p0
    pmovi bx, 5
    padd ax, ax, bx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv ax, p0
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
ajuste_seguro_secure_exit_1:    # addr=176
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
mezcla_segura:    # addr=192
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x44
    beqz lr, 12    # -> mezcla_segura_secure_exit_2 @ 256
    send ax, p0
    send bx, p1
    send cx, p2
    pxorxor ax, ax, bx, cx
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    recv ax, p0
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
mezcla_segura_secure_exit_2:    # addr=256
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
main:    # addr=272
    addi sp, sp, 16
    stw ra, 0(sp)
    li r0, 0
    stw r0, 12(sp)
    li r0, 0
    stw r0, 8(sp)
    li r0, 0
    stw r0, 4(sp)
main_for_cond_3:    # addr=304
    ldw r0, 4(sp)
    li r1, 4
    bge r0, r1, 15    # -> main_for_end_5 @ 372
    ldw r0, 4(sp)
    li r1, 1
    mov p0, r0
    mov p1, r1
    call -80    # -> suma @ 12
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
main_for_update_4:    # addr=352
    li r0, 1
    ldw r1, 4(sp)
    add r1, r1, r0
    stw r1, 4(sp)
    jmp -16    # -> main_for_cond_3 @ 304
main_for_end_5:    # addr=372
main_while_cond_6:    # addr=372
    ldw r1, 12(sp)
    li r0, 3
    bge r1, r0, 13    # -> main_while_end_7 @ 432
    ldw r1, 12(sp)
    mov p0, r1
    call -81    # -> cuadrado @ 68
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
    li r0, 1
    ldw r1, 12(sp)
    add r1, r1, r0
    stw r1, 12(sp)
    jmp -14    # -> main_while_cond_6 @ 372
main_while_end_7:    # addr=432
    ldw r1, 8(sp)
    mov p0, r1
    call -81    # -> ajuste_seguro @ 116
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
    ldw r0, 8(sp)
    li r1, 7
    li r2, 3
    mov p0, r0
    mov p1, r1
    mov p2, r2
    call -73    # -> mezcla_segura @ 192
    mov r2, p0
    ldw r1, 8(sp)
    add r1, r1, r2
    stw r1, 8(sp)
    ldw r1, 8(sp)
    li r2, 20
    ble r1, r2, 5    # -> main_if_else_9 @ 532
    ldw r1, 8(sp)
    la r2, 584
    stw r1, 0(r2)
    jmp 11    # -> main_if_end_8 @ 572
main_if_else_9:    # addr=532
    ldw r1, 8(sp)
    li r2, 20
    bne r1, r2, 5    # -> main_elif_next_0_10 @ 560
    li r1, 20
    la r2, 584
    stw r1, 0(r2)
    jmp 4    # -> main_if_end_8 @ 572
main_elif_next_0_10:    # addr=560
    li r1, 0
    la r2, 584
    stw r1, 0(r2)
main_if_end_8:    # addr=572
    ldw ra, 0(sp)
    addi sp, sp, -16
    ret
