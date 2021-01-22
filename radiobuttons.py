from tkinter import *

food = ["マルゲリータピザ","肉巻き寿司","ホットドッグ"]

def order():
    if(x.get()==0):
        print("マルゲリータピザを注文いたしました")
    elif(x.get()==1):
         print("肉巻き寿司を注文いたしました")
    elif(x.get()==2):
         print("ホットドッグを注文いたしました")
    else:
        print("もう一度やり直してください")

window = Tk()



x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                             text=food[index],
                             variable=x,
                             value=index,
                             padx = 25,
                             font=("Impact",50),
                            compound = 'left',
                            indicatoron=0,
                            width  = 375,
                            command=order
                             )

    radiobutton.pack(anchor=W)
window.mainloop()
