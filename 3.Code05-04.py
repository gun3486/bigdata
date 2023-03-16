from tkinter import *
from PIL import Image, ImageTk #Pollow install

window = Tk()
window.title("냥이들 ^^")
msg="반도체융합캠퍼스 반도체융합SW"
label5=Label(window, text=msg)

photo1 = PhotoImage(file="testimage.gif")
label1 = Label(window, image=photo1)
photo2 = PhotoImage(file="testimage.gif")
label2 = Label(window, image=photo1)

image=Image.open("testimage2.gif")
img=image.resize((200, 200))
my_img = ImageTk.PhotoImage(img)
label3 = Label(window, image=my_img)

imgrotate = img.rotate(50)
my_img2 = ImageTk.PhotoImage(imgrotate)
label4 = Label(window, image=my_img2)

#label1.pack(side=RIGHT)
#label2.pack(side=LEFT)
#label3.pack(side=RIGHT)
label4.pack(side=RIGHT)
label5.pack(side=RIGHT)

window.mainloop()