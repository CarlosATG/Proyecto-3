from bitarray import bitarray
mensaje=bitarray('11010110111')
print(len(mensaje))
FF8=bitarray(input("escribe 8bits \n"))
for bits in mensaje:
    print(bits)
    prop=FF8[0]
    FF8[7] = prop ^ bits
    print(FF8)
    if prop == 0:
        FF8 <<= 1
        continue
        #hay retro-alimentacion en 7,5,2,1 que equivale a las posiciones 0,2,5,6
    FF8[6] = FF8[7] ^ prop
    FF8[5] = FF8[6] ^ prop
    FF8[4] = FF8[5]
    FF8[3] = FF8[4]
    FF8[2] = FF8[3] ^ prop
    FF8[1] = FF8[2]
    FF8[0] = FF8[1] ^ prop
    #
    # FF8[0]= FF8[1]^prop
    # FF8[1]=FF8[2]
    # FF8[2]=FF8[3]^prop
    # FF8[3]=FF8[4]
    # FF8[4]=FF8[5]
    # FF8[5]=FF8[6]^prop
    # FF8[6]=FF8[7]^prop
    # FF8[7]=prop
    print('chcking', FF8)
print('New CRC ',FF8)
for bits in mensaje:
    prop=FF8[0] ^ bits
    FF8[0]= FF8[1]^prop
    FF8[1]=FF8[2]
    FF8[2]=FF8[3]^prop
    FF8[3]=FF8[4]
    FF8[4]=FF8[5]
    FF8[5]=FF8[6]^prop
    FF8[6]=FF8[7]^prop
    FF8[7]=prop
print('Decodificado',FF8)
FF32=bitarray('00000000000000000000000000000000')
for bits in mensaje:
    prop= FF32[0]^bits
    for i in range(0,5):
        FF32[i]=FF32[i+1]
    FF32[6]=FF32[7]^prop
    FF32[7]=FF32[8]
    FF32[8]=FF32[9]
    FF32[9]=FF32[10]^prop
    FF32[10]=FF32[11]^prop
    for i in range(11,15):
        FF32[i] = FF32[i + 1]
    FF32[16]=FF32[17]^prop
    for i in range(17,19):
        FF32[i] = FF32[i + 1]
    for i in range(20, 22):
        FF32[i] = FF32[i + 1]^prop
    FF32[23] = FF32[24]
    FF32[24] = FF32[25]^prop
    FF32[25] = FF32[26]^prop
    FF32[26] = FF32[27]
    FF32[27] = FF32[28]^prop
    FF32[28] = FF32[29] ^ prop
    FF32[29] = FF32[30]
    FF32[30] = FF32[31] ^ prop
    FF32[31] = prop
print(FF32)
print(len(FF32))
b=bitarray('11010110111')
FlipFlopb=bitarray('0000')
for bit in b:
    prop=FlipFlopb[0]^bit
    FlipFlopb[0]=FlipFlopb[1]
    FlipFlopb[1]=FlipFlopb[2]
    FlipFlopb[2]=FlipFlopb[3]^prop
    FlipFlopb[3]=prop
print(FlipFlopb)
for bit in b:
    prop=FlipFlopb[0]^bit
    FlipFlopb[0]=FlipFlopb[1]
    FlipFlopb[1]=FlipFlopb[2]
    FlipFlopb[2]=FlipFlopb[3]^prop
    FlipFlopb[3]=prop
print('Decodificado',FlipFlopb)
