def shift_encrypt(msg, key):
    output = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for c in msg:
        index = alphabet.find(c)
        if index < 0:
            output += ' '
        else:
            new_index = (index + key) % len(alphabet)
            ctx = alphabet[new_index]
            output += ctx
    return output

def shift_decrypt(ctx, key):
    output = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for c in ctx:
        index = alphabet.find(c)
        if index < 0:
            output += ' '
        else:
            new_index = (index - key) % len(alphabet)
            plain = alphabet[new_index]
            output += plain
    return output
    
print(shift_encrypt('abc', 3)    
msg = print(shift_encrypt('abc', 3)
print(shift_decrypt(msg, 3)
