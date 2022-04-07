print("Dot Product Implementation with Forwarding")
ID1_17 = "015988271"
ID2_17 = "237100493"

R0_17=0

R1_17=0 #stores the sum

R2_17=[] #stores the fist vector
R4_17=[] #stores the second vector

R3_17=0*1 #point at next element in R2_17
R5_17=0*1 #point at next element in R4_17

R7_17=int(len(ID1_17)) #stores the length of vector which reduces after every cycle by one
ps_12=0

for var in ID1_17:
    R2_17.append(var) #1st vector stored

for var in ID2_17:
    R4_17.append(var) #2nd vector stored

def done():
    global ps_12 
    print("RESULTS AND ANALYSIS")
    print("Dot Product Using Forwarding")
    print("Two vectors are", ID1_17,"and",ID2_17)
    ps_12 = ps_12 + 1 #1 stalls due to beq $r7 $r0 done ; done  looping? Control Hazard 
    print("Dot Product Result=", R1_17, "stalls",ps_12) 
    exit()
#code starts here

R1_17=(R0_17 + R0_17)                       #addu $r1 $r0 $r0 ; result = 0
while(1):
 if R7_17==R0_17:                           #beq $r7 $r0 done ; done looping?
    done()
 else:
    if(R2_17):                          #Fetch  lw $r2 0($r3) ; load a elem
        True

    if(R2_17[R3_17])!="":                       #Decode lw $r2 0($r3) ; load a elem
        if(R4_17):                      #Fetch  lw $r4 0($r5) ; load b elem     
            True
    
    if len(R2_17)>=0:                       #Execute lw $r2 0($r3) ; load a elem
        if(R4_17[R5_17])!="":                   #Decode  lw $r4 0($r5) ; load b elem
            if(R2_17):                  #Fetch mul $r2 $r2 $r4 ;
                True                        

    if(R2_17[R3_17]):                       #Memory  lw $r2 0($r3) ; load a elem
        if len(R4_17)>=0:                   #Execute lw $r4 0($r5) ; load b elem
            if(R4_17[R5_17])!="":               #Decode mul $r2 $r2 $r4 ;
                if(R2_17):              #Fetch addu $r1 $r1 $r2 
                    True                            
                            
    if(R2_17[R3_17]):                       #Write  lw $r2 0($r3) ; load a elem
        m_v_12 = float(R2_17[R3_17])        
        m_v_12=m_v_12+0     
        if float(R4_17[R5_17])>=0:              #Memory lw $r4 0($r5) ; load b elem     
            ps_12=ps_12+1               
            pass                #NOP due to STALL           
            

    if(R4_17[R5_17]):                       #Write  lw $r4 0($r5) ; load b elem
        l_v_12 = float(R4_17[R5_17])        
        l_v_12=l_v_12+0 
        if len(R4_17)>=0:                   #Execute #mul $r2 $r2 $r4 ;
            if(R4_17[R5_17])!="":               #Decode addu $r1 $r1 $r2
             True

    if float(R4_17[R5_17])>=0:                  #Memory mul $r2 $r2 $r4 ; 
            ps_12=ps_12+1               
            pass                #NOP due to STALL           
    
                                                                    
    if(R4_17[R5_17]):                       #Write  mul $r2 $r2 $r4 
        if(R2_17[R3_17])!="":                   #Execute addu $r1 $r1 $r2             
            True        
        R2_17[R3_17] = float(R2_17[R3_17])*float(R4_17[R5_17])  
        R1_17=R1_17 + float(R2_17[R3_17])           #Memory addu $r1 $r1 $r2    
        R1_17=R1_17                     #Write addu $r1 $r1 $r2
        print(R2_17[0:R3_17])
        #print R1_17    
    R3_17=R3_17+1                           #Increment counter addiu $r3 $r3 #4
    R5_17=R5_17+1                           #Increment counter addiu $r5 $r5 #4 
    R7_17=R7_17-1
