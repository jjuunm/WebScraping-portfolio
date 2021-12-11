from tkinter import *

root = Tk()
root.title("Jun GUI")
root.geometry("640x480")  # 가로 * 세로

Label(root, text = "메뉴를 선택해 주세요").pack(side = 'top')

Button(root, text = "주문하기").pack(side = "bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief = "solid", bd = 1)
frame_burger.pack(side = "left", fill = "both", expand = True)

Button(frame_burger, text = "햄거버").pack()
Button(frame_burger, text = "치즈거버").pack()
Button(frame_burger, text = "치킨거버").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side = "right", fill = "both", expand = True)

Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "사이다").pack()

root.mainloop()