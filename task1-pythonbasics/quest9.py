def caesar_encrypt(text,shift):
    encrypted='' 
    for char in text:
        if char.isupper():
            base=ord('A')
        else:
            base=ord('a')
        encrypted+= chr((ord(char))-base + int(shift) % 26 + base)
    return encrypted

string=input('enter your text')
print('your encrypted text is - ', caesar_encrypt(string,3))

