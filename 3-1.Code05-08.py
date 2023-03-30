from tkinter import *
window = Tk()

## 함수 선언 부분 ##
def  myFunc() :
    if var.get() == 1 :
        label1.configure(text = "파이썬",font = ("궁서체", 12), fg = "blue")
    elif var.get() == 2 :
        label1.configure(text = "C++",font = ("궁서체", 12), fg = "yellow")
    else :
        label1.configure(text = "Java")
    
## 메인 코드 부분 ##
var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)

label1 = Label(window, text="선택한 언어 : ", font = ("궁서체", 15),fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
