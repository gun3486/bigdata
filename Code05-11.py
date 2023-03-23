from tkinter import *

window = Tk()

mainMenu = Menu(window) #상위메뉴(부모)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu) #자식메뉴
mainMenu.add_cascade(label = "파일", menu = fileMenu) #상위메뉴 text
fileMenu.add_command(label = "열기",font = ("궁서체", 30))
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

window.mainloop()
