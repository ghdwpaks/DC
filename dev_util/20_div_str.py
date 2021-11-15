
import copy
from Cryptodome.Cipher import AES 
import socket
while True :
    '''
    s = "ghdwpaks 123     홍제만홍제만홍제만홍제만홍제만홍제만 ghdwpaks 홍제만"
    print(s)
    '''
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
    '''
    import socket
    socket.gethostname()
    'DESKTOP-EPE6PMI'

    '''

    '''
    이 아래 real_name을 다루는 섹션이 암호 키를 다루는 섹션이다.
    real_name에는 어찌됐든 HCB8KM 같은 문자열이 들어가면 된다.
    16진수가 아니여도 돼지만, 내용에 한글을 넣으면 안된다.
    길이는 상관 없다.

    Below, the section dealing with real_name is the section dealing with encryption keys.
    Real_name can contain strings such as HCB8KM anyway.
    It doesn't have to be hexadecimal, but you shouldn't put Korean in the content.
    The length doesn't matter.

    43 real_name : HCB8KMM

    '''
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

    '''
    이 아래에서는 평문을 나누고
    숫자와 영어, 영어가 아닌 문자들을 구분한다.
    사실 숫자와 영어는 아스키코드로 묶고 풀며
    영어가 아닌(한국어, 일본어, 러시아어 등등)은 UTF-8을 통해 묶고 푼다.
    space_bar_loc와 blank_loc에는 아래와 같은 예시의 데이터들이 저장된다.

    We're going to divide the plain text.
    Separate numbers from non-English characters.
    Actually, I tied numbers and English numbers together and solved them.
    Non-English (Korean, Japanese, Russian, etc.) is grouped and loosened through UTF-8.
    Data of the following examples are stored in space_bar_loc and blank_loc.

    space_bar_loc : [8, 11, 11, 11, 11, 11, 29, 37]
    blank_loc : [1, 1, 5, 1]

    '''

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
        
    print("88 s :",s)
    for i in range(1,len(s)) :
        iisalpha = return_isalph(s[i])
        tisalpha = return_isalph("".join(temp))
        #print("s[i] :",s[i])
        print("iisalpha :",iisalpha)

        #print("''.join(temp) :","".join(temp))
        print("tisalpha :",tisalpha)
        print("iisalpha == tisalpha  :",iisalpha == tisalpha )
        if iisalpha == tisalpha :
            temp.append(s[i])
            if i == len(s)-1 : dived_s.append("".join(temp))
        else :
            dived_s.append("".join(temp))
            temp = [s[i]]
        #print("\n\n\n")
    print("1 dived_s :",dived_s)

    '''
    이 시점에서의 'dived_s' 변수의 예시는 다음과 같다.
    The following are examples of 'dived_s' variables in this point.
    1 dived_s : ['ghdwpaks', '123', '홍제만홍제만홍제만홍제만홍제만홍제만', 'ghdwpaks', '홍제만']
    '''
    alpha = []
    for i in range(len(dived_s)) :
        if 'g' == return_isalph(dived_s[i]):
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
            alpha.append('g')
            dived_s[i] = (temp_res)

        elif 'n' == return_isalph(dived_s[i]) :
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
            alpha.append('n')
            dived_s[i] = (temp_res)
        elif 'k' == return_isalph(dived_s[i]) :
            temp = []
            for j in range(len(dived_s[i])) :
                c = dived_s[i][j]
                #c : "만"
                od = hex(ord(c))[2:]
                #od : b64d
                temp.append(od)
                #appending : b64d
                '''
                #dived_s[i] = dived_s[i].encode("utf-8")
                #(str(dived_s[i][j]).encode("utf-8"))
                print("219 dived_s[i] :",dived_s[i])
                #219 dived_s[i] : 홍제만
                print("220 dived_s[i][j] : ",dived_s[i][j])
                #220 dived_s[i][j] :  만

                string = str(str(dived_s[i][j]).encode("utf-8"))
                print("1 string :",string)
                #string : b'\xeb\xa7\x8c'
                characters = "\\x'"
                #print(characters)
                for x in range(len(characters)):
                    string = (string.replace(characters[x],""))
                print("2 string :",string)
                #2 string : beba78c
                temp.append(string[1:])
                #appending : eba78c
                #print("temp :",temp)
                '''
            temp_res = "".join(temp)
            '''
            temp_res = list(temp_res)
            temp_res.insert(0,"k")
            temp_res = "".join(temp_res)
            '''
            alpha.append('k')
            dived_s[i] = (temp_res)
    print("143 dived_s :",dived_s)
    '''
    143 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    '''
    '''
    위에 부분에서 아스키코드로 풀거나, UTF-8을 따른 유니코드로 풀어냈다.
    'alpha'라는 변수에 이렇게 단어들을 풀어내기 직전에, 한글인지 숫자인지 영어인지를 구분하여 정보를 저장한다.

    'extend_loc'와 관련된 문단은 256bit 이상을 암호화 또는 복호화를 할 수 없는 aes265을 위해서 길이가 초과된 단어들을 이어주는 언더바의 위치를 삽입해주는 위치를 알려주는 역할을 수행하는 'extend_loc' 변수를 설정하는 문단이다.

    '''
    extend_loc = []
    for i in range(len(dived_s)) :
        if len(dived_s[i]) > 31 :
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
    '''
    154 2 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    154 2 extend_loc : [2, 3, 4]
    '''
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
        exited
        dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
        dived_s[i] : 366b49f2ee3f22fb063465d8b6baef3c
        len(dived_s[i]) : 32
        len(dived_s[i])%32 : 0
        dived_s 259 : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
        extend_loc : [2, 3, 4]
        '''

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

            
    print("dived_s 259 :",dived_s)
    print("extend_loc :",extend_loc) 
    '''
    dived_s 259 : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    extend_loc : [2, 3, 4]
    '''
    '''
    extend_loc 변수가 활용되는 이 바로 아래의 문단은 확장됐던 각 부분들을 다시 언더바로 이어주는 곳이다.
    The paragraph right below, where the extended_loc variable is used, is where each part that has been expanded connects to the underbar again.

    '''
    print("\n\n\n")
    for i in range(len(extend_loc)) :
        print("257 i :",i)
        print("extend_loc[i] :",extend_loc[i])
        temp = '_'.join([dived_s[extend_loc[i]-i],dived_s[(extend_loc[i]+1)-i]])
        del dived_s[extend_loc[i]-i]
        del dived_s[extend_loc[i]-i]
        dived_s.insert(extend_loc[i]-i,temp)
        print("temp :",temp)
        
        print("dived_s :",dived_s)
    '''
    dived_s와 alpha가 활용되는 이 바로 아래의 문단은 각각의 단어들의 인코딩 또는 디코딩 형식을 지정해주고, 마지막으로 상대에게 보낼 문장 부분을 포장하는 곳이다.

    The paragraph right below, where divided_s and alpha are utilized, specifies the encoding or decoding format of each word and finally packs the sentence portion to be sent to the other person.
    '''
    print("final exited")
    print("dived_s :",dived_s)
    for i in range(len(alpha)) :
        dived_s[i] = list(dived_s[i])
        print("alpha[",i,"] :",alpha[i])
        dived_s[i].insert(0,alpha[i])
        dived_s[i] = "".join(dived_s[i])
    print("="*20)
    print("281 dived_s :",dived_s)
    print("="*20)
    res = ""
    for i in range(len(blank_loc)) :
        res += dived_s[i]
        for j in range(blank_loc[i]) :
            res += "."  
    res += dived_s[-1]
    print(res)
    print("alpha :",alpha)
    #s = "ghdwpaks 123 홍제만홍제만홍제만홍제만홍제만홍제만 ghdwpaks 홍제만"
    '''
    281 dived_s : ['gd1c61a2f633708a7f802914917e62833', 'n6df2938405ff970dad859019c4552602', 'k6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213', 'gd82c84bbd9b7f4938daff2cebafcc213', 'k898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']


    iisalpha == tisalpha  : True
    1 dived_s : ['ghdwpaks', '123', '홍제만홍제만홍제만홍제만홍제만홍제만', 'ghdwpaks', '홍제만']
    143 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c']
    temp : ['ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c']
    temp : ['ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c']
    temp : ['a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    154 2 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    154 2 extend_loc : [2, 3, 4]
    1 dived_s[i] : 6768647770616b73

    dived_s 259 : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7','87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']




    257 i : 2
    extend_loc[i] : 4
    temp : d82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4', '898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    257 i : 1
    extend_loc[i] : 3
    temp : 6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', '6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    final exited
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', '6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    alpha[ 0 ] : g
    alpha[ 1 ] : n
    alpha[ 2 ] : k
    alpha[ 3 ] : g
    alpha[ 4 ] : k
    ====================
    281 dived_s : ['gd1c61a2f633708a7f802914917e62833', 'n6df2938405ff970dad859019c4552602', 'k6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213', 'gd82c84bbd9b7f4938daff2cebafcc213', 'k898d5f9c69e314935864046ca36137b4', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    ====================
    res : gd1c61a2f633708a7f802914917e62833.n6df2938405ff970dad859019c4552602.k6df2938405ff970dad859019c4552602_d82c84bbd9b7f4938daff2cebafcc213.gd82c84bbd9b7f4938daff2cebafcc213.366b49f2ee3f22fb063465d8b6baef3c
    alpha : ['g', 'n', 'k', 'g', 'k']


    dived_s 259 : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213', '898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    extend_loc : [2, 3, 4]




    257 i : 0
    extend_loc[i] : 2
    temp : d82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4', '6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    257 i : 1
    extend_loc[i] : 3
    temp : d82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7', '87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    257 i : 2
    extend_loc[i] : 4
    temp : d82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7_87be00c786c23bcba2730816edb95e62
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7_87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    final exited
    dived_s : ['d1c61a2f633708a7f802914917e62833', '6df2938405ff970dad859019c4552602', 'd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7_87be00c786c23bcba2730816edb95e62', '7a2c72be86c1951299e3d7c451e9ca28', '366b49f2ee3f22fb063465d8b6baef3c']
    alpha[ 0 ] : g
    alpha[ 1 ] : n
    alpha[ 2 ] : k
    alpha[ 3 ] : g
    alpha[ 4 ] : k
    ====================
    281 dived_s : ['gd1c61a2f633708a7f802914917e62833', 'n6df2938405ff970dad859019c4552602', 'kd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7_87be00c786c23bcba2730816edb95e62', 'g7a2c72be86c1951299e3d7c451e9ca28', 'k366b49f2ee3f22fb063465d8b6baef3c']
    ====================
    res : gd1c61a2f633708a7f802914917e62833.n6df2938405ff970dad859019c4552602.kd82c84bbd9b7f4938daff2cebafcc213_898d5f9c69e314935864046ca36137b4_6ec4673d5c8e55d78b629190e90bb7f7_87be00c786c23bcba2730816edb95e62.g7a2c72be86c1951299e3d7c451e9ca28.k366b49f2ee3f22fb063465d8b6baef3c
    alpha : ['g', 'n', 'k', 'g', 'k']



    143 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c']
    temp : ['ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c']
    temp : ['ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced998deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    temp 154 : ['a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c']
    temp : ['a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c']
    dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    154 2 dived_s : ['6768647770616b73', '313233', 'ed998deca09ceba78ced998deca09ce', 'ba78ced998deca09ceba78ced998dec', 'a09ceba78ced998deca09ceba78ced9', '98deca09ceba78c', '6768647770616b73', 'ed998deca09ceba78c']
    154 2 extend_loc : [2, 3, 4]


    '''
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



