import queue
import socket
from multiprocessing import Process, Queue
cli_PORT = 9999
import time
def ip_getter(cli_HOST) :
    global cli_PORT
    try :
        #print(cli_HOST,"접속 시도중")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((cli_HOST, cli_PORT))
        print("성공함 :",cli_HOST)
        ip_info_getter.put(cli_HOST)
    except :
        pass
        

    



ip = "192.168.1.24"
#cli_HOST = '172.30.1.46'
ip = ip.split(".")
ip_info_getter = Queue()
ip_info_table = []
print("cli")

ip_getter_funcs = []
for i4 in range(256) :
    cli_HOST = ip[0]+"."+ip[1]+"."+ip[2]+"."+str(i4)
    #print("cli_HOST :",cli_HOST)
    ip_getter_funcs.append(Process(target=ip_getter, args=(cli_HOST)))
    #ip_getter_funcs.append(cli_HOST)
    #print(i1+i2+i3+i4)
#print("ip_getter_funcs :",ip_getter_funcs)
try :
    for i in range(len(ip_getter_funcs)) :ip_getter_funcs[i].start()
    #for i in range(len(ip_getter_funcs)) :ip_getter_funcs[i].join() 
    for i in range(len(ip_getter_funcs)) :ip_getter_funcs[i].close() 
except :
    pass
