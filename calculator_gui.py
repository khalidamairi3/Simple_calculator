from tkinter import * 


root = Tk()
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
result = 0 
operation = 0
def calculate(num):
    cur= e.get()
    e.delete(0,END)
    e.insert(0,cur+str(num))
def perform():
    global result
    global operation
    if operation==0 or operation==1:
        result = result + int(e.get())
    elif operation == 2:
        result = result - int(e.get())
    elif operation == 3:
        result = result * int(e.get())
    elif operation == 4:
        result = result / int(e.get())
    e.delete(0,END)
    
   
def operationToUse(opt):
    global operation
    global result
    perform()
    operation=opt
    if operation == 5:
         e.insert(0,result)

    
def clear():
    global operation
    result=0
    operation=0
    e.delete(0,END)
button_1 = Button(root,text="1",padx=40,pady=20,command= lambda: calculate(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: calculate(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: calculate(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: calculate(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: calculate(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: calculate(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: calculate(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: calculate(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: calculate(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: calculate(0))

button_add=Button(root,text="+",padx=40,pady=20,bg="#FF6700",fg="#EBEBEB",command=lambda: operationToUse(1))
button_subtract=Button(root,text="-",padx=40,pady=20,bg="#FF6700",fg="#EBEBEB",command=lambda: operationToUse(2))
button_multiply=Button(root,text="*",padx=40,pady=20,bg="#FF6700",fg="#EBEBEB",command=lambda: operationToUse(3))
button_divide=Button(root,text="/",padx=40,pady=20,bg="#FF6700",fg="#EBEBEB",command=lambda: operationToUse(4))
button_clear=Button(root,text="clear",padx=30,pady=20,command=clear)
button_equal=Button(root,text="=",padx=40,pady=20,command=lambda: operationToUse(5))


button_0.grid(row=4,column=0)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=4,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=1,column=3)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)


root.mainloop()