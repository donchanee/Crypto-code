def vigenere_genkey(n):
    output = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for c in range(0, n):
        a = random.choice(alphabet)
        output += a
    return output

def vigenere_encrypt(msg, key):
    output = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cnt = 0
    
    for c in msg:
        index = alphabet.find(c)
        keyindex = alphabet.find(key[cnt])
        cnt+=1
        if index < 0:
            output += ' '
        else:
            new_index = (index + keyindex) % len(alphabet)
            ctx = alphabet[new_index]
            output += ctx
    return output

def vigenere_decrypt(msg, key):
    output = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cnt = 0
    
    for c in msg:
        index = alphabet.find(c)
        keyindex = alphabet.find(key[cnt])
        cnt+=1
        if index < 0:
            output += ' '
        else:
            new_index = (index - keyindex) % len(alphabet)
            plain = alphabet[new_index]
            output += plain
    return output
