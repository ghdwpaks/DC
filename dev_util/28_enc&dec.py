import copy as c
from Cryptodome.Cipher import AES 
import socket
class AESCryptoCBC():
    def __init__(self, key):
        # Initial vector를 0으로 초기화하여 16바이트 할당함
        # iv = chr(0) * 16 #pycrypto 기준
        iv = bytes([0x00] * 16) #pycryptodomex 기준
        # aes cbc 생성
        self.crypto = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, data):
        #암호화 message는 16의 배수여야 한다.
        enc = self.crypto.encrypt(data)
        return enc

    def decrypt(self, enc):
        #복호화 enc는 16의 배수여야 한다.
        dec = self.crypto.decrypt(enc)
        return dec

def get_key(s = (str(socket.gethostname()).split("-"))[1]) : 
    #s : HCB8KMM

    real_name_multiply = (32 // len(s))+1
    real_name = (s * real_name_multiply)[:32]
    real_name = list(real_name)
    for i in range(len(real_name)) :
        real_name[i] = ord(real_name[i])
    key = c.deepcopy(real_name)         
    #print("key :",key)
    aes = AESCryptoCBC(bytes(key))
    return aes
    #print("aes :",aes)
aes = get_key()


temp = [40, 60, 228, 136, 75, 137, 76, 154, 185, 54, 243, 76, 163, 160, 255, 104]
print("1 temp :",temp)
temp = list(aes.decrypt(bytes(temp)))
print("2 temp :",temp)
aes = get_key()
temp = list(aes.encrypt(bytes(temp)))
print("3 temp :",temp)