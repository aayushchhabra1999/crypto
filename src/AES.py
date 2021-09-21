from cryptography.hazmat import backends
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
import os

key = os.urandom(16)
aesCypher = Cipher(algorithms.AES(key), modes.ECB(), backend = default_backend())
encryptor = aesCypher.encryptor()
decryptor = aesCypher.decryptor()

