_init_:
    addi sp, sp, 32
    addi p0, zero, 20
    call 1  # @sec_sum
    jmp 19  # @_end_

sec_sum: # sum(n): p0:n, p0:suma de numeros del 0 al n
    addi sp, sp, 12
    stw ra,+ 0(sp)
    stw r0,+ 4(sp)
    stw r1,+ 8(sp)

    login 0xA9C1F
    movi r0, 0     # i=0
    movi r1, 0     # sum=0
    loop:
        add r1, r1, r0
        addi r0, r0, 1
        bne r0, p0, -3
    
    @stw r1,+ 4(zero)
    send bx, r1
    quit
    mov p0, r1

    ldw r1,+ 8(sp)
    ldw r0,+ 4(sp)
    ldw ra,+ 0(sp)
    addi sp, sp, -12
    ret

_end_:
    sth p0,+ 6(zero)