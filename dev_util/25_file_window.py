'''
https://inspireman.tistory.com/16
'''
from tkinter import Canvas, filedialog
from tkinter import messagebox

list_file = []                                          #파일 목록 담을 리스트 생성
while True :
    cannotpass = True
    
    while True :
        files = filedialog.askopenfilenames(initialdir="/",title = "파일을 선택 해 주세요",)
        print(files)
        if files == '':
            messagebox.showwarning("경고", "파일 추가를 종료합니다.")    #파일 선택 안했을 때 메세지 출력
            cannotpass = True
            break
        else : 
            continue
    if cannotpass : break
    else : continue
        
            

print(files)    #files 리스트 값 출력
#리스트 값은 튜플로 저장된다.
