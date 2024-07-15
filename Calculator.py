#GUI Based Calculator

from tkinter import *

root=Tk()
root.title("Calculator")

#Add empty box
my_entry=Entry(root,width=50,borderwidth=10)
my_entry.grid(row=0,column=0,columnspan=4,padx=10,pady=20)

def button_click(number):
    current=my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,current+str(number))

def button_add():
    first_number=my_entry.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    my_entry.delete(0, END)

def button_sub():
    first_number=my_entry.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    my_entry.delete(0, END)

def button_mul():
    first_number=my_entry.get()
    global f_num
    global math
    math = "Multiplication"
    f_num=int(first_number)
    my_entry.delete(0, END)

def button_div():
    first_number=my_entry.get()
    global f_num
    global math
    math = "Division"
    f_num=int(first_number)
    my_entry.delete(0, END)

def button_eq():
    second_number=my_entry.get()
    s_num=int(second_number)
    my_entry.delete(0, END)
    if math == "Addition":
        my_entry.insert(0, f_num+s_num)
    if math == "Subtraction":
        my_entry.insert(0, f_num-s_num)
    if math == "Multiplication":
        my_entry.insert(0, f_num*s_num)
    if math == "Division":
        my_entry.insert(0, f_num/s_num)



#Create buttons
my_button1=Button(root,text="1", font=72, padx=40, pady=30, command=lambda: button_click(1))
my_button2=Button(root,text="2", font=72, padx=40, pady=30, command=lambda: button_click(2))
my_button3=Button(root,text="3", font=72, padx=40, pady=30, command=lambda: button_click(3))

my_button4=Button(root,text="4", font=72, padx=40, pady=30, command=lambda: button_click(4))
my_button5=Button(root,text="5", font=72, padx=40, pady=30, command=lambda: button_click(5))
my_button6=Button(root,text="6", font=72, padx=40, pady=30, command=lambda: button_click(6))

my_button7=Button(root,text="7", font=72, padx=40, pady=30, command=lambda: button_click(7))
my_button8=Button(root,text="8", font=72, padx=40, pady=30, command=lambda: button_click(8))
my_button9=Button(root,text="9", font=72, padx=40, pady=30, command=lambda: button_click(9))

my_button0=Button(root,text="0", font=72, padx=40, pady=30, command=lambda: button_click(0))

my_button_add=Button(root,text="+", font=72, padx=40, pady=30, command=button_add)
my_button_sub=Button(root,text="-", font=72, padx=40, pady=30, command=button_sub)
my_button_mul=Button(root,text="×", font=72, padx=40, pady=30, command=button_mul)
my_button_div=Button(root,text="÷", font=72, padx=40, pady=30, command=button_div)

my_button_clear=Button(root,text="C", font=72, padx=40, pady=30, bg="blue", command=lambda: my_entry.delete(0,END))
my_button_equal=Button(root,text="=", font=72, padx=40, pady=30, command=button_eq)
#Position
my_button7.grid(row=1,column=0)
my_button8.grid(row=1,column=1)
my_button9.grid(row=1,column=2)

my_button4.grid(row=2,column=0)
my_button5.grid(row=2,column=1)
my_button6.grid(row=2,column=2)

my_button1.grid(row=3,column=0)
my_button2.grid(row=3,column=1)
my_button3.grid(row=3,column=2)

my_button0.grid(row=4,column=1)

my_button_add.grid(row=1,column=3)
my_button_sub.grid(row=2,column=3)
my_button_mul.grid(row=3,column=3)
my_button_div.grid(row=4,column=3)

my_button_clear.grid(row=4,column=0)
my_button_equal.grid(row=4,column=2)
root.mainloop()