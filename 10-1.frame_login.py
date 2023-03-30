from tkinter import *

ws = Tk()
ws.title('login')
#ws.geometry('940x500')
password = StringVar() #string변수 선언, tkinter함수
variable= StringVar()

def check_data():
        print(variable.get(),password.get())

# widgets
left_frame = LabelFrame(ws, bd=2, relief=SOLID, padx=10, pady=10,text="로그인정보")

Label(left_frame, text="Enter name", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Enter Password", font=('Times', 14)).grid(row=1, column=0, pady=10)
log_em = Entry(left_frame, font=('Times', 14),textvariable = variable) #한줄 입력창
log_em.insert(10, "홍길동") #엔트리 초기값 설정
log_pw = Entry(left_frame, font=('Times', 14),show="*",textvariable = password) #변수를 variable로 교체실행 확인

login_btn = Button(left_frame, width=15, text='Login', font=('Times', 14), command=check_data)

log_em.grid(row=0, column=1, pady=10, padx=20)
log_pw.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.pack()
#left_frame.place(x=50, y=50)


# infinite loop
ws.mainloop()