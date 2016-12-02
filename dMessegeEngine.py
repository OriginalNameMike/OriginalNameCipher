class DMessegeEngine:
    def __init__(self, key):
        self.key = key
        self.alphabet = [ letter for letter in range( ord("A"),ord("Z") + 1 )]
        self.alphabet1 = [ letter for letter in range( ord("a"),ord("z") + 1 )]
    def transform(self, letter, key):
        ord_letter = ord(letter)

        if (ord_letter in self.alphabet):
            first_letter = self.alphabet[0]
            transformed = ( (ord_letter + key - first_letter) % len(self.alphabet) ) + first_letter
            return chr( transformed )

        elif (ord_letter in self.alphabet1):
            first_letter = self.alphabet1[0]
            transformed = ( (ord_letter + key - first_letter) % len(self.alphabet1) ) + first_letter
            return chr( transformed )

        else:
            return letter
        

    def cipher(self, messege):
        return "".join([self.transform(letter, self.key) for letter in messege ])

    def decipher(self, ciphered):
        return "".join([self.transform(letter, -self.key) for letter in ciphered ])

    def report(self, begin_messege):

        print("Используем ключ : {}".format(self.key) )

        print( "Исходный текст: {}" .format(begin_messege) )

        ciphered = self.cipher(begin_messege)
        print("После шифрования: {}" .format(ciphered) )

        deciphered = self.decipher(ciphered)
        print( "После дешифрования: {}" .format(deciphered) )

        print("-" * 40)
        