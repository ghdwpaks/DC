
import copy
from Cryptodome.Cipher import AES 
import socket
enc_count = 0
while True :
    s = input("입력 : ")

    def list_chunk(lst, n):
            return [lst[i:i+n] for i in range(0, len(lst), n)]

            

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
    def get_key(s = (str(socket.gethostname()).split("-"))[1]) : 
        
        #real_name : HCB8KMM
        real_name_multiply = (32 // len(s))+1
        real_name = (s * real_name_multiply)[:32]
        real_name = list(real_name)
        for i in range(len(real_name)) :
            real_name[i] = ord(real_name[i])
        key = copy.deepcopy(real_name)      
        aes = AESCryptoCBC(bytes(key))
        return aes
    aes = get_key()      
    
    dived_s = copy.deepcopy(s)
    s = list(s)
    temp = [s[0]]
    def return_isalph(w) :
        #w = "c"
        if w.isdigit() :
            return "n"
        else :
            if w.encode().isalpha():
                return "g"
            else: 
                return "k"
    def FillUp0(i,byte=4) :
        #i = 10
        i = list(i)
        while True :
            if len(i) < byte :
                i.insert(0,"0")
            else :
                break
        return "".join(i)
    dived_s = list(dived_s)
    alpha = return_isalph(dived_s[0])
    temp_res = []
    for i in range(len(dived_s)) :
        if 'g' == alpha:
            dived_s[i] = ord(dived_s[i])
        elif 'k' == alpha :
            c = dived_s[i]
            od = hex(ord(c))[2:]
            #1 od : d64d
            od = list(od)
            od = list_chunk(od,2)
            for k in range(len(od)) :
                od[k] = "".join(od[k])
                od[k] = int("0x"+od[k], 16)
            temp_res.extend(od)
    if 'k' == alpha :
        dived_s = temp_res
    if len(dived_s) > 31 :
        temp = copy.deepcopy(dived_s)
        temp = list(temp)
        temp = list_chunk(dived_s,32)
        dived_s = copy.deepcopy(temp)
    else :
        dived_s = [dived_s]
    for i in range(len(dived_s)) :
        
        tempi = copy.deepcopy(dived_s[i])
        for j in range(32-len(tempi)) :
            tempi.append(0)
        enc = list(aes.encrypt(bytes(tempi)))
        dived_s[i] = copy.deepcopy(enc)
    for i in range(len(dived_s)) :
        for j in range(len(dived_s[i])) :
            
            dived_s[i][j] = FillUp0(hex(dived_s[i][j])[2:],2)
        dived_s[i] = "".join(dived_s[i])
    for i in range(len(dived_s)) :
        "".join(dived_s[i])
    res = alpha+"".join(dived_s)
    print(res)