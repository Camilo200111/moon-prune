from tkinter import *
import random
root = Tk()
root.title("24")
label = Label(root, text="opera 4 números utilizando suma, resta, multiplicación y división de modo que el resultado sea 24")
label.grid(row=1, column=0, columnspan=7)



#operaciones de numeros
a= 0
b= 0
c= 0
val1= random.randrange(1,2)
val2= random.randrange(3,4)
val3= random.randrange(1,2)
val4= random.randrange(9,10)
num1= val1
num2= val2
num3= val3
num4= val4
def mdr():
    global num1
    global val1
    n1 = Button(root, text=val1, command=mdr1).grid(row=2,column=0)
    num1= val1
def mdr1():
    global num1
    global val2
    n1 = Button(root, text=val2, command=mdr2).grid(row=2,column=0)
    num1= val2
def mdr2():
    global num1
    global val3
    n1 = Button(root, text=val3, command=mdr3).grid(row=2,column=0)
    num1= val3
def mdr3():
    global num1
    global val4
    n1 = Button(root, text=val4, command=mdr).grid(row=2,column=0)
    num1= val4
n1 = Button(root, text=val1, command=mdr1).grid(row=2,column=0)

def ci():
    global num2
    global val1
    n2 = Button(root, text=val1, command=ci1).grid(row=2,column=2)
    num2= val1
def ci1():
    global num2
    global val2
    n2 = Button(root, text=val2, command=ci2).grid(row=2,column=2)
    num2= val2
def ci2():
    global num2
    global val3
    n2 = Button(root, text=val3, command=ci3).grid(row=2,column=2)
    num2= val3
def ci3():
    global num2
    global val4
    n2 = Button(root, text=val4, command=ci).grid(row=2,column=2)
    num2= val4
n2 = Button(root, text=val2, command=ci).grid(row=2,column=2)

def cic():
    global num3
    global val1
    n3 = Button(root, text=val1, command=cic1).grid(row=2,column=4)
    num3= val1
def cic1():
    global num3
    global val2
    n3 = Button(root, text=val2, command=cic2).grid(row=2,column=4)
    num3= val2
def cic2():
    global num3
    global val3
    n3 = Button(root, text=val3, command=cic3).grid(row=2,column=4)
    num3= val3
def cic3():
    global num3
    global val4
    n3 = Button(root, text=val4, command=cic).grid(row=2,column=4)
    num3= val4
n3 = Button(root, text=val3, command=cic).grid(row=2,column=4)

def cicl():
    global num4
    global val1
    n4 = Button(root, text=val1, command=cicl1).grid(row=2,column=6)
    num4= val1
def cicl1():
    global num4
    global val2
    n4 = Button(root, text=val2, command=cicl2).grid(row=2,column=6)
    num4= val2
def cicl2():
    global num4
    global val3
    n4 = Button(root, text=val3, command=cicl3).grid(row=2,column=6)
    num4= val3
def cicl3():
    global num4
    global val4
    n4 = Button(root, text=val4, command=cicl).grid(row=2,column=6)
    num4= val4
n4 = Button(root, text=val4, command=cicl).grid(row=2,column=6)

def opera():
    global a
    op1 = Button(root, text="-", padx=53, command=opera1).grid(row=2,column=1)
    a= num1 - num2
def opera1():
    global a
    op1 = Button(root, text="*", padx=53, command=opera2).grid(row=2,column=1)
    a= num1 * num2
def opera2():
    global a
    op1 = Button(root, text="/", padx=53, command=opera3).grid(row=2,column=1)
    a= num1 / num2
def opera3():
    global a
    op1 = Button(root, text="+", padx=53, command=opera).grid(row=2,column=1)
    a= num1 + num2

op1 = Button(root, text="", padx=53, command=opera).grid(row=2,column=1)

def seco():
    global a
    global b
    op2 = Button(root, text="-", padx=54, command=seco1).grid(row=2,column=3)
    b = a - num3
def seco1():
    global a
    global b
    op2 = Button(root, text="*", padx=54, command=seco2).grid(row=2,column=3)
    b = a * num3
def seco2():
    global a
    global b
    op2 = Button(root, text="/", padx=54, command=seco3).grid(row=2,column=3)
    b = a / num3
def seco3():
    global a
    global b
    op2 = Button(root, text="+", padx=54, command=seco).grid(row=2,column=3)
    b = a + num3

op2 = Button(root, text="", padx=54, command=seco).grid(row=2,column=3)

def tero():
    global b
    global c
    op3 = Button(root, text="-", padx=50, command=tero1).grid(row=2,column=5)
    c = b - num4
def tero1():
    global b
    global c
    op3 = Button(root, text="*", padx=50, command=tero2).grid(row=2,column=5)
    c = b * num4
def tero2():
    global b
    global c
    op3 = Button(root, text="/", padx=50, command=tero3).grid(row=2,column=5)
    c = b / num4
def tero3():
    global b
    global c
    op3 = Button(root, text="+", padx=50, command=tero).grid(row=2,column=5)
    c = b + num4

op3 = Button(root, text="", padx=50, command=tero).grid(row=2,column=5)











#botones de solucion
    #button func

def ressol():
    global c
    global a
    if c == 24:
        labelres= Label(root, text=("Correcto")).grid(row=5,column=3)
    else:
        labelres= Label(root, text=("Incorrecto")).grid(row=5,column=3)
        #button
res = Button(root, text="Fin", padx=50, command=ressol)
nosol= Button(root, text="No tiene solucion", padx=10, command=root.destroy)
    #buton placement
res.grid(row=4,column=5)
nosol.grid(row=4,column=1)
#space placemennt
space = Label(root, text="                   ").grid(row=4,column=2)
space = Label(root, text="                   ").grid(row=4,column=4)
space = Label(root, text="                   ").grid(row=4,column=0)
space = Label(root, text="                   ").grid(row=4,column=6)

ind= Label(root, text=(num1,num2,num3,num4)).grid(row=4, column=3)




root.mainloop()
