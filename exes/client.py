

import copy
from Cryptodome.Cipher import AES 
import socket

import defs
key = (str(socket.gethostname()).split("-"))[1]
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
#print("IP Address(Internal) : ",socket.gethostbyname(socket.gethostname()))


cli_HOST = ""
keep_lv1 = True
while keep_lv1 :
    user_ans2 = input("접속 대상의 아이피를 입력해주세:")
    '''
    if defs.defs.get_ans_yes_or_no_or_another(user_ans2) == False :
        print("송신대기를 시작합니다.")
        keep_lv1 = False
        
    '''
    if defs.get_ans_yes_or_no_or_another(user_ans2) == False :
        print("다시 입력해주세요.")
        continue
    else :
        while True :
            user_ans3 = input(str(user_ans2)+"와 연결하시겠습니까?(y/n) :")
            if user_ans3 == "y" :
                print(user_ans2,"와의 연결확정이 확인됐습니다.")
                cli_HOST = copy.deepcopy(user_ans2)
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans2,"와의 연결 취소가 확인됐습니다.")
                break
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue

cli_PORT = 0
keep_lv1 = True
while keep_lv1 :
    user_ans2 = input("접속을 받을 포트를 입력해주세요 (미입력시 9999):")

    if user_ans2 :
        cli_PORT = 9999
        keep_lv1 = False
        continue
    else :
        while True :
            user_ans3 = input(str(user_ans2)+"로 연결하시겠습니까?(y/n) :")
            if user_ans3 == "y" :
                print(user_ans2,"와의 연결확정이 확인됐습니다.")
                cli_PORT = int(copy.deepcopy(user_ans2))
                keep_lv1 = False
                break
            elif user_ans3 == "n":
                print(user_ans2,"와의 연결 취소가 확인됐습니다.")
                break
            else :
                print("y 또는 n 만 입력해주세요.\ny는 승인이며 n은 취소입니다.")
                continue


print("cli_HOST :",cli_HOST)
print("cli_PORT :",cli_PORT)
if cry_ans :
    i = 0
    while True :
        try :

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((cli_HOST, cli_PORT))
            print("연결됨.")
            while True:
                recvData = s.recv(1024).decode('utf-8')
                #print(recvData)
                try :
                    inputing = recvData.split(".")

                    res = []
                    for i in range(len(inputing)) :
                        res.append(defs.dec(inputing[i],key))
                    res = ''.join(res)
                    print(res)
                    sendData = "ack"
                    s.send(sendData.encode('utf-8'))
                except :
                    sendData = "Failed to receive"
                    s.send(sendData.encode('utf-8'))
                    
        except :
            i += 1
            
            print(i,"회 시도 실패함.",end="\n")
            continue
else :
    print("cli")
    i = 0
    while True :
        try :

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((cli_HOST, cli_PORT))
            while True:
                recvData = s.recv(1024).decode('utf-8')
                print(recvData)
                sendData = "ack"
                s.send(sendData.encode('utf-8'))
        except :
            i += 1
            print(i,"회 연결 시도 실패함.")
            continue