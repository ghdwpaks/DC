
import copy
from Cryptodome.Cipher import AES 
import socket
import defs

cry_ans = False
while True :
    user_ans1 = input("암호화를 사용하시겠습니까?(미입력시 비암호화연결 시도) :")

    user_ans1 = defs.get_ans_yes_or_no_or_another(user_ans1)
    if user_ans1 == 2 :
        print("다시 정상적으로 입력해주세요.")
        continue
    else :
        if user_ans1  :
            cry_ans = True
            print("암호화 연결을 시도합니다.")
            key = input("키 입력(안할시 기본값) :")
            if key == "" or key == " " :
                key = (str(socket.gethostname()).split("-"))[1]
            break
        else :
            cry_ans = False
            print("비 암호화 연결을 시도합니다.")
            break
ser_HOST = ""
keep_lv1 = True
while keep_lv1 :
    ip_recommendation = socket.gethostbyname(socket.gethostname())
    
    user_ans2 = input(str(ip_recommendation)+"으로 서버를 여시겠습니까?(미입력시 승인거부):")

    '''
    if defs.defs.get_ans_yes_or_no_or_another(user_ans2) == False :
        print("송신대기를 시작합니다.")
        keep_lv1 = False
        
    '''
    if defs.get_ans_yes_or_no_or_another(user_ans2) :
        print(str(ip_recommendation),"으로 서버를 엽니다.")
        ser_HOST=copy.deepcopy(ip_recommendation)
        keep_lv1 = False
        continue
    else :
        while True :
            user_ans_ip = input("어떤 IP로 여시겠습니까? :")
            user_ans3 = input(user_ans_ip+"로 서버를 여시겠습니까?(y/n)")
            if user_ans3 == "y" :
                print(user_ans_ip,"로의 연결확정이 확인됐습니다.")
                ser_HOST = copy.deepcopy(user_ans_ip)
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans_ip,"로의 연결 취소가 확인됐습니다.")
                continue
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue

ser_PORT = 0
keep_lv1 = True
while keep_lv1 :
    user_ans2 = input("접속을 받을 포트를 입력해주세요 :")
    if defs.get_ans_yes_or_no_or_another(user_ans2) == False :
        print("다시 입력해주세요.")
        continue
    else :
        while True :
            user_ans3 = input(str(user_ans2)+"로 연결하시겠습니까?(y/n) :")
            if user_ans3 == "y" :
                print(user_ans2,"와의 연결확정이 확인됐습니다.")
                ser_PORT = int(copy.deepcopy(user_ans2))
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans2,"와의 연결 취소가 확인됐습니다.")
                break
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue



print("ser")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ser_HOST, ser_PORT))

    s.listen(5)
    conn, addr = s.accept()


conn.sendall("연결됨".encode('utf-8'))
if cry_ans :
    while True:
        recvData = conn.recv(1024)
        print(recvData.decode('utf-8'))
        sendData = input("보내기 > ")
        #inputs : "ghdwpaks홍제만ghdwpaks"
        inputs = list(sendData)
        res = []
        stamp = 0
        for i in range(1,len(inputs)) :
            if inputs[i-1] == " " and inputs[i] == " " :
                continue
            if not defs.return_isalph(inputs[i-1]) == defs.return_isalph(inputs[i]) :
                res.append(inputs[stamp:i])
                stamp = copy.deepcopy(i)
            elif i == len(inputs) -1 :
                res.append(inputs[stamp:i+1])
        for i in range(len(res)) :
            res[i] = "".join( res[i])
        
        sending = []
        for i in range(len(res)) :
            sending.append(defs.enc(res[i],key))
        sending = '.'.join(sending)
        print(sending)
        conn.send(sending.encode('utf-8'))
else :
    while True:
        recvData = conn.recv(1024)
        print(recvData.decode('utf-8'))
        sendData = input("보내기 > ")
        if sendData == "" or sendData == None :
            sendData = " "
        conn.send(sendData.encode('utf-8'))

