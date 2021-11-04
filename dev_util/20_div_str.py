
import copy
s = "ghdwpaks 홍제만홍제만홍제만홍제만홍제만홍제만 ghdwpaks 홍제만"

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
'''
import socket
socket.gethostname()
'DESKTOP-EPE6PMI'

'''
from Cryptodome.Cipher import AES 
import socket
real_name = (str(socket.gethostname()).split("-"))[1]

real_name_multiply = (32 // len(real_name))+1
real_name = (real_name * real_name_multiply)[:32]
real_name = list(real_name)
for i in range(len(real_name)) :
    real_name[i] = ord(real_name[i])
print("real_name :",real_name)
print("len(real_name) :",len(real_name))
key = copy.deepcopy(real_name)         

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
#print("1 dived_s :",dived_s)
alpha = []
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
        alpha.append(True)
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
        alpha.append(False)
        dived_s[i] = (temp_res)
print("143 dived_s :",dived_s)
'''
dived_s 259 : ['ge5c8a2991a0aebfa018a33e24fe49f44', 'k1e319151c2668319b69803d54b80933d', 'g0da63d40419246f111ab026bea6f8c8', 'ka7c951b92d38ef9bffcc18e8e2bb97d', 'd93c252a2c8c2a430ab4a177b9404fe']
dived_s 259 : ['ge5c8a2991a0aebfa018a33e24fe49f44', 'k205c98f3247cab0a7d5f60bcc07a3456', 'g2483bcfb24a41851504b9a29b7c6e0c9', 'kc1ede9dcab46ab2e14af01c5414544e2', '8204f60a68a7af1187f2c3f309d7a5a8']
'''
extend_loc = []
for i in range(len(dived_s)) :
    if len(dived_s[i]) > 32 :
        extend_loc.append(i)
        temp = copy.deepcopy(dived_s[i])
        temp = list(temp)
        temp = [temp[:31],temp[31:]]
        for j in range(len(temp)) :
            temp[j] = "".join(temp[j])
        print("temp 154 :",temp)
        del dived_s[i]
        for j in range(len(temp)) :
            dived_s.insert(i+j,temp[j])
        print("temp :",temp)
        print("dived_s :",dived_s)
print("154 2 dived_s :",dived_s)
print("154 2 extend_loc :",extend_loc)

for i in range(len(dived_s)) :
    #print("len(dived_s[",i,"]) :",len(dived_s[i]))
    #print("1 dived_s[{}] : {}".format(i,dived_s[i]))
    print("1 dived_s[i] :",dived_s[i])
    print("1 len(dived_s[i]) :",len(dived_s[i]))
    print("1 BLOCK_SIZE * 2 :",BLOCK_SIZE*2)
    print("1 ((BLOCK_SIZE*2)-(len(dived_s[i]) % (BLOCK_SIZE*2))) :",((BLOCK_SIZE*2)-(len(dived_s[i]) % (BLOCK_SIZE*2))))
    dived_s[i] =dived_s[i] + ((BLOCK_SIZE*2)-(len(dived_s[i]) % (BLOCK_SIZE*2)))*"0"
    #print("2 dived_s[{}] : {}".format(i,dived_s[i]))
    dived_s[i] = list_chunk(list(dived_s[i]),BLOCK_SIZE*2)
    #dived_s[i] = ["0ed998deca09ceba0ed998deca09ceba","78c0ed998deca09c78c0ed998deca09c"]
    print("2 dived_s[i] :",dived_s[i])
    print("2 len(dived_s[i]) :",len(dived_s[i]))
    temp = dived_s[i]
    #temp = "0ed998deca09ceba0ed998deca09ceba"

    for k in range(len(temp)) :
        temp = list(temp)
        print("143 temp :",temp)
        #temp = ['0', 'e', 'd', '9', '9', '8', 'd', 'e', 'c', 'a', '0', '9', 'c', 'e', 'b', 'a', '0', 'e', 'd', '9', '9', '8', 'd', 'e', 'c', 'a', '0', '9', 'c', 'e', 'b', 'a']
        tempk = list_chunk(temp[k],2)
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
        
        res = copy.deepcopy(str(enc))
        #res : [200,182,117,166,2,34,203,255,222,183,47,150,232,132,245,75]
        res = res[1:-1]
        #res : 200,182,117,166,2,34,203,255,222,183,47,150,232,132,245,75
        print("res 1:",res)
        res = res.split(",")
        #res 2: ['200', ' 182', ' 117', ' 166', ' 2', ' 34', ' 203', ' 255', ' 222', ' 183', ' 47', ' 150', ' 232', ' 132', ' 245', ' 75']
        print("res 2:",res)
        for o in range(len(res)) :
            res[o] = str(hex(int(res[o].strip())))
        print("res 3:",res)
        print("(res[0])[2:] :",(res[0])[2:])
        res[0] = (res[0])[2:]
        print("res[0] :",res[0])
        for p in range(1,len(res)) :
            res[p] = (res[p])[2:]
            res[p] = FillUp0(res[p],2)
        print("res 4:",res)
        #print("res 3:",res)
        print("type(res) :",type(res))
        temp = "".join(res)
        print("temp :",temp)
        dived_s[i] = temp
        print("i :",i)
        print("dived_s[i] :",dived_s[i])
    print("exited")
    print("dived_s :",dived_s)
    print("dived_s[i] :",dived_s[i])
    print("len(dived_s[i]) :",len(dived_s[i]))
    print("len(dived_s[i])%32 :",len(dived_s[i])%(BLOCK_SIZE*2))


    '''
    if return_isalph(dived_s[i]) :
        dived_s[i] = list(dived_s[i])
        dived_s[i].insert(0,"g")
        dived_s[i] = "".join(dived_s[i])
    else :
        dived_s[i] = list(dived_s[i])
        dived_s[i].insert(0,"k")
        dived_s[i] = "".join(dived_s[i])
    '''

print("final exited")
print("dived_s :",dived_s)
for i in range(len(alpha)) :
    dived_s[i] = list(dived_s[i])
    if alpha[i] :
        dived_s[i].insert(0,"g")
    else :
        dived_s[i].insert(0,"k")
    dived_s[i] = "".join(dived_s[i])
        
print("dived_s 259 :",dived_s)
print("\n\n\n")
for i in range(len(extend_loc)-1,0,-1) :
    print("257 i :",i)
    print("extend_loc[i] :",extend_loc[i])
    temp = '_'.join([dived_s[i],dived_s[i+1]])
    print("temp :",temp)
    del dived_s[extend_loc[i]]
    dived_s.insert(extend_loc[i]-1,temp)
    print("dived_s :",dived_s)


res = ""
for i in range(len(blank_loc)) :
    res += dived_s[i]
    for j in range(blank_loc[i]) :
        res += "."  
res += dived_s[-1]
print("res :",res)
print(alpha)

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

'''



