
import copy
from Cryptodome.Cipher import AES 
import socket
enc_count = 0
while True :
    print("\n\n")
    s = input("입력 : ")

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
    def get_key(s = (str(socket.gethostname()).split("-"))[1]) : 
        
        #real_name : HCB8KMM
        real_name_multiply = (32 // len(s))+1
        real_name = (s * real_name_multiply)[:32]
        real_name = list(real_name)
        for i in range(len(real_name)) :
            real_name[i] = ord(real_name[i])
        key = copy.deepcopy(real_name)         
        print("key :",key)
        aes = AESCryptoCBC(bytes(key))
        return aes
        print("aes :",aes)
    aes = get_key()      
    
    dived_s = copy.deepcopy(s)
    s = list(s)
    temp = [s[0]]
    '''
    return_isalph 함수는 숫자인것,영어인것, 영어가 아닌것을 구분한다.
    number의 n
    english 의 g
    korean 의 k
    을 모티브로 작성하였다.
    english의 앞글자인 e를 쓰지 않는 이유는
    e가 16진수에도 포함되어있기 때문에 헷갈리지 않기 위해서이다.

    The return_isalph function distinguishes between numbers, English, and non-English.
    n of number
    g of english 
    k of korean 
    It was written with the motif of.
    The reason why I don't use the first letter of English, e,
    This is to avoid confusion because e is also included in hexadecimal numbers.
    '''
    def return_isalph(w) :
        #w = "c"
        if w.isdigit() :
            return "n"
        else :
            if w.encode().isalpha():
                return "g"
            else: 
                return "k"

    '''
    fillup0는 문자열에서 0을 채워주는 함수이다.
    예를 들어, 32bit의 특정할 길이의 문자열이 필요한데 길이가 부족할경우
    32까지 부족한 부분은 0으로 채워준다.
    안에 들어가는 byte라는 숫자보다 길이가 길면 아무것도 반환하지 않는다.
    들어가는 형식은 문자열 형식 이여야만 한다.

    Fillup0 is a function that fills the string with zero.
    For example, if you need a string of a specific length of 32 bits, but the length is insufficient,
    Fill the deficiencies up to 32 with zero.
    If the length is longer than the number byte inside, nothing is returned.
    The format that goes in must be in the form of a string.
    '''
    def FillUp0(i,byte=4) :
        #i = 10
        i = list(i)
        while True :
            if len(i) < byte :
                i.insert(0,"0")
            else :
                break
        return "".join(i)
    dived_s = list(dived_s)
    print("1 dived_s :",dived_s)

    alpha = return_isalph(dived_s[0])
    print("110 alpha :",alpha)
    temp_res = []
    for i in range(len(dived_s)) :
        if 'g' == alpha:
            dived_s[i] = ord(dived_s[i])
        elif 'k' == alpha :
            print("116 dived_s :",dived_s)
            print(i,"j dived_s :",dived_s)
            c = dived_s[i]
            print("119 c :",c)
            od = hex(ord(c))[2:]
            print("1 od :",od)
            #1 od : d64d
            od = list(od)
            od = list_chunk(od,2)
            print("3 od :",od)
            for k in range(len(od)) :
                od[k] = "".join(od[k])
                od[k] = int("0x"+od[k], 16)
            print("2 od :",od)
            temp_res.extend(od)
    print("126 temp_res :",temp_res)
    if 'k' == alpha :
        dived_s = temp_res
    
            
        
    print("143 dived_s :",dived_s)
    '''
    143 dived_s : [103, 104, 100, 119, 112, 97, 107, 115]
    '''
    print("134 len(dived_s) :",len(dived_s))
    if len(dived_s) > 31 :
        temp = copy.deepcopy(dived_s)
        temp = list(temp)
        print("272 temp :",[temp[:31],temp[31:]])
        print("273 temp :",list_chunk(temp,32))
        temp = list_chunk(dived_s,32)
        print("140 temp:",temp)
        dived_s = copy.deepcopy(temp)
    else :
        dived_s = [dived_s]
    print("143 dived_s :",dived_s)
    '''
    143 dived_s : [[103, 104, 100, 119, 112, 97, 107, 115]]
    '''
    print("len(dived_s) :",len(dived_s))
    for i in range(len(dived_s)) :
        
        tempi = copy.deepcopy(dived_s[i])
        for j in range(32-len(tempi)) :
            tempi.append(0)
        print("tempi :",tempi)
        enc = list(aes.encrypt(bytes(tempi)))
        dived_s[i] = copy.deepcopy(enc)
    print("dived_s :",dived_s)
    for i in range(len(dived_s)) :
        for j in range(len(dived_s[i])) :
            
            dived_s[i][j] = FillUp0(hex(dived_s[i][j])[2:],2)
        dived_s[i] = "".join(dived_s[i])
    print("1 dived_s :",dived_s)
    for i in range(len(dived_s)) :
        "".join(dived_s[i])
    print("2 dived_s :",dived_s)
    res = alpha+"".join(dived_s)
    print(res)