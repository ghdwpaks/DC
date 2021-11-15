import copy as c
from Cryptodome.Cipher import AES 
import socket
#input_str = 'gd1c61a2f633708a7f802914917e62833.ke48319fc5fc49a26c3f03b15bc9fed26.n85f848fc121e51b5bbcf3fee8036f8da.g334f1100efa7821771efd28739c2c261'

input_str = 'g96e5cb30a9326688c33765c4f1f1a227_923ada3ab3a813cde8374b0ec74c584b.kc1a33057f1dee997893d4a2e0fbb7c90.....nad8220606e191dd5a8fffb2bb234ca00'

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



'''
이 아래 문단의 1 div_s 에 대한 영역은 '단어 단위로 분할'의 기능을 한다.
변수 내용 예시 :
1 div_s : ['gd1c61a2f633708a7f802914917e62833', 'ke48319fc5fc49a26c3f03b15bc9fed26', 'n85f848fc121e51b5bbcf3fee8036f8da', 'g334f1100efa7821771efd28739c2c261']
'''
div_s = input_str.split(".")
print("1 div_s :",div_s)
#div_s : ['gb487f142698d496b6884074f8710cfc9_42961e4edc6d1061e970c72dd24171d5', 'gb487f142698d496b6884074f8710cfc9_42961e4edc6d1061e970c72dd24171d5']


print("\n\n\n.2.\n\n\n")


'''
이 아래의 2의 부분은 div_s의 상태진단 및 인코딩 언어를 담은 글자를 삭제시키며
alpha에는 각 단어의 디코딩 형식이 어떻게 되는지에 대해 정보를 저장한다.
변수 내용 예시 :
2 div_s : ['d1c61a2f633708a7f802914917e62833', 'e48319fc5fc49a26c3f03b15bc9fed26', '85f848fc121e51b5bbcf3fee8036f8da', '334f1100efa7821771efd28739c2c261']
2 alpha : ['g', 'k', 'n', 'g']
'''
alpha = []
for i in range(len(div_s)) :
    alpha.append(div_s[i][:1])
    div_s[i] = div_s[i][1:]
print("2 div_s :",div_s)
print("2 alpha :",alpha)


print("\n\n\n.3.\n\n\n")


'''
이 아래의 3의 부분은 공백이 포함된 space_loc 변수에 관한 내용을 설정한다.
변수 내용 예시 :
3 space_loc : [33, 65, 97]
3 temp_input_str : gd1c61a2f633708a7f802914917e62833ke48319fc5fc49a26c3f03b15bc9fed26n85f848fc121e51b5bbcf3fee8036f8dag334f1100efa7821771efd28739c2c261
'''
space_loc = []
temp_input_str = c.deepcopy(input_str)
for i in range(temp_input_str.count(".")) :
    dot_loc = temp_input_str.find(".")
    space_loc.append(dot_loc-i)
    temp_input_str = list(temp_input_str)
    temp_input_str[dot_loc] = ""
    temp_input_str = "".join(temp_input_str)
print("3 space_loc :",space_loc)
print("3 temp_input_str :",temp_input_str)

print("\n\n\n.4.\n\n\n")

'''
이 아래의 4의 내용의 부분은 확장된 글자들에 관한 내용을 설정한다.
'''
print("len(div_s) :",len(div_s))
for i in range(len(div_s)) :
    print("div_s[",i,"] :",div_s[i])
    print("if '_' in div_s[i] :","_" in div_s[i])
    if "_" in div_s[i] :
        print("4 1 : ",div_s[i].split("_"))
        div_s[i] = div_s[i].split("_")
print("4 div_s :",div_s)



