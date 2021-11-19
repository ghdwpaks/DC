
import copy


def return_isalph(w) :
    #w = "c"
    if w.isdigit() :
        return "n"
    else :
        if w.encode().isalpha():
            return "g"
        else: 
            return "k"



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


def dec(input_str,key=None) :
    #input_str ='g94c0ce0ade1452a940af00d843f50512aac9ed7bffdd6c74186516d05aadca07a1efe1337c0c43c30818a8022ef9819dac98f220a4d3615e3717bc7c0812620d'
    aes = get_key(key)

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

key = input("키 입력(안할시 기본값) :")
if key == "" or key == " " :
    key = (str(socket.gethostname()).split("-"))[1]




while True :

    inputing = "g263cf9989fa35dd411b8214b451b154ea7186829b3643114e90c143b07653ba8.k78af1637caf4c6971a18419e7fb384953880c10f9e9cece42352dbdca1b4f8ac.g83a5492f8c603a64ccaa3efc046bd44fa5f67dfb1081fd0bf7a84bf895bf2f57.k78af1637caf4c6971a18419e7fb384953880c10f9e9cece42352dbdca1b4f8ac.g7369ea85adc0ac3d33b71297f9b26d6c6f4db256bb7934e8b1fd65b12a68451b.k78af1637caf4c6971a18419e7fb384953880c10f9e9cece42352dbdca1b4f8ac"
    inputing = inputing.split(".")

    res = []
    for i in range(len(inputing)) :
        res.append(dec(inputing[i],key))
    res = ''.join(res)
    print(res)