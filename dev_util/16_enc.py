"codes from : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221021909030"

# -*- coding: utf-8 -*-
# python3는 Cryptodome, python2는 Crypto
# pycrypto 설치 필요
# from Crypto import Random   
# from Crypto.Cipher import AES
# pycryptodomex 설치 필요
from Cryptodome import Random   
from Cryptodome.Cipher import AES 


BLOCK_SIZE=16

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

#키 32바이트 = aes 256
key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6,0xA7, 0x6E, 0xE6, 0xE5, 0x3F]

#원본 데이터
data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16]

print("len(key) :",len(key))
print("len(data) :",len(data))
#출력
print("Data is " + str(data))

data = [14, 217, 152, 222, 202, 9, 206, 186, 14, 217, 152, 222, 202, 9, 206, 186]


#키 생성
aes = AESCryptoCBC(bytes(key))
print("aes :",aes)
#변경
enc = aes.encrypt(bytes(data))
print("The encrypted value is " + str(list(enc)))

#키 생성
aes2 = AESCryptoCBC(bytes(key))
#변경
dec = aes2.decrypt(bytes(enc))
print("The decrypted value is " + str(list(dec)))