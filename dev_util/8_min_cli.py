import socket

cli_HOST = '127.0.0.1'
cli_PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((cli_HOST, cli_PORT))
    while True:
        recvData = s.recv(1024).decode('utf-8')
        print(recvData)
        sendData = "ack"
        s.send(sendData.encode('utf-8'))