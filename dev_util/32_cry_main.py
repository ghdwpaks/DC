
import copy
from Cryptodome.Cipher import AES 
import socket
enc_count = 0
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


def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

def enc(s) :
    #ghdwpaksghdaosdunfodsjn

            
    aes = get_key()      
    
    dived_s = copy.deepcopy(s)
    s = list(s)
    temp = [s[0]]
    
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
    return res



def dec(input_str) :
    #input_str ='g94c0ce0ade1452a940af00d843f50512aac9ed7bffdd6c74186516d05aadca07a1efe1337c0c43c30818a8022ef9819dac98f220a4d3615e3717bc7c0812620d'
    aes = get_key()

    alpha = ""
    div_s = copy.deepcopy(input_str)
    div_s = list(div_s)
    alpha = div_s[0]
    del div_s[0] 
    div_s = list_chunk(div_s,64)
    for i in range(len(div_s)) :
        temp = list_chunk(div_s[i],2)
        for j in range(len(temp)) :
            temp[j] = "".join(temp[j])
        temp_res = []
        dec = []
        for j in range(len(temp)) :
            temp[j] = int("0x"+temp[j],16)
        temp = list_chunk(temp , 16)
        dec_temp = []
        for j in range(len(temp)) :
            aes_dec = list(aes.decrypt(bytes(temp[j])))
            temp_dec = copy.deepcopy(aes_dec)
            dec_temp.extend(temp_dec)
        dec.extend(dec_temp)
        div_s[i] = dec

    for i in range(len(div_s)) :
        temp = []
        div_s[i] = [i for i in div_s[i] if i != 0]
        if alpha == "g" or alpha == "n" :
            temp = copy.deepcopy(div_s[i])
            for j in range(len(temp)) :
                temp[j] = chr(temp[j])
            div_s[i] = ("".join(temp))
        elif alpha == "k" :
            temp = copy.deepcopy(div_s[i])
            for j in range(len(temp)) :
                temp[j] = hex(temp[j])[2:]
            temp = list_chunk(temp,2)
            for j in range(len(temp)) :
                temp[j] = "".join(temp[j])
                temp[j] = int(temp[j],16)
                temp[j] = chr(temp[j])
            div_s[i] = "".join(temp)
    res = "".join(div_s)
    return res

while True :
    inputs = input("입력 :")
    enc_res = enc(inputs)
    print(enc_res)
    dec_res = dec(enc_res)
    print(dec_res)