import socket

HOST = '127.0.0.1'
PORT = 9999

def connSocket():
    global conn, addr
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("1 s:",s)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("2 s:",s)
        s.bind((HOST, PORT))
        print("3 s:",s)

        s.listen(3)
        conn, addr = s.accept()
        print(__name__,"\t conn 1:",conn)  
        print(__name__,"\t addr 1:",addr)
        return addr

if __name__ == '__main__':
    print('%d번 포트 접속 대기중..' % PORT)
    #print(__name__,"\t conn :",conn)
    #NameError: name 'conn' is not defined
    #print(__name__,"\t addr :",addr)
    #NameError: name 'addr' is not defined   
    connSocket()
    print(__name__,"\t conn 2:",conn)
    print(__name__,"\t addr 2:",addr)
    sendData = '%s님 접속.' % addr[0]
    conn.sendall(sendData.encode('utf-8'))
    while True:
        recvData = conn.recv(1024)
        print(recvData.decode('utf-8'))
        sendData = input("보내기 > ")
        conn.send(sendData.encode('utf-8'))