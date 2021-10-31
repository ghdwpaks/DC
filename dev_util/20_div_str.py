
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




