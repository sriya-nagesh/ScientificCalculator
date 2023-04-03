#Sriya Nagesh

import tkinter as tk
import math

calculation=""
result=1

def add(symbol):
    global calculation
    calculation+=str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "error")

def clear():
    global calculation
    calculation=""
    result.delete(1.0,"end")
    pass


def ScientificCalculate(pressed):
    global calculation
    if pressed=='√':
        calculation=str(math.sqrt(float(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0, calculation)

    if pressed=='deg':
        calculation=str(math.degrees(float(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)

    if pressed=='sin':
        calculation=str(math.sin(float(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)

    if pressed=='cos':
        calculation=str(math.cos(float(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)

    if pressed=='tan':
        calculation=str(math.tan(float(calculation)))
        result.delete(1.0, "end")
        result.insert(1.0,calculation)

    if pressed=='log':
        calculation=str(math.log10(float(calculation)))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)

    if pressed=='ln':
        calculation=str(math.log(float(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0, calculation)

    if pressed=='n!':
        calculation=str(math.factorial(int(calculation)))
        result.delete(1.0,"end")
        result.insert(1.0, calculation)

    if pressed=='1/n':
        calculation=str(1/(float(calculation))) 
        result.delete(1.0, "end")  
        result.insert(1.0, calculation)


root=tk.Tk()
root.title("Scientific Calculator")
root.geometry("302x398")
root.configure(bg="#12182B")

result= tk.Text(root, height=2, width=20, font=("Helvetica", 20), bg="lightgray", fg="#1c2341")
result.grid(row=1, column=1, columnspan=5)

def button(name,number,r,c):
    name=tk.Button(root, text=number, command=lambda:add(number), width=3, font=("Arial", 18), bg="#394f6b", fg="#FFF", activebackground="#1c2341", activeforeground="white", relief=tk.RAISED)
    name.grid(row=r, column=c)

button("btn1",1,7,1)
button("btn2",2,7,2)
button("btn3",3,7,3)
button("add","+",6,5)
button("btn4",4,6,1)
button("btn5",5,6,2)
button("btn6",6,6,3)
button("minus","-",6,4)
button("btn7",7,5,1)
button("btn8",8,5,2)
button("btn9",9,5,3)
button("multiply","*",5,4)
button("btn0",0,4,3)
button("divide","/",5,5)
button("open","(",4,1)
button("close",")",4,2)
button("decimalpoint",".",4,4)

clear=tk.Button(root, text="C", command=clear, width=7, font=("Helvetica", 18), bg="#ff6961", fg="#FFF", activebackground="#1c2341", activeforeground="white", relief=tk.RAISED)
clear.grid(row=7, column=4, columnspan=2)
equal=tk.Button(root, text="=", command=evaluate, width=20, font=("Helvetica", 18), bg="gray", fg="#FFF", activebackground="#1c2341", activeforeground="white", relief=tk.RAISED)
equal.grid(row=8, column=1, columnspan=5)
pi=tk.Button(root, text="π",command=lambda:add(math.pi), width=3, font=("Arial", 18), bg="#1c2341", fg="#FFF", activebackground="#394f6b", activeforeground="white", relief=tk.RAISED)
pi.grid(row=3, column=2)
e=tk.Button(root, text="e",command=lambda:add(math.e), width=3, font=("Arial", 18), bg="#394f6b", fg="#FFF", activebackground="#1c2341", activeforeground="white", relief=tk.RAISED)
e.grid(row=4, column=5)

def ScientificButton(text,r,c):
    sqrt=tk.Button(root, text=text,command=lambda:ScientificCalculate(text), width=3, font=("Helvetica", 18), bg="#1c2341", fg="#FFF", activebackground="#39456b", activeforeground="white", relief=tk.RAISED)
    sqrt.grid(row=r, column=c)

ScientificButton("√",2,1)
ScientificButton("deg",2,2)
ScientificButton("sin",2,3)
ScientificButton("cos",2,4)
ScientificButton("tan",2,5)
ScientificButton("log",3,1)
ScientificButton("ln",3,3)
ScientificButton("n!",3,4)
ScientificButton("1/n",3,5)

root.mainloop()
