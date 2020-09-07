from tkinter import *

root=Tk()

root.title('calculator')

e=Entry(root, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=4)


def buttonclick(number):
		current=e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))

def add():
	first=e.get()
	global fnum
	global math
	math = 'addition'
	fnum = int(first)
	e.delete(0, END)

def subtract():
	first=e.get()
	global fnum
	global math
	math = 'subtraction'
	fnum = int(first)
	e.delete(0, END)

def multiply():
	first=e.get()
	global fnum
	global math
	math = 'multiplication'
	fnum = int(first)
	e.delete(0, END)
		
def divide():
	first=e.get()
	global fnum
	global math
	math = 'division'
	fnum = int(first)
	e.delete(0, END)

def clear():
	e.delete(0, END)

def equals():
		second=e.get()
		e.delete(0, END)

		if math == 'addition':
			e.insert(0, fnum + int(second))

		if math == 'subtraction':
			e.insert(0, fnum - int(second))
		
		if math == 'multiplication':
			e.insert(0, fnum * int(second))

		if math == 'division':
			e.insert(0, fnum / int(second))	


button1=Button(root, text="1", padx=40, pady=20, command=lambda:buttonclick(1))
button2=Button(root, text="2", padx=40, pady=20, command=lambda:buttonclick(2))
button3=Button(root, text="3", padx=40, pady=20, command=lambda:buttonclick(3))
button4=Button(root, text="4", padx=40, pady=20, command=lambda:buttonclick(4))
button5=Button(root, text="5", padx=40, pady=20, command=lambda:buttonclick(5))
button6=Button(root, text="6", padx=40, pady=20, command=lambda:buttonclick(6))
button7=Button(root, text="7", padx=40, pady=20, command=lambda:buttonclick(7))
button8=Button(root, text="8", padx=40, pady=20, command=lambda:buttonclick(8))
button9=Button(root, text="9", padx=40, pady=20, command=lambda:buttonclick(9))
button0=Button(root, text="0", padx=40, pady=20, command=lambda:buttonclick(0))

buttonadd=Button(root, text="+", padx=48, pady=20, command=add)
buttonsubtract=Button(root, text="-", padx=40, pady=20, command=subtract)
buttondivide=Button(root, text="/", padx=40, pady=20, command=divide)
buttonmultiply=Button(root, text="*", padx=40, pady=20, command=multiply)
buttonequals=Button(root, text="=", padx=49, pady=52, command=equals)
buttonclear=Button(root, text="clear", padx=40, pady=20, command=clear)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

buttonadd.grid(row=1, column=3)
buttonequals.grid(row=3, column=3, rowspan=2)
buttonsubtract.grid(row=4, column=0)
buttondivide.grid(row=4, column=1)
buttonmultiply.grid(row=4,column=2)
buttonclear.grid(row=2, column=3)

root.mainloop()
