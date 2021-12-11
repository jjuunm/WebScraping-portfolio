from tkinter import *

root = Tk()
root.title("Jun GUI")

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "버튼2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "버튼3") # 여백 ?
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text="버튼4") # 창 고정 크기
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", text = "버튼 5") # fg =  글자 색상, bg = 백그라운드 배경
btn5.pack()

photo = PhotoImage(file = "C:/Users/J/PycharmProjects/pythonProject1/GUI_basic/image.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()