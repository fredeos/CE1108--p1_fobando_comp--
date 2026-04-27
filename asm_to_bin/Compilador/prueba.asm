; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 464
    call 47    # entrada principal | -> main @ 192
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
    @mov r0, p0
    @li r1, 5
    @add r0, r0, r1
    @stw r0, 4(sp)
    @ldw r0, 4(sp)
    @mov p0, r0
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
ajuste_seguro_secure_exit_1:    # addr=176
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
main:    # addr=192
    addi sp, sp, 16
    stw ra, 0(sp)
    li r0, 0
    stw r0, 12(sp)
    li r0, 0
    stw r0, 8(sp)
    li r0, 0
    stw r0, 4(sp)
main_for_cond_2:    # addr=224
    ldw r0, 4(sp)
    li r1, 4
    bge r0, r1, 15    # -> main_for_end_4 @ 292
    ldw r0, 4(sp)
    li r1, 1
    mov p0, r0
    mov p1, r1
    call -60    # -> suma @ 12
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
main_for_update_3:    # addr=272
    li r0, 1
    ldw r1, 4(sp)
    add r1, r1, r0
    stw r1, 4(sp)
    jmp -16    # -> main_for_cond_2 @ 224
main_for_end_4:    # addr=292
main_while_cond_5:    # addr=292
    ldw r1, 12(sp)
    li r0, 3
    bge r1, r0, 13    # -> main_while_end_6 @ 352
    ldw r1, 12(sp)
    mov p0, r1
    call -61    # -> cuadrado @ 68
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
    li r0, 1
    ldw r1, 12(sp)
    add r1, r1, r0
    stw r1, 12(sp)
    jmp -14    # -> main_while_cond_5 @ 292
main_while_end_6:    # addr=352
    ldw r1, 8(sp)
    mov p0, r1
    call -61    # -> ajuste_seguro @ 116
    mov r1, p0
    ldw r0, 8(sp)
    add r0, r0, r1
    stw r0, 8(sp)
    ldw r0, 8(sp)
    li r1, 20
    ble r0, r1, 5    # -> main_if_else_8 @ 408
    ldw r0, 8(sp)
    la r1, 460
    stw r0, 0(r1)
    jmp 11    # -> main_if_end_7 @ 448
main_if_else_8:    # addr=408
    ldw r0, 8(sp)
    li r1, 20
    bne r0, r1, 5    # -> main_elif_next_0_9 @ 436
    li r0, 20
    la r1, 460
    stw r0, 0(r1)
    jmp 4    # -> main_if_end_7 @ 448
main_elif_next_0_9:    # addr=436
    li r0, 0
    la r1, 460
    stw r0, 0(r1)
main_if_end_7:    # addr=448
    ldw ra, 0(sp)
    addi sp, sp, -16
    ret
main_if_end_8:    # addr=448
    beqz lr, 11
    beq lr, zero, 11
    ret
    