
import re

s = "ghdwpaks    홍제만 ghdwpaks 홍제만"




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
        temp_res = list(temp_res)
        temp_res.insert(0,"g")
        temp_res = "".join(temp_res)
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
        temp_res = list(temp_res)
        temp_res.insert(0,"k")
        temp_res = "".join(temp_res)
        dived_s[i] = (temp_res)
print("dived_s :",dived_s)

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
"홍".encode() = b'\xed\x99\x8d'
이중에서 필요 없는 것은 b , ' , \x 이다.
b'\xed\x99\x8d' 을 ed998d 로 바꿔줬다.
이런식으로 변환된다.

현재로써는 암호화가 적용되지 않은 상태이지만. 이런 예문이 완성돼서 클라이언트의 영역으로 넘어가기 전에 암호화를 반드시 시켜야한다.
.은 암호화를 할 수 없는 대상이기 때문이다.
만약 암호화 함수를 적용시키게 된다면 아마 예문만을 저장한 dived_s가 완성된 부분과
(이 부분의 결과물을 알리는)res변수가 생성 및 완성되기 전에 부분에 추가할 예정이다.



'''



