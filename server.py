import socket

ser_HOST = '172.30.1.46'
ser_PORT = 9999

print("ser")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ser_HOST, ser_PORT))

    s.listen(5)
    conn, addr = s.accept()


conn.sendall("연결됨".encode('utf-8'))
while True:
    recvData = conn.recv(1024)
    print(recvData.decode('utf-8'))
    sendData = input("보내기 > ")
    if sendData == "" or sendData == None :
        sendData = " "
    conn.send(sendData.encode('utf-8'))