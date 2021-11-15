
import copy
from Cryptodome.Cipher import AES 
import socket
def get_key(real_name=None) :
    if real_name == None :
        real_name = (str(socket.gethostname()).split("-"))[1]
    real_name_multiply = (32 // len(real_name))+1
    real_name = (real_name * real_name_multiply)[:32]
    real_name = list(real_name)
    for i in range(len(real_name)) :
        real_name[i] = ord(real_name[i])
    key = copy.deepcopy(real_name)  
    return key

def encode(s,key=None) :
    if s == "" : s = "0"
    def list_chunk(lst, n):
            return [lst[i:i+n] for i in range(0, len(lst), n)]
    BLOCK_SIZE=16

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
       
    key = get_key(key)
    aes = AESCryptoCBC(bytes(key))
    space_bar_loc = []
    scount = s.count(" ")
    for i in range(scount) :
        space_bar_loc.append(s.find(" "))
        s = "".join([s[:s.find(" ")],s[s.find(" ")+1:]])
    space_bar_loc_set = set(space_bar_loc)
    space_bar_loc_set = list(space_bar_loc_set)
    blank_loc = []
    for i in range(len(space_bar_loc_set)) :
        blank_loc.append(0)
        blank_loc[i] += space_bar_loc.count(space_bar_loc_set[i])
    dived_s = []
    s = list(s)
    temp = [s[0]]
    def return_isalph(w) :
        if w.isdigit() :return "n"
        else :
            if w.encode().isalpha():return "g"
            else: return "k"
    def FillUp0(i,byte=4) :
        #i = 10
        i = list(i)
        while True :
            if len(i) < byte :i.insert(0,"0")
            else :break
        return "".join(i)
    for i in range(1,len(s)) :
        iisalpha = return_isalph(s[i])
        tisalpha = return_isalph("".join(temp))
        if iisalpha == tisalpha :
            temp.append(s[i])
            if i == len(s)-1 : dived_s.append("".join(temp))
        else :
            dived_s.append("".join(temp))
            temp = [s[i]]
    alpha = []
    for i in range(len(dived_s)) :
        if 'g' == return_isalph(dived_s[i]):
            temp = []
            for j in range(len(dived_s[i])) :
                temp.append(str(hex(ord(dived_s[i][j])))[2:])
            temp_res = "".join(temp)
            alpha.append('g')
            dived_s[i] = (temp_res)

        elif 'n' == return_isalph(dived_s[i]) :
            temp = []
            for j in range(len(dived_s[i])) :
                temp.append(str(hex(ord(dived_s[i][j])))[2:])
            temp_res = "".join(temp)
            alpha.append('n')
            dived_s[i] = (temp_res)
        elif 'k' == return_isalph(dived_s[i]) :
            temp = []
            for j in range(len(dived_s[i])) :
                string = str(str(dived_s[i][j]).encode("utf-8"))
                ##print(string)

                characters = "\\x'"
                for x in range(len(characters)):
                    string = (string.replace(characters[x],""))
                temp.append(string[1:])
            temp_res = "".join(temp)
            alpha.append('k')
            dived_s[i] = (temp_res)
    extend_loc = []
    for i in range(len(dived_s)) :
        if len(dived_s[i]) > 31 :
            extend_loc.append(i)
            temp = copy.deepcopy(dived_s[i])
            temp = list(temp)
            temp = [temp[:31],temp[31:]]
            for j in range(len(temp)) :
                temp[j] = "".join(temp[j])
            del dived_s[i]
            for j in range(len(temp)) :
                dived_s.insert(i+j,temp[j])
    for i in range(len(dived_s)) :
        dived_s[i] =dived_s[i] + ((BLOCK_SIZE*2)-(len(dived_s[i]) % (BLOCK_SIZE*2)))*"0"
        dived_s[i] = list_chunk(list(dived_s[i]),BLOCK_SIZE*2)
        temp = dived_s[i]

        for k in range(len(temp)) :
            temp = list(temp)
            tempk = list_chunk(temp[k],2)
            for m in range(len(tempk)) :
                tempk[m] = "".join(tempk[m])
                tempk[m] = int(("0x"+tempk[m]),16)
            enc = list(aes.encrypt(bytes(tempk)))
            
            res = copy.deepcopy(str(enc))
            res = res[1:-1]
            res = res.split(",")
            for o in range(len(res)) :
                res[o] = str(hex(int(res[o].strip())))
            res[0] = (res[0])[2:]
            for p in range(1,len(res)) :
                res[p] = (res[p])[2:]
                res[p] = FillUp0(res[p],2)
            temp = "".join(res)
            dived_s[i] = temp
    for i in range(len(extend_loc)) :
        temp = '_'.join([dived_s[extend_loc[i]-i],dived_s[(extend_loc[i]+1)-i]])
        del dived_s[extend_loc[i]-i]
        del dived_s[extend_loc[i]-i]
        dived_s.insert(extend_loc[i]-i,temp)
    for i in range(len(alpha)) :
        dived_s[i] = list(dived_s[i])
        dived_s[i].insert(0,alpha[i])
        dived_s[i] = "".join(dived_s[i])
    res = ""
    for i in range(len(blank_loc)) :
        res += dived_s[i]
        for j in range(blank_loc[i]) :
            res += "."  
    res += dived_s[-1]
    print(res)

while True :
    s = input("입력 >")
    encode(s)