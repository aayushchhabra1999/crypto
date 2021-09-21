## A playground implementation of AES Cipher (wraps the AES implementation of crytography lib).
## Mode ECB should never be used. For production, use GCM.
## This is only for learning purposes.

from cryptography.hazmat.primitives import ciphers
from cypher import CypherBase
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AESCypher(CypherBase):
    def __init__(self, key = None):
        self._key = key if key else os.urandom(16)

        AES = Cipher(algorithms.AES(self._key), modes.ECB(), backend=default_backend())
        self._encryptor = AES.encryptor()
        self._decryptor = AES.decryptor()
        self._padding = 0

    def encode(self, plaintext: str):
        length = len(plaintext)
        padding_needed = 16 - length%16
        self._padding = padding_needed
        net = plaintext + ' '*padding_needed
        return self._encryptor.update(net.encode())

    def decode(self, cyphertext: str):
        ret = self._decryptor.update(cyphertext).decode()
        # remove the padding
        len_plain = len(ret) - self._padding
        return ret[:len_plain]