import os
import socket
import copy as c
import threading
import time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("pwnbit.kr",443))

def get_user_ans(s,y="승인됐습니다.",n="거부됐습니다.") :
    while True :
        user_ans1 = input(str(s)+"(y/n) :")
        if user_ans1 == "y" or user_ans1 == "Y" :
            print(y)
            return True
        elif user_ans1 == "n" or user_ans1 == "N" :
            print(n)
            return False
        else :
            print("y 또는 n 중에 하나만 입력해주세요.")
            continue

def inputer() :
    while True :
        s = input("입력 :")
        if s == "s" :
            print("서버를 엽니다.")
            os.system("start python server.py")
        elif s == "c" :
            print("클라이언트를 엽니다.")
            os.system("start python client.py")
        else :
            print(last_prints)
        
         

def ip_getter(cli_HOST, *catch) :
    global uport
    #print("ip_getter cli_HOST :",cli_HOST)
    #print("ip_getter catch :",catch)
    #print(catch)
    try :
        #print(cli_HOST,"접속 시도중")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((cli_HOST, uport))
        s.connect((cli_HOST, 7904))
        lct = time.localtime()
        s = lct.tm_sec
        m = lct.tm_min
        h = lct.tm_hour
        add_prints = ""
        if str(cli_HOST) == str(inside_ip) :
            add_prints = "(자신)"
        print("\n확인됨 :",str(cli_HOST)+add_prints+"\t\t"+str(h)+":"+str(m)+":"+str(s),"\n입력 :",end="")
        #ip_info_getter.put(cli_HOST)
    except :
        pass

banner = """
환영합니다.
현재 상테애서는 자신이 속한 내부 네트워크에 어떤 사람들이 통신준비가 되어있는지
또는, 통신을 하고있는지 확인할 수 있습니다.
포트포워딩을 통하여 자신이 원하는 만큼 통신 범위를 넓히는 방법도 있으나 이 방법은 권장하지 않습니다.

자신의 아이피를 입력해주시고 프로그램을 본격적으로 시작해주세요.
"""
print("\n\n\n")
print(banner)
inside_ip = sock.getsockname()[0]
uip = ""
uport = 0
while True :
    user_ip = input("IP 입력(기본값 :"+str(inside_ip)+") : ")
    if user_ip == "" :
        print("기본값인 "+str(inside_ip)+" 로 설정합니다.")
        uip = c.deepcopy(str(inside_ip))
        break
    else :
        ip_userans = get_user_ans(str(user_ip)+"로 연결하시겠습니까?")
        if ip_userans :
            uip = c.deepcopy(user_ip)
            break
        else : 
            continue

print("\n\n\n")
while True :
    user_port = input("연결 포트(기본값 :9999) :")
    if user_port == "" :
        print("기본값인 9999 로 설정합니다.")
        uport = 9999
        break
    else :
        ip_userans2 = get_user_ans(str(user_port)+"로 연결하시겠습니까?")
        if ip_userans2 :
            uport = c.deepcopy(int(user_port))
            break
        else : 
            continue

print("\n\n\n")

print("마지막으로 본격적으로 프로그램을 시작하기 전에 마지막으로 알려드리겠습니다.")
last_prints = """
이 프로그램은 기본적으로 멀티 쓰레드를 지원하기 때문에
어떠한 순간에도 입력을 할 수 있습니다.
c 는 클라이언트를 열고
s 는 본인의 서버를 엽니다.

열어놓은 서버나 클라이언트를 종료시키려면 그냥 창을 끄면 됩니다.

클라이언트는 '접속자'로써 사실상 몇개를 만들던간에 상관 없으며
서버는 '생성자'로써 단 한개만 생성할 수 있음을 알려드립니다.

이 다음 과정에서는 별 다른 안내 없이 설정된 네트워크 정보와
접속 가능한 아이피를 알려줍니다.
다만, 포트마저 변경된 경우에는 찾을 수 없을 수도 있습니다.

이 안내문이 다시 보고싶으시면 s, c이외에 아무거나 치면 나옵니다.
"""
print(last_prints)
passing = input("준비 되셨으면 아무 키를 입력해주세요.")



print("\n\n\n")
usp = uip.split(".") # uip splited "."
info_prints = """
최종적인 설정은 다음과 같습니다.
수색 범위 : \t\t{}
사용자 서버 아이피 : \t{}
사용자 연결 포트 : \t{}
""".format(str(usp[0])+"."+str(usp[1])+"."+str(usp[2])+".0 ~ "+str(usp[0])+"."+str(usp[1])+"."+str(usp[2])+".255",uip,uport)
print(info_prints)

ip_getter_th = []
while True :
    th2 = threading.Thread(target=inputer)
    th2.start()
    try :
        ip_getter_funcs = []
        for i4 in range(256) :
            cli_HOST = usp[0]+"."+usp[1]+"."+usp[2]+"."+str(i4)
            #print("__main__ cli_HOST :",cli_HOST)
            #print("__main__ type(cli_HOST) :",type(cli_HOST))
            th = threading.Thread(target=ip_getter ,args=[cli_HOST])
            th.start()
            ip_getter_th.append(th)
            #ip_getter_funcs.append(Process(target=ip_getter, args=(cli_HOST)))        
        #print("p1")
        for i4 in range(256) :
            ip_getter_th[i4].join()
        #print("p3")
        for i4 in range(256) :
            del ip_getter_th[0]
        #print("p4")
    except :
        continue
