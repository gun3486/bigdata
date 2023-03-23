from tkinter import *
app = Tk()

btn_0 = Button(app, text="(0, 1)")
btn_0.grid(column=0, row=0, columnspan=2) #두 셀을 합침
btn_1 = Button(app, text="(0, 2)")
btn_1.grid(column=2, row=0)
btn_2 = Button(app, text="(0, 3)")
btn_2.grid(column=3, row=0, padx= 20, pady= 5,rowspan=2)
btn_3 = Button(app, text="(1, 1)")
btn_3.grid(column=0, row=1,sticky="n") #정렬
btn_4 = Button(app, text="(1, 2)")
btn_4.grid(column=1, row=1, ipadx= 5, ipady= 5)
btn_5 = Button(app, text="(1, 3)")
btn_5.grid(column=4, row=1)

app.title('grid')
app.geometry("300x200")
app.mainloop()