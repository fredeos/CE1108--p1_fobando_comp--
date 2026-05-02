_init__:
    jmp 15   # @main

sum: # sum(a,b): p0=a, p1=b, p0 = res
    addi sp, sp, 12
    stw ra,+ 0(sp)
    stw r0,+ 4(sp)
    stw r1,+ 8(sp)
    
    li r0,  0  # i=0 
    mov r1, zero # sum = 0
    loop:
        add r1, r1, p0 # sum += a
        addi r0, r0, 1 # i++
        blt r0, p1, -3 # @loop
    mov p0, r1

    ldw r1,+ 8(sp) 
    ldw r0,+ 4(sp)
    ldw ra,+ 0(sp)
    subi sp, sp, 12
    ret

main:
    movi p0, 7
    movi p1, 10
    call 1          # @sum(7,10)
    divi r0, p0, 5