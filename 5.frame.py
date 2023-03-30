from tkinter import *

window=Tk()
window.title("frame")
window.geometry("640x400+100+100")
window.resizable(True, True)

frame1=LabelFrame(window, relief="solid", bd=2,bg="yellow",text='Hello_World',) #relief= 경계선 설정
 #LabelFrame, Frame차이 =text='Hello_World' 유무     #flat	기본값으로 경계선이 보이지 않는다.
                                                    #raised	경계 안쪽이 바깥보다 볼록하게 보인다.
                                                    #sunken	경계 안쪽이 바깥보다 오목하게 보인다.
                                                    #solid	경계에 단순한 선이 그어진다.
                                                    #ridge	경계선만 볼록해 보인다.
                                                    #groove	경계선만 오목해 보인다.
                                                    #frame1.pack(side="left", fill="both", expand=True)
                                            #bg  : 배경색
                                            #bd  : 프레임 보드라인
                                            #cursor : frame1위에 커서를 올리면 동그라미 커서
                                            #height : 프레임의 높이
                                            #highligtbackground : 프레임을 선택하지 않았을때 나오는 색상
                                            #highlightcolor  : 프레임을 선택하면 나오는색상
                                            #highlightthickness :프레임의 두께
                                            #relief  :경계선
                                            #width   : 폭
frame1.pack(side="right", fill="both", expand=True)
#X = 수평으로만 늘리기
#Y = 수직으로만 늘리기
#BOTH = 수평,수직 모두 늘리기
#NONE = 늘리지 않기

frame2=Frame(window, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

btd_0 = Button(frame1, text="(0, 1)",bd=10,bg="yellow")
btd_0.grid(column=1, row=0)
btd_1 = Button(frame1, text="(0, 2)", bg="yellow",activebackground="green",
    activeforeground='black')
btd_1.grid(column=2, row=0)
btd_2 = Button(frame1, text="(0, 3)")
btd_2.grid(column=3, row=0)

button2=Button(frame2, text="프레임2")
button2.pack(side="left")

window.mainloop()
