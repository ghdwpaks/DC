import socket

print("ser")

ser_HOST = "127.0.0.1"
ser_PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ser_HOST, ser_PORT))

    s.listen(50)
    conn, addr = s.accept()
    '''
    s.accept() : (<socket.socket fd=324, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('10.241.150.211', 9999), raddr=('10.241.150.211', 50426)>, ('10.241.150.211', 50426))

    conn : <socket.socket fd=348, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('10.241.150.211', 9999), raddr=('10.241.150.211', 50427)>

    addr : ('10.241.150.211', 50427)
    '''


conn.sendall("연결됨".encode('utf-8'))
while True:
    recvData = conn.recv(1024)
    print(recvData.decode('utf-8'))
    sendData = input("보내기 > ")
    if sendData == "" or sendData == None :
        sendData = " "
    conn.send(sendData.encode('utf-8'))