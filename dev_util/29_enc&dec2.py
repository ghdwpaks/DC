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
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
def FillUp0(i,byte=4) :
    #i = 10
    i = list(i)
    while True :
        if len(i) < byte :
            i.insert(0,"0")
        else :
            break
    return "".join(i)
aes = get_key()
#[250, 140, 201, 179, 209, 19, 92, 119, 47, 175, 113, 73, 172, 81, 130, 244]
#before_l = [250, 140, 201, 179, 209, 19, 92, 119, 47, 175, 113, 73, 172, 81, 130, 244]
#before_l = [221, 53, 46, 206, 180, 166, 242, 121, 21, 51, 112, 148, 229, 199, 78, 177]
before_l = [221, 53, 46, 206, 180, 166, 242, 121, 21, 51, 112, 148, 229, 199, 78, 177]
al1 = list(aes.decrypt(bytes(before_l)))
print(al1)
aes = get_key()
al2 = list(aes.encrypt(bytes(before_l)))
print(al2)

print("\n\n\n")

s = "홍제만"
s = list(s)
div_s = []
for i in range(len(s)) :
    cc = s[i]
    od = hex(ord(cc))[2:]
    print("od :",od)
    div_s.append(od)
print("1 div_s :",div_s)
div_s = list(div_s)
div_s2 = []
for i in range(len(div_s)) :
    temp = list_chunk(list(div_s[i]),2)
    for j in range(len(temp)) :
        temp[j] = "".join(temp[j])
    
    div_s2.extend(temp)
div_s = div_s2
print("2 div_s :",div_s)
for i in range(len(div_s)) :
    temp = div_s[i]
    div_s[i] = int("0x"+temp,16)
print("3 div_s :",div_s)
for i in range((16-(len(div_s) % 16))) :
    div_s.append(0)
#div_s = div_s + (32-(len(div_s) % 32))*"0"
print("4 div_s :",div_s)
aes = get_key()
res = list(aes.encrypt(bytes(div_s)))
print("res :",res)

aes = get_key()
#채택됨
al1 = list(aes.decrypt(bytes(res)))
#채택됨
print("al1 :",al1)
al11 = list(aes.decrypt(bytes(al1)))
print("al11 :",al11)
aes = get_key()
al2 = list(aes.encrypt(bytes(res)))
print("al2 :",al2)




