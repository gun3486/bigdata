from tkinter import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "입력된 값 : ")
label1.pack()

label2 = Label(window, text = "입력된 값 : ")
label2.pack()

# simpledialog 모듈에는 숫자(askinteger), 문자열(asksrting), 실수(askflaot)를 입력받을 수 있음.
# askinteger() 타이틀, 내용, 입력창이 출력된다.
value = askinteger("확대 배수", "주사위 숫자(1~6)을  입력하세요", minvalue = 1, maxvalue = 6) #정수 입력
label1.configure(text = str(value))
# configure() 변경하고자 하는 내용의 값을 바꾼다.
value2 = askstring("이름", "이름을 입력하세요")
label2.configure(text =value2)
window.mainloop()
