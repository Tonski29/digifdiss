from Crypto.Cipher import AES
import base64
import os


def encrypt(privateInfo, key):
    BLOCK_SIZE = 16
    PADDING = '{'

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))


    print('encryption key:', str(key))
    cipher = AES.new(key)
    encoded = EncodeAES(cipher, privateInfo)
    print('Encrypted string', str(encoded))
    return encoded


def decrypt(cipher_text, key):
    PADDING = '{'
    decodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, cipher_text)
    print(decoded)