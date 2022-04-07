print (' - DOT PRODUCT WITHOUT FORWARDING - ')
print ('STUDENT ID- 015268617')
ID1_17 = '015268617'
ID2_17 = '237480839'

R0_17 = 0

R1_17 = 0  # USED FOR STORING THE RESULT

R2_17 = []  # FIRST VECTOR
R4_17 = []  # SECOND VECTOR

R3_17 = 0 * 1  # NEXT ELEMENT POINTER IN R2
R5_17 = 0 * 1  # NEXT ELEMENT POINTER IN R4

R7_17 = int(len(ID1_17))  # STORE THE LENGTH OF A VECTOR
Stalls_17 = 0

for var in ID1_17:
    R2_17.append(var)  # STORE 1st VECTOR

for var in ID2_17:
    R4_17.append(var)  # STORE SECOND VECTOR

def done():
    global Stalls_17
    print ('RESULT AND ANALYSIS')
    print ('Dot Product Without Forwarding')
    print ('Two vectors are', ID1_17, 'and', ID2_17)
    Stalls_17 = Stalls_17 + 3  # 3 INSTRUCTION DELAY
    print ('Dot Product Result=', R1_17, 'stalls', Stalls_17)
    exit()

                                            # START OF THE CODE

R1_17 = R0_17 + R0_17  # ADDU $R1 $R0 $R0 ; result = 0
while 1:
    if R7_17 == R0_17:  # BEQ $R7 $R0 DONE ; done looping?
        done()
    else:
        if R2_17:  # Fetch  LW $R2 0($R3) ; load a element
            True

        if R2_17[R3_17] != '':  # Decode LW $R2 0($R3) ; load a element
            if R4_17:  # Fetch  lw $R4 0($R5) ; load b element........
                True

        if len(R2_17) >= 0:  # Execute lW $R2 0($R3) ; load a element
            if R4_17[R5_17] != '':  # Decode  lW $R4 0($R5) ; load b element
                if R2_17:  # Fetch mul $R2 $R2 $R4 ;
                    True

        if R2_17[R3_17]:  # Memory  lW $R2 0($R3) ; load a element
            if len(R4_17) >= 0:  # Execute lW $R4 0($R5) ; load b element
                Stalls_17 = Stalls_17 + 1
                pass  # NOP due to STALL............

        if R2_17[R3_17]:  # Write  lW $R2 0($R3) ; load a element
            m_v_12 = float(R2_17[R3_17])
            m_v_12 = m_v_12 + 0
            if float(R4_17[R5_17]) >= 0:  # Memory lW $R4 0($R5) ; load b element
                Stalls_17 = Stalls_17 + 1
                pass  # NOP due to STALL............

        if R4_17[R5_17]:  # Write  lW $R4 0($R5) ; load b element
            l_v_12 = float(R4_17[R5_17])
            l_v_12 = l_v_12 + 0
            Stalls_17 = Stalls_17 + 1
            pass  # NOP due to STALL

        if R4_17[R5_17] != '':  # Decode MUL $R2 $R2 $R4 ;
            if R2_17:  # Fetch addu $R1 $R1 $R2....
                True

        if len(R4_17) >= 0:  # Execute #MUL $R2 $R2 $R4 ;
            Stalls_71 = Stalls_17 + 1
            pass  # NOP due to STALL....

        if float(R4_17[R5_17]) >= 0:  # Memory mul $r2 $r2 $r4 ;
            Stalls_17 = Stalls_17 + 1
            pass  # NOP due to STALL

        if R4_17[R5_17]:  # Write  MUL $R2 $R2 $R4
            R2_17[R3_17] = float(R2_17[R3_17]) * float(R4_17[R5_17])
            Stalls_17 = Stalls_17 + 1
            pass  # NOP due to STALL

        if R4_17[R5_17] != '':  # Decode ADDU $r1 $r1 $R2
            if R2_17[R3_17] != '':  # Execute ADDU $R1 $R1 $R2............
                R1_17 = R1_17 + float(R2_17[R3_17])  # Memory addu $R1 $R1 $R2....
                R1_17 = R1_17  # Write addu $R1 $R1 $R2....
        R3_17 = R3_17 + 1  # Increment counter addiu $R3 $R3 #4
        R5_17 = R5_17 + 1  # Increment counter addiu $R5 $R5 #4....

                                           # R7_71=R7_71-1

        if R7_17:  # Fetch  beq $R7 $R0 done ; done looping?
            Stalls_17 = Stalls_17 + 1
            pass  # NOP due to STALL

        if R7_17 != '':  # Decode beq Rr7 R0 done ; done looping?
            Stalls_17 = Stalls_17 + 1
            pass  # NOP due to STALL

        if len(str(R7_17)) >= 0:  # Execute BEQ $R7 $R0 done ; done looping?
            if R7_17 == R7_17:  # Memory  BEQ $R7 $R0 done ; done looping?
                R7_17 = R7_17 - 1  # Write and Decrement counter addiu $R7 $R7 #-1
        print (R2_17[0:R3_17])