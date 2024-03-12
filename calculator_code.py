from tkinter import *
class Calculator:
    def __init__(self):
        self.window=Tk()
        self.window.title("CALCULATOR")
        self.window.minsize(550,450)
        self.window.config(background='#DDD0C8')
        self.L1=Label(self.window, text="First Number : ")
        self.L2=Label(self.window, text="Second Number : ")
        self.L3=Label(self.window,text="  ")
        self.L4=Label(self.window,text="  ")
        self.L5=Label(self.window,text="  ")
        self.L6 = Label(self.window, text="  ")

        self.e1=Entry(self.window)
        self.e2=Entry(self.window)
        #self.e3=Entry(self.window)
        self.b1=Button(self.window,text="Addition :",command=self.addition)
        self.b2=Button(self.window,text="Subtraction :",command=self.Subtraction)

        self.b3=Button(self.window,text="Product:",command=self.Product)
        self.b4=Button(self.window,text="Division:",command=self.Division)

       #================ Placement Layout:-=================
        x1=10
        x2=x1+100
        y1=20
        y2=y1+50
        self.L1.place(x=x1,y=y1,width=90,height=40)
        self.e1.place(x=x2,y=y1,width=150,height=40)
        self.L2.place(x=x1,y=y2,width=95,height=40)
        #x3=x2+100
        self.e2.place(x=x2,y=y2,width=150,height=40)
        self.b1.place(x=x1,y=y2+60,width=80,height=40)
        self.L3.place(x=x2,y=y2+60,width=150,height=40)
        self.b2.place(x=x1, y=y2 +120, width=80, height=40)
        self.L4.place(x=x2, y=y2 +120, width=150, height=40)
        self.b3.place(x=x1,y=y2+180,width=80,height=40)
        self.L5.place(x=x2,y=y2+180,width=150,height=40)
        self.b4.place(x=x1, y=y2 + 240, width=80, height=40)
        self.L6.place(x=x2, y=y2 + 240, width=150, height=40)
        self.window.mainloop()

    def addition(self):
        a = float(self.e1.get())
        b = float(self.e2.get())
        c = a+b
        self.L3.config(text="Addition:-"+str(c))
    def Subtraction(self):
        a = float(self.e1.get())
        b = float(self.e2.get())
        c = a-b
        self.L4.config(text="Subtraction:-"+str(c))
    def Product(self):
        a = float(self.e1.get())
        b = float(self.e2.get())
        s = a * b
        self.L5.config(text="Product:- "+str(s))

    def Division(self):
        a = float(self.e1.get())
        b = float(self.e2.get())
        s = a / b
        self.L6.config(text="Division:- " + str(s))



if __name__ == '__main__':
    obj=Calculator()