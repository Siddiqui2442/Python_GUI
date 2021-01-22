from tkinter import *

def submit():
    print("現在の温度は"+ str(scale.get())+"度")

window = Tk()

scale = Scale(window,
             from=100,to=0,
             lengthen=600,
             orient=VERTICAL,
             font =('Consolas',20),
             tickinterval=10,
             #showvalue=0
             resolution=5,
             troughcolor='#69EAFF',
             fg = '#FF1C88',
             bg = '#111111'
            )


scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

button = Button(window,text='submit',command=submit)
butoon.pack()

window.mainloop()