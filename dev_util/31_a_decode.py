import copy 
from Cryptodome.Cipher import AES 
import socket
dec_count = 0

#ghdwpaksghdwpaksghdwpaksghdwpaksghdwpaks
input_str ='g94c0ce0ade1452a940af00d843f50512aac9ed7bffdd6c74186516d05aadca07a1efe1337c0c43c30818a8022ef9819dac98f220a4d3615e3717bc7c0812620d'


class AESCryptoCBC():
    def __init__(self, key):
        iv = bytes([0x00] * 16)
        # aes cbc 생성
        self.crypto = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, data):
        enc = self.crypto.encrypt(data)
        return enc

    def decrypt(self, enc):
        dec = self.crypto.decrypt(enc)
        return dec

def get_key(s = (str(socket.gethostname()).split("-"))[1]) : 
    real_name_multiply = (32 // len(s))+1
    real_name = (s * real_name_multiply)[:32]
    real_name = list(real_name)
    for i in range(len(real_name)) :
        real_name[i] = ord(real_name[i])
    key = copy.deepcopy(real_name)         
    aes = AESCryptoCBC(bytes(key))
    return aes
aes = get_key()
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

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
        dec_count += 1
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
print(res)
        






