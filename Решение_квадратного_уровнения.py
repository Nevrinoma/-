from tkinter import *
from math import *
D = ""
x1 = ""
x2 = ""
def x2_uravn(event):
    a = enta.get()
    b = entb.get()
    c = entc.get()
    D = float(b)**2 - (4*float(a)*float(c))
    if D >= 0:
        x1 = (-float(b) + sqrt(float(D))) / (2*float(a))
        x2 = (-float(b) - sqrt(float(D))) / (2*float(a))
        lbl4.configure(text=f"""D >>> {round(D,2)}
        x1 >>> {round(x1,2)}
        x2 >>> {round(x2,2)}""")
    elif D == 0:
        x1 = (-float(b)/2*float(a))
        lbl4.configure(text=f"""D >>> {D}
        x >>> {x1}""")
    else:
        lbl4.configure(text=f"""D >>> Нет решений
        x1 >>> Нет решений
        x2 >>> Нет решений""")



root = Tk()
root.title("Решение квадратного уравнения")
root.minsize(550,225)
root.resizable(width=False, height=False)
lbl = Label(root,text="Решение квадратного уравнения",height=1,width=30,font="Arial 20",bg="lightblue",fg="green",relief="flat")
lbl.pack()

butn = Button(root,text="Решение",height=2,width=8,font="Arial 22",bg="green",fg="black",relief="raised")
butn.place(x=375,y=55)
butn.bind("<Button-1>",x2_uravn)

enta = Entry(root,width=3,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
enta.place(x=10,y=85)

lbl2 = Label (root,text="x**2+",height=1,width=4,font="Arial 15",fg="green",relief="flat")
lbl2.place(x=60,y=85)

entb = Entry(root,width=3,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
entb.place(x=110,y=85)


lbl3 = Label (root,text="x+",height=1,width=2,font="Arial 15",fg="green",relief="flat")
lbl3.place(x=165,y=85)

entc = Entry(root,width=3,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
entc.place(x=200,y=85)

lbl4 = Label (root,text="=0",height=1,width=2,font="Arial 15",fg="green",relief="flat")
lbl4.place(x=255,y=85)

lbl5 = Label (root,text="D >>> "+D+"\nx1 >>> "+x1+"\nx2 >>> "+x2+"",height=4,width=25,font="Arial 12",bg="yellow",fg="black",relief="flat")
lbl5.pack(side=BOTTOM)









root.mainloop()



