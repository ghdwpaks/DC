s1 = "홍 ghd 제 wp 만 aks"
print("1 :",s1.encode("utf-8"))

s2 = "ㅎ"
print("2 :",s2.encode("utf-8"))
s3 = "호"
print("3 :",s3.encode("utf-8"))
s4 = "홍"
print("4 :",s4.encode("utf-8"))
print("4 :",str(s4.encode("utf-8")).encode("utf-8"))