; Codigo ensamblador generado por FCC
; ISA base: F32IS (isa.md)
__init__:    # addr=0
    li sp, 748
    call 90    # entrada principal | -> main @ 364
__halt__:    # addr=8
    jmp 0    # -> __halt__ @ 8
llenar:    # addr=12
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
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
sumar4:    # addr=132
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
mezclar:    # addr=284
    addi sp, sp, 8
    stw ra, 0(sp)
    mov p0, zero
    login 0x21
    beqz lr, 12    # -> mezclar_secure_exit_1 @ 348
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
mezclar_secure_exit_1:    # addr=348
    quit
    ldw ra, 0(sp)
    addi sp, sp, -8
    ret
main:    # addr=364
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
    call -120    # -> llenar @ 12
    addi r0, sp, 16
    mov p0, r0
    call -93    # -> sumar4 @ 132
    mov r0, p0
    stw r0, 8(sp)
    li r0, 0
    stw r0, 4(sp)
main_for_cond_2:    # addr=524
    ldw r0, 4(sp)
    li r1, 4
    bge r0, r1, 14    # -> main_for_end_4 @ 588
    addi r1, sp, 16
    ldw r2, 4(sp)
    muli r2, r2, 4
    add r1, r1, r2
    ldw r0, 0(r1)
    ldw r1, 8(sp)
    add r1, r1, r0
    stw r1, 8(sp)
main_for_update_3:    # addr=568
    li r1, 1
    ldw r0, 4(sp)
    add r0, r0, r1
    stw r0, 4(sp)
    jmp -15    # -> main_for_cond_2 @ 524
main_for_end_4:    # addr=588
main_while_cond_5:    # addr=588
    ldw r0, 12(sp)
    li r1, 2
    bge r0, r1, 17    # -> main_while_end_6 @ 664
    ldw r0, 12(sp)
    ldw r1, 8(sp)
    li r2, 3
    mov p0, r0
    mov p1, r1
    mov p2, r2
    call -85    # -> mezclar @ 284
    mov r2, p0
    ldw r1, 8(sp)
    add r1, r1, r2
    stw r1, 8(sp)
    li r1, 1
    ldw r2, 12(sp)
    add r2, r2, r1
    stw r2, 12(sp)
    jmp -18    # -> main_while_cond_5 @ 588
main_while_end_6:    # addr=664
    ldw r2, 8(sp)
    li r1, 50
    ble r2, r1, 5    # -> main_if_else_8 @ 692
    ldw r2, 8(sp)
    la r1, 744
    stw r2, 0(r1)
    jmp 11    # -> main_if_end_7 @ 732
main_if_else_8:    # addr=692
    ldw r2, 8(sp)
    li r1, 50
    bne r2, r1, 5    # -> main_elif_next_0_9 @ 720
    li r2, 50
    la r1, 744
    stw r2, 0(r1)
    jmp 4    # -> main_if_end_7 @ 732
main_elif_next_0_9:    # addr=720
    li r2, 0
    la r1, 744
    stw r2, 0(r1)
main_if_end_7:    # addr=732
    ldw ra, 0(sp)
    addi sp, sp, -32
    ret
