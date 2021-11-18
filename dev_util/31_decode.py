import copy as c
from Cryptodome.Cipher import AES 
import socket
dec_count = 0

#ghdwpaksghdwpaksghdwpaksghdwpaksghdwpaks
input_str ='g94c0ce0ade1452a940af00d843f50512aac9ed7bffdd6c74186516d05aadca07a1efe1337c0c43c30818a8022ef9819dac98f220a4d3615e3717bc7c0812620d'





print("\n\n\n.1.\n\n\n")

'''
이 아래의 AESCryptoCBC는 암호화를 하는 부분이다.
get_key 영역은 기본적으로 사용자의 컴퓨터의 이름을 가지고 키를 반환하는 함수이다.
아무것도 넣지 않아도 괜찮지만 넣어도 상관 없다.
넣는 평문은 기본적으로 16진수가 아닌 일반적인 영어 알파벳이여도 괜찮지만 이외의것을 넣으면 안된다.
'''
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
    print("key :",key)
    aes = AESCryptoCBC(bytes(key))
    return aes
    #print("aes :",aes)
aes = get_key()

'''
list_chunk는 n변수를 따라 몇개씩 나눌건지에 대해 정하고, 나누는 함수이다.
입력예시 :
lst : ['g', 'h', 'd', 'w', 'p', 'a', 'k', 's']
n : 2
'''
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
'''
결과 예시 : [['g', 'h'], ['d', 'w'], ['p', 'a'], ['k', 's']]
'''



'''
이 아래 문단의 1 div_s 에 대한 영역은 '확장된 영역의 분할'의 기능을 한다.
alpha 변수에 '전달받은 단어의 디코딩 형식'을 저장한다.
'''

alpha = ""
div_s = c.deepcopy(input_str)
div_s = list(div_s)
alpha = div_s[0]
del div_s[0] 
div_s = list_chunk(div_s,64)
print("1 div_s :",div_s)
'''
변수 내용 예시 :
1 div_s : [['9', '4', 'c', '0', 'c', 'e', '0', 'a', 'd', 'e', '1', '4', '5', '2', 'a', '9', '4', '0', 'a', 'f', '0', '0', 'd', '8', '4', '3', 'f', '5', '0', '5', '1', '2', 'a', 'a', 'c', '9', 'e', 'd', '7', 'b', 'f', 'f', 'd', 'd', '6', 'c', '7', '4', '1', '8', '6', '5', '1', '6', 'd', '0', '5', 'a', 'a', 'd', 'c', 'a', '0', '7'], ['a', '1', 'e', 'f', 'e', '1', '3', '3', '7', 'c', '0', 'c', '4', '3', 'c', '3', '0', '8', '1', '8', 'a', '8', '0', '2', '2', 'e', 'f', '9', '8', '1', '9', 'd', 'a', 'c', '9', '8', 'f', '2', '2', '0', 'a', '4', 'd', '3', '6', '1', '5', 'e', '3', '7', '1', '7', 'b', 'c', '7', 'c', '0', '8', '1', '2', '6', '2', '0', 'd']]
'''


'''
아래 서술된 5의 영역은
들어온 모든 문자들에 대해서 복호화 과정을 거친다.
최대 32바이트, 16바이트 2세트까지 수용할 수 있다.
'''
for i in range(len(div_s)) :
    print("i :",i)
    temp = list_chunk(div_s[i],2)
    print("5 1 temp :",temp)
    #5 1 temp : [['9', '4'], ['c', '0'], ['c', 'e'], ['0', 'a'], ['d', 'e'], ['1', '4'], ['5', '2'], ['a', '9'], ['4', '0'], ['a', 'f'], ['0', '0'], ['d', '8'], ['4', '3'], ['f', '5'], ['0', '5'], ['1', '2'], ['a', 'a'], ['c', '9'], ['e', 'd'], ['7', 'b'], ['f', 'f'], ['d', 'd'], ['6', 'c'], ['7', '4'], ['1', '8'], ['6', '5'], ['1', '6'], ['d', '0'], ['5', 'a'], ['a', 'd'], ['c', 'a'], ['0', '7']]
    for j in range(len(temp)) :
        temp[j] = "".join(temp[j])
    temp_res = []
    dec = []
    for j in range(len(temp)) :
        temp[j] = int("0x"+temp[j],16)
        print("5 temp[",j,"] :",temp[j])
    print("5 3 temp :",temp)
    #5 3 temp : [148, 192, 206, 10, 222, 20, 82, 169, 64, 175, 0, 216, 67, 245, 5, 18, 170, 201, 237, 123, 255, 221, 108, 116, 24, 101, 22, 208, 90, 173, 202, 7]
    temp = list_chunk(temp , 16)
    print("5 4 temp :",temp)
    dec_temp = []
    for j in range(len(temp)) :
        print("j :",j)
        print("temp[j] :",temp[j])
        aes_dec = list(aes.decrypt(bytes(temp[j])))
        temp_dec = c.deepcopy(aes_dec)
        dec_count += 1
        print("temp_dec :",temp_dec)
        dec_temp.extend(temp_dec)
        print("dec_temp :",dec_temp)
    dec.extend(dec_temp)
    print("5 dec :",dec)
    div_s[i] = dec
    print("\n\n\n")
print("5 div_s :",div_s)
print("5 dec_count :",dec_count)
'''
5 div_s : [[103, 104, 100, 119, 112, 97, 107, 115, 103, 104, 100, 119, 112, 97, 107, 115, 103, 104, 100, 119, 112, 97, 107, 115, 103, 104, 100, 119, 112, 97, 107, 115], [103, 104, 100, 119, 112, 97, 107, 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''


'''
아래 6의 영역은 비어있는 영역을 뜻하는 0을 없애고 문자로 변환해주는 과정을 거친다.
'''

for i in range(len(div_s)) :
    temp = []
    div_s[i] = [i for i in div_s[i] if i != 0]
    if alpha == "g" or alpha == "n" :
        temp = c.deepcopy(div_s[i])
        for j in range(len(temp)) :
            temp[j] = chr(temp[j])
        div_s[i] = ("".join(temp))
    elif alpha == "k" :
        temp = c.deepcopy(div_s[i])
        for j in range(len(temp)) :
            temp[j] = hex(temp[j])[2:]
        temp = list_chunk(temp,2)
        for j in range(len(temp)) :
            temp[j] = "".join(temp[j])
            temp[j] = int(temp[j],16)
            temp[j] = chr(temp[j])
        div_s[i] = "".join(temp)
res = "".join(div_s)
print("res :",res)
        






