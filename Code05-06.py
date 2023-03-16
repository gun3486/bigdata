from tkinter import *
from PIL import Image, ImageTk #Pollow install
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

window = Tk()

image=Image.open("testimage2.gif")
img=image.resize((100, 100))
my_img = ImageTk.PhotoImage(img)

image=Image.open("testimage3.gif")
img=image.resize((100, 100))
my_img2 = ImageTk.PhotoImage(img)

button1 = Button(window, image = my_img, command = myFunc)
button2 = Button(window, image = my_img2, command = myFunc)
button3 = Button(window, image = my_img2, command = myFunc)

button1.pack(side=BOTTOM, fill = X, padx = 10, pady = 10) #위젯 외부 여백
button2.pack(side=LEFT, fill = X, padx = 10, pady = 10)
button3.pack(side=BOTTOM, fill = X, padx = 10, pady = 10)

window.mainloop()