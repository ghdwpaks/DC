def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

print(list_chunk([1,2,3,4,5,6],2))
print(list("0ed998deca09ceba0ed998deca09ceba"))
temp = list_chunk(list("0ed998deca09ceba0ed998deca09ceba"),2)
print(temp)
for i in range(len(temp)) :
    temp[i] = "".join(temp[i])
    temp[i] = int(("0x"+temp[i]),16)
print("temp :",temp)

print("len(temp) :",len(temp))
print("hello"+(14%5)*"0")


a = "ab"
i = int(("0x"+a),16)
print(i)