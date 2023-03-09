from tkinter import * #toolkit interface
#타 GUI 프레임워크나 툴킷에 비해 지원되는 위젯들이 부족하고 UI도 그렇게 예쁘지 않다는 단점이 있지만, Python 설치시 기본적으로 내장되어 있는 파이썬 표준 라이브러리이기 때문에 쉽고 간단한 GUI 프로그램을 만들 때 활용될 수 있다.

window = Tk()
window.title("윈도 창 연습")
#window.geometry("400x100")  # [ dʒi|ɑːmətri ]
window.resizable(width = FALSE, height = FALSE)

label1 = Label(window, text = "데이터 분석을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "yellow")
#label2.place(x=100, y=100) #pack과 같이 사용하면 주의
#label3 = Label(window, text = "공부 중입니다.", bg = 'ghost white', width = 20, height = 5, anchor = SE)
label3 = Label(window, text = "공부 중입니다.", bg = 'yellow', width = 20, height = 5, anchor = SE,
               borderwidth=5,relief='ridge')
#https://opentutorials.org/module/3181/18805
#anchor https://www.tutorialspoint.com/python/tk_anchors.htm
#색상 : https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/
label1.pack() #공간에 채워 넣음
label2.pack()
label3.pack()
window.mainloop()

#https://dafarry.github.io/tkinterbook/label.htm