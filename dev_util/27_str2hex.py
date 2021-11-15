"""
tech and codes from : https://www.kite.com/python/answers/how-to-convert-a-string-to-hex-in-python
"""

a = "d1"
#b = hex("0x"+a)
b = int("0x"+a,16)
print(b)
print(type(b))

hex_string = "0xAA"

an_integer = int(hex_string, 16) 

hex_value = hex(an_integer)
print(hex_value)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
lst = list("ghdwpaks")
n = 2
print("lst :",lst)
print("n :",n)
r = list_chunk(lst,n)
print(r)


print("\n\n\n\n")
print("*"*50)

s = "ghdwpaks_ghdwpaks"
print(s.find("_"))
s = s[s.find("_")+1:]+s[:s.find("_")]
print(s)

s = hex(ord("홍"))
print(s)
print(type(s))

s = chr(ord("홍"))
print(s)
print("===")
print(hex(ord("홍"))[2:])


