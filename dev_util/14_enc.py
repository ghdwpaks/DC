'''
codes from : https://jonghyeok-dev.tistory.com/13
'''


import base64
from Crypto import Random
from Crypto.Cipher import AES

class AES256():

    def __init__(self, key):
        self.bs = 128
        self.key = key.encode('utf-8')
        self.key = AES256.str_to_bytes(key)

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * AES256.str_to_bytes(chr(self.bs - len(s) % self.bs))

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, raw):
        raw = self._pad(AES256.str_to_bytes(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

cry = "hellohellohellohellohellohellohellohellohellohellohellohello0000"
key = "DESKTOPHCB8KMMDESKTOPHCB8KMMDESKTOPHCB8KMMDESKTOPHCB8KMM"
print("len(cry) :",len(cry))
print("len(key) :",len(key))
print(AES256.encrypt(cry,key))
