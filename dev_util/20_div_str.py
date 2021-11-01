
import re

s = "ghdwpaks    홍제만 ghdwpaks 홍제만"

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

from Cryptodome import Random   
from Cryptodome.Cipher import AES 
key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D, 0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6,0xA7, 0x6E, 0xE6, 0xE5, 0x3F]
aes = AESCryptoCBC(bytes(key))
print("aes :",aes)


space_bar_loc = []
scount = s.count(" ")
for i in range(scount) :
    print("i :",i)
    print("s :",s)
    space_bar_loc.append(s.find(" "))
    s = "".join([s[:s.find(" ")],s[s.find(" ")+1:]])
print("s :",s)
print("space_bar_loc :",space_bar_loc)
space_bar_loc_set = set(space_bar_loc)
space_bar_loc_set = list(space_bar_loc_set)
blank_loc = []
for i in range(len(space_bar_loc_set)) :
    blank_loc.append(0)
    blank_loc[i] += space_bar_loc.count(space_bar_loc_set[i])

print("blank_loc :",blank_loc)

dived_s = []
s = list(s)
temp = [s[0]]

def return_isalph(w) :
    if w.encode().isalpha(): return True
    else: return False

def FillUp0(i,byte=4) :
    #i = 10
    i = list(i)
    while True :
        if len(i) < byte :
            i.insert(0,"0")
        else :
            break
    return "".join(i)
    

for i in range(1,len(s)) :
    iisalpha = return_isalph(s[i])
    tisalpha = return_isalph("".join(temp))
    #print("s[i] :",s[i])
    #print("iisalpha :",iisalpha)

    #print("''.join(temp) :","".join(temp))
    #print("tisalpha :",tisalpha)
    #print("iisalpha == tisalpha  :",iisalpha == tisalpha )
    if iisalpha == tisalpha :
        temp.append(s[i])
        if i == len(s)-1 : dived_s.append("".join(temp))
    else :
        dived_s.append("".join(temp))
        temp = [s[i]]
    #print("\n\n\n")
#print("dived_s :",dived_s)

for i in range(len(dived_s)) :
    if return_isalph(dived_s[i]) :
        temp = []
        for j in range(len(dived_s[i])) :
            #print("hex(ord(dived_s[i][j])) :",hex(ord(dived_s[i][j])))
            temp.append(str(hex(ord(dived_s[i][j])))[2:])
        temp_res = "".join(temp)
        '''
        temp_res = list(temp_res)
        temp_res.insert(0,"g")
        temp_res = "".join(temp_res)
        '''
        dived_s[i] = (temp_res)
    else :
        temp = []
        for j in range(len(dived_s[i])) :
            #dived_s[i] = dived_s[i].encode("utf-8")
            #(str(dived_s[i][j]).encode("utf-8"))
            string = str(str(dived_s[i][j]).encode("utf-8"))
            #print(string)

            characters = "\\x'"
            #print(characters)
            for x in range(len(characters)):
                string = (string.replace(characters[x],""))
            temp.append(string[1:])
            #print("temp :",temp)
        temp_res = "".join(temp)
        '''
        temp_res = list(temp_res)
        temp_res.insert(0,"k")
        temp_res = "".join(temp_res)
        '''
        dived_s[i] = (temp_res)
print("dived_s :",dived_s)

