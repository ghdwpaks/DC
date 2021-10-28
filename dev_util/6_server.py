import socket

HOST = '127.0.0.1'
PORT = 9999

def connSocket():
   global conn, addr
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s.bind((HOST, PORT))
      s.listen(1)
      conn, addr = s.accept()
      return addr

if __name__ == '__main__':
   print('%d번 포트 접속 대기중..' % PORT)
   connSocket()
   sendData = '%s님 접속.' % addr[0]
   conn.sendall(sendData.encode('utf-8'))
   while True:
      recvData = conn.recv(1024)
      print(recvData.decode('utf-8'))
      sendData = input("보내기 > ")
      conn.send(sendData.encode('utf-8'))