import queue
import socket
from multiprocessing import Process, Queue
import threading
cli_PORT = 9999
import time
def ip_getter(cli_HOST, *catch) :
    global cli_PORT
    #print("ip_getter cli_HOST :",cli_HOST)
    #print("ip_getter catch :",catch)
    #print(catch)
    try :
        #print(cli_HOST,"접속 시도중")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((cli_HOST, cli_PORT))
        lct = time.localtime()
        s = lct.tm_sec
        m = lct.tm_min
        h = lct.tm_hour
        print("성공함 :",str(cli_HOST)+"\t\t"+str(h)+":"+str(m)+":"+str(s))
        #ip_info_getter.put(cli_HOST)
    except :
        pass
        
def ip_shower() :
    while True :
        lct = time.localtime()
        s = lct.tm_sec
        m = lct.tm_min
        h = lct.tm_hour
        print(str(ip_info_getter.get())+"\t"+str(h)+":"+str(m)+":"+str(s))
    
def inputer() :
    s = input("입력 :")
    print("s :",s)



ip = "10.241.150.211"
#cli_HOST = '172.30.1.46'
ip = ip.split(".")
ip_info_getter = Queue()
ip_info_table = []
print("cli")

while True :
    th2 = threading.Thread(target=inputer)
    th2.start()
    try :
        ip_getter_funcs = []
        for i4 in range(256) :
            cli_HOST = ip[0]+"."+ip[1]+"."+ip[2]+"."+str(i4)
            #print("__main__ cli_HOST :",cli_HOST)
            #print("__main__ type(cli_HOST) :",type(cli_HOST))
            th = threading.Thread(target=ip_getter ,args=[cli_HOST])
            th.start()
            #ip_getter_funcs.append(Process(target=ip_getter, args=(cli_HOST)))        
    except :
        continue
