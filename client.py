import socket

print("cli")

cli_HOST = "127.0.0.1"
cli_PORT = 9999

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
        print(i,"회 시도 실패함.")
        continue