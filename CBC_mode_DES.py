import random

def expansion(pblock):
        left = []
        
        left = pblock[:2]
        left.append(pblock[3])
        left.append(pblock[2])
        left.append(pblock[3])
        left.append(pblock[2])
        left.extend(pblock[4:])

        return left
        
def left_half(pblock):
    num = int(len(pblock)/2)
    return pblock[:num]

def right_half(pblock):
    num = int(len(pblock)/2)
    return pblock[num:]

def xor(pblock, key):
    new = ''
    for bit, key_bit in zip(pblock, key):
        new += str(bit ^ key_bit)
    return list(map(int,new))

def sbox1(bits):
    sbox1 = [[[1,0,1], [0,1,0], [0,0,1], [1,1,0], [1,1,0], [1,0,0], [1,1,1], [0,0,0]],
         [[0,0,1], [1,0,0], [1,1,0], [0,1,0], [0,0,0], [1,1,1], [1,0,1], [0,1,1]]]
      
    index = bits[1]*4 + bits[2]*2 + bits[3]*1
    
    return sbox1[bits[0]][index]

def sbox2(bits):
    sbox2 = [[[1,0,0], [0,0,0], [1,1,0], [1,0,1], [1,1,1], [0,0,1], [0,1,1], [0,1,0]],
         [[1,0,1], [0,1,1], [0,0,0], [1,1,1], [1,1,0], [0,1,0], [0,0,1], [1,0,0]]]
             
    col = bits[1]*4+bits[2]*2+bits[3]*1
    return sbox2[bits[0]][col]

def key_shift_enc(key) :

    key_s =  key[1:]
    key_s.append(key[0])

    return key_s

def key_shift_dec(key) :
    
    key_s = key[:8]
    key_s.insert(0, key[-1])

    return key_s

def function(key, pblock):

    key = key[:8]
    rpblock = pblock[6:]
    lpblock = pblock[:6]
    bits = expansion(rpblock)
    bits = xor(bits, key)
    left = left_half(bits)
    right = right_half(bits)
    left = sbox1(left)
    right = sbox2(right)
    bits = left + right
    bits = xor(bits, lpblock)
    bits = rpblock + bits
    
    return bits

def sdes_encrypt(key, pblock):

    pblock_tmp = []
    
    pblock = function(key, pblock)
    
    key = key_shift_enc(key)
    pblock = function(key, pblock)
    
    key = key_shift_enc(key)
    pblock = function(key, pblock)

    pblock_tmp.extend(pblock[6:])
    pblock_tmp.extend(pblock[:6])
    pblock = pblock_tmp

    return pblock

def sdes_decrypt(key, pblock):
    
    key3 = []
    pblock_tmp = []
    
    key3 = key[2:]
    key3.extend(key[:2])
    key = key3
    
    pblock = function(key, pblock)
    
    key = key_shift_dec(key)
    pblock = function(key, pblock)
    
    key = key_shift_dec(key)
    pblock = function(key, pblock)

    pblock_tmp.extend(pblock[6:])
    pblock_tmp.extend(pblock[:6])
    pblock = pblock_tmp

    return pblock

def cbc_genkey():

    numlist = [random.randint(0,1) for _ in range(9)]

    return numlist

def cbc_encrypt(key, IV, pblock):

    pblock_tmp = []
    result = []
    cnt = 0
    IV_tmp = IV

    while True:
        pblock_tmp = pblock[cnt*12:cnt*12+12]

        if(len(pblock)/12 == cnt):
                break
        else:
                pblock_tmp = xor(pblock_tmp, IV_tmp)
                pblock_tmp = sdes_encrypt(key, pblock_tmp)
                IV_tmp = pblock_tmp
                cnt += 1
                result.extend(pblock_tmp)

    return result

def cbc_decrypt(key, IV, cblock):
    
    cblock_tmp = []
    result = []
    cnt = 0
    IV_tmp = []

    while True:
        cblock_tmp = cblock[cnt*12:cnt*12+12]

        if(len(cblock)/12 == cnt):
                break
        else:
                cblock_tmp = sdes_decrypt(key, cblock_tmp)
                if(cnt == 0):
                    cblock_tmp = xor(cblock_tmp, IV)
                else:
                    cblock_tmp = xor(cblock_tmp, IV_tmp)
                    
                IV_tmp = cblock[cnt*12:cnt*12+12]
                cnt += 1
                result.extend(cblock_tmp)
                

    return result
    
