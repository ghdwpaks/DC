import copy as c
from Cryptodome.Cipher import AES 
import socket
#input_str = 'gd1c61a2f633708a7f802914917e62833.ke48319fc5fc49a26c3f03b15bc9fed26.n85f848fc121e51b5bbcf3fee8036f8da.g334f1100efa7821771efd28739c2c261'

input_str ='g96e5cb30a9326688c33765c4f1f1a227_6894e7a45b772a127a01968852515d4f.kfa8cc9b3d1135c772faf7149ac5182f4.n292f030d257e2680a7526ca575b201b4'

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
이 아래 문단의 1 div_s 에 대한 영역은 '단어 단위로 분할'의 기능을 한다.
'''
div_s = input_str.split(".")
print("1 div_s :",div_s)
i = 0
while (i < len(div_s)) :
    if div_s[i] == "" or div_s[i] == None :
        del div_s[i]
    else :
        i+= 1
i = 0
#div_s : ['gb487f142698d496b6884074f8710cfc9_42961e4edc6d1061e970c72dd24171d5', 'gb487f142698d496b6884074f8710cfc9_42961e4edc6d1061e970c72dd24171d5']
'''
변수 내용 예시 :
1 div_s : ['gd1c61a2f633708a7f802914917e62833', 'ke48319fc5fc49a26c3f03b15bc9fed26', 'n85f848fc121e51b5bbcf3fee8036f8da', 'g334f1100efa7821771efd28739c2c261']
'''


print("\n\n\n.2.\n\n\n")


'''
이 아래의 2의 부분은 div_s의 상태진단 및 인코딩 언어를 담은 글자를 삭제시키며
alpha에는 각 단어의 디코딩 형식이 어떻게 되는지에 대해 정보를 저장한다.
'''
alpha = []
for i in range(len(div_s)) :
    alpha.append(div_s[i][:1])
    div_s[i] = div_s[i][1:]
print("2 div_s :",div_s)
print("2 alpha :",alpha)
'''
변수 내용 예시 :
2 div_s : ['d1c61a2f633708a7f802914917e62833', 'e48319fc5fc49a26c3f03b15bc9fed26', '85f848fc121e51b5bbcf3fee8036f8da', '334f1100efa7821771efd28739c2c261']
2 alpha : ['g', 'k', 'n', 'g']
'''

print("\n\n\n.3.\n\n\n")


'''
이 아래의 3의 부분은 공백이 포함된 space_loc 변수에 관한 내용을 설정한다.
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
'''
변수 내용 예시 :
3 space_loc : [33, 65, 97]
3 temp_input_str : gd1c61a2f633708a7f802914917e62833ke48319fc5fc49a26c3f03b15bc9fed26n85f848fc121e51b5bbcf3fee8036f8dag334f1100efa7821771efd28739c2c261
'''



print("\n\n\n.4.\n\n\n")

'''
이 아래의 4의 내용의 부분은 확장된 글자들에 관한 내용을 설정한다.
확장된 영역의 표시인 언더바(_)를 삭제하고, 이에 대한 위치를 기록하는
extended_loc 변수를 설정한다는 역할의 구역이였지만,
지금 뒤에 나오는 디코딩 영역의 논리적인 문제로 인하여 
언더바만을 삭제하는 역할의 구역으로 변경하였다.
'''
print("len(div_s) :",len(div_s))
extended_loc = []
for i in range(len(div_s)) :
    #변경 이전의 코드
    print("div_s[",i,"] :",div_s[i])
    print("if '_' in div_s[i] :","_" in div_s[i])
    if "_" in div_s[i] :
        loc = div_s[i].find("_")
        div_s[i] = list(div_s[i])
        div_s[i]  = div_s[i][loc+1:]+div_s[i][:loc]
        div_s[i] = "".join(div_s[i])
        '''
            print("4 1 : ",div_s[i].split("_"))
            temp = div_s[i].split("_")
            del div_s[i]
            print("len(temp) :",len(temp))
            for j in range(len(temp)) :
                print("j :",j)
                div_s.insert(i+j,temp[j])
                extended_loc.append(i)
        '''
print("4 div_s :",div_s)
print("4 extended_loc :",extended_loc)
'''
변수 내용 예시 :
4 div_s : ['923ada3ab3a813cde8374b0ec74c584b96e5cb30a9326688c33765c4f1f1a227', 'c1a33057f1dee997893d4a2e0fbb7c90', '6fe09159ec092503cfdac330c8c9a44a']
'''

'''
아래 서술된 5의 영역은
들어온 모든 문자들에 대해서 복호화 과정을 거친다.
최대 32바이트, 16바이트 2세트까지 수용할 수 있다.
'''
for i in range(len(div_s)) :
    print("5 i :",i)
    print("5 div_s[i] :",div_s[i])
    print("5 len(div_s[i]) :",len(div_s[i]))
    temp = list_chunk(list(div_s[i]),2)
    print("5 1 temp :",temp)
    #1 temp : [['3', '8'], ['7', '2'], ['e', '8'], ['5', '3'], ['d', 'b'], ['1', 'c'], ['3', 'b'], ['a', 'e'], ['4', '6'], ['7', '5'], ['a', '4'], ['1', 'd'], ['c', '6'], ['5', 'd'], ['9', '6'], ['c', '4']]
    for j in range(len(temp)) :
        temp[j] = "".join(temp[j])
    print("5 2 temp :",temp)
    #2 temp : ['38', '72', 'e8', '53', 'db', '1c', '3b', 'ae', '46', '75', 'a4', '1d', 'c6', '5d', '96', 'c4']
    temp_res = []
    dec = list()
    for j in range(len(temp)) :
        temp[j] = int("0x"+temp[j],16)
        print("5 temp[",j,"] :",temp[j])
    print("5 3 temp :",temp)
    dec = list(aes.decrypt(bytes(temp)))
    print("5 dec :",dec)
    div_s[i] = dec
    print("\n\n\n")
print("5 div_s :",div_s)
'''
5 div_s : [[166, 229, 203, 48, 169, 50, 102, 136, 195, 55, 101, 196, 241, 241, 162, 39, 15, 252, 131, 211, 43, 22, 65, 97, 29, 105, 242, 255, 34, 48, 54, 63], [40, 60, 228, 136, 75, 137, 76, 154, 185, 54, 243, 76, 163, 160, 255, 104], [48, 48, 50, 51, 49, 48, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''

for i in range(len(div_s)) :
    language = alpha[i]
    if language == "g" or language == "n" :
        pass
    elif language == "k" :
        temp = c.deepcopy(div_s[i])
        print("temp :",temp)
        
        






