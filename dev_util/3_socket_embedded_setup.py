'''
https://seolin.tistory.com/97
socket 필수 기능 셋업 및 화이트박스 테스트용 파일
'''

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

clientSock, addr = serverSock.accept()