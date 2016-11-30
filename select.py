alphabet = [letter for letter in range(ord("a"),ord("z") + 1)]

def transform(letter, key):
    ord_letter = ord(letter)

    if (ord_letter in alphabet):
        first_letter = alphabet[0]
        transformed = ( (ord_letter + key - first_letter) % len(alphabet) ) + first_letter
        return chr( transformed )
    else:
        return letter
    

def cipher(text, key):
    
   
   

def decipher(text, key):

    return "".join([transform(letter, -key) for letter in text ])

def d_messege(messege, key):
    print("Используем ключ : {}".format(key) )

    print( "Исховный текст: {}" .format(messege) )

    ciphered = cipher(messege, key)
    print("После шифрования: {}" .format(ciphered) )

    deciphered = decipher(ciphered, key)
    print( "После дешифрования: {}" .format(deciphered) )

d_messege("niga beech", 10)

print("-" * 30)

d_messege("very good", 12)