## The most basic cipher (Caesar Cipher)

from cypher import CypherBase

class ShiftCypher(CypherBase):
    def __init__(self, shift:int = 3):
        self.shift = shift

    def _shift(self, text, shift):
        result = []
        for letter in text:
            if letter.isalpha():
                result.append(chr(ord(letter) + shift))
            else:
                result.append(letter)
        return ''.join(result)

    def encode(self, pt:str):
        return self._shift(pt, self.shift)

    def decode(self, ct:str):
        return self._shift(ct, -self.shift)