for i in range(len(dived_s)) :
    #print("len(dived_s[",i,"]) :",len(dived_s[i]))
    #print("1 dived_s[{}] : {}".format(i,dived_s[i]))
    dived_s[i] =dived_s[i] + (len(dived_s[i]) % (BLOCK_SIZE*2))*"0"
    print("dived_s[i] :",dived_s[i])
    print("len(dived_s[i]) :",len(dived_s[i]))
    print("len(dived_s[i])%16 :",len(dived_s[i])%(BLOCK_SIZE*2))
    #print("2 dived_s[{}] : {}".format(i,dived_s[i]))
    
    dived_s[i] = list_chunk(list(dived_s[i]),BLOCK_SIZE*2)
    #dived_s[i] = ["0ed998deca09ceba0ed998deca09ceba","78c0ed998deca09c78c0ed998deca09c"]
    for j in range(len(dived_s[i])) :
        temp = dived_s[i][j]
        #temp = "0ed998deca09ceba0ed998deca09ceba"
        for k in range(len(temp)) :
            temp = list(temp)
            #temp = ['0', 'e', 'd', '9', '9', '8', 'd', 'e', 'c', 'a', '0', '9', 'c', 'e', 'b', 'a', '0', 'e', 'd', '9', '9', '8', 'd', 'e', 'c', 'a', '0', '9', 'c', 'e', 'b', 'a']
            tempk = list_chunk(temp,2)
            #tempk = [['0', 'e'], ['d', '9'], ['9', '8'], ['d', 'e'], ['c', 'a'], ['0', '9'], ['c', 'e'], ['b', 'a'], ['0', 'e'], ['d', '9'], ['9', '8'], ['d', 'e'], ['c', 'a'], ['0', '9'], ['c', 'e'], ['b', 'a']]
            print("145 tempk :",tempk)
            for m in range(len(tempk)) :
                print("1 tempk[m] :",tempk[m])
                tempk[m] = "".join(tempk[m])
                print("2 tempk[m] :",tempk[m])
                tempk[m] = int(("0x"+tempk[m]),16)
                print("tempk[m] :",tempk[m])
            #tempk =  [14, 217, 152, 222, 202, 9, 206, 186, 14, 217, 152, 222, 202, 9, 206, 186]
            print("153 tempk :",tempk)
            enc = list(aes.encrypt(bytes(tempk)))
            print("enc :",enc)
            print("type(enc[0]) :",type(enc[0]))
            enc[0] = str(enc[0])
            enc[1] = str(enc[1])
            enc[2] = str(enc[2])
            enc[3] = str(enc[3])
            enc[4] = str(enc[4])
            enc[5] = str(enc[5])
            enc[6] = str(enc[6])
            enc[7] = str(enc[7])
            enc[8] = str(enc[8])
            enc[9] = str(enc[9])
            enc[10] = str(enc[10])
            enc[11] = str(enc[11])
            enc[12] = str(enc[12])
            enc[13] = str(enc[13])
            
            enc[14] = str(enc[14])
            enc[15] = str(enc[15])
            print("enc[14] :",enc[14])
            print("enc[15] :",enc[15])
            
            res = "".join(enc)
            print("res :",res)
            temp = res
        dived_s[i][j] = temp
    dived_s[i] = "".join(dived_s[i])



    if return_isalph(dived_s[i]) :
        dived_s[i] = list(dived_s[i])
        dived_s[i].insert(0,"g")
        dived_s[i] = "".join(dived_s[i])
    else :
        dived_s[i] = list(dived_s[i])
        dived_s[i].insert(0,"k")
        dived_s[i] = "".join(dived_s[i])





res = ""
for i in range(len(blank_loc)) :
    res += dived_s[i]
    for j in range(blank_loc[i]) :
        res += "."
res += dived_s[-1]
print("res :",res)


'''
res : g6768647770616b73....ked998deca09ceba78c.g6768647770616b73.ked998deca09ceba78c
예문에 대한 설명
g 는 6768647770616b73 이 영어로 재구성을 해야한다는걸 뜻한다.(해당 문서 63행 부근의 'temp_res.insert(0,"g")' 부분)
6768647770616b73은 예문이다.
아스키코드를 16진수로 변환한 결과값이다.
g = 103
103(10진수) = 67(16진수)
이런식으로 변환된다.

예문에서의 .(온점)은 문장의 공백을 의미한다.

k 는 ed998deca09ceba78c 이 유니코드로 재구성을 해야한다는걸 뜻한다.(해당 문서 82번 행 부근의 'temp_res.insert(0,"k")' 부분)
ed998deca09ceba78c은 예문이다.
utf-8을 따라 인코딩된것을 중요 부분만 추출한것이다.
원래 예문에는 '홍' 이 있었다.
"홍".encode() = b'\ x ed \ x 99 \ x 8d'
이중에서 필요 없는 것은 b , ' , \ x 이다.
b'\ x ed \ x 99 \ x 8d' 을 ed998d 로 바꿔줬다.
이런식으로 변환된다.

현재로써는 암호화가 적용되지 않은 상태이지만. 이런 예문이 완성돼서 클라이언트의 영역으로 넘어가기 전에 암호화를 반드시 시켜야한다.
.은 암호화를 할 수 없는 대상이기 때문이다.
만약 암호화 함수를 적용시키게 된다면 아마 예문만을 저장한 dived_s가 완성된 부분과
(이 부분의 결과물을 알리는)res변수가 생성 및 완성되기 전에 부분에 추가할 예정이다.



'''



