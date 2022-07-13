'''
--------------------------------------------------------------------------------------------------------------
Simple GUI Calculator
--------------------------------------------------------------------------------------------------------------'''

from tkinter import *
root = Tk()
root.title("Simple Calculator")



calculation =""

def add_to_calculation(symbol):
    global calculation
    add_to_cal = str(symbol)
    calculation = calculation + str(add_to_cal)
    ent1.delete(0, END) #delete what is alread in the box
    ent1.insert(0, str(calculation))
    
    
def clear_field():
    ent1.delete(0, END)
    calculation =""

    
def eval_calculation():
    global calculation
    clear_field()

    try: 
        calc_result = str(eval(calculation))
        #print (calc_result)
        calculation =""
        #ent1.delete = (0, END)
        ent1.insert(0,calc_result)
    except:
        clear_field()
        ent1.insert(0,"ERROR")
    

ent1 = Entry(root, width = 35,  borderwidth = 5)
ent1.grid(row =0,column=0, columnspan=4)


#Define buttons
btn_add = Button(root, text='+',padx=5,bg = "gray99", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation("+"))
btn_add.grid(row=1, column=0)

btn_minus = Button(root, text='-',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation("-"))
btn_minus.grid(row=1, column=1)

btn_division = Button(root, text='/',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation("/"))
btn_division.grid(row=1, column=2)

btn_multiply = Button(root, text='*',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation("*"))
btn_multiply.grid(row=1, column=3)

btn_open = Button(root, text='(',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda:add_to_calculation("("))
btn_open.grid(row=2, column=0)

btn_close = Button(root, text=')',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation(")"))
btn_close.grid(row=2, column=1)

btn_percent = Button(root, text='%',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda:add_to_calculation("%"))
btn_percent.grid(row=2, column=2)

btn_log = Button(root, text='log',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda:add_to_calculation("log"))
btn_log.grid(row=2, column=3)


#Put the buttons on the screen
btn_1 = Button(root, text='1',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3, command = lambda: add_to_calculation(1))
btn_1.grid(row=3, column=0)

btn_2 = Button(root, text='2',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(2))
btn_2.grid(row=3, column=1)

btn_3 = Button(root, text='3',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(3))
btn_3.grid(row=3, column=2)

btn_4 = Button(root, text='4',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(4))
btn_4.grid(row=3, column=3)

btn_5 = Button(root, text='5',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(5))
btn_5.grid(row=4, column=0)

btn_6 = Button(root, text='6',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(6))
btn_6.grid(row=4, column=1)

btn_7 = Button(root, text='7',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(7))
btn_7.grid(row=4, column=2)

btn_8 = Button(root, text='8',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(8))
btn_8.grid(row=4, column=3)

btn_9 = Button(root, text='9',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(9))
btn_9.grid(row=5, column=0)

btn_0 = Button(root, text='0',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(0))
btn_0.grid(row=5, column=1)

btn_decimal = Button(root, text='.',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: add_to_calculation(1))
btn_decimal.grid(row=5, column=2)

btn_equal = Button(root, text='=',padx=5,bg = "White", fg ="Blue",width = 8,borderwidth = 3,command = lambda: eval_calculation())
btn_equal.grid(row=5, column=3)

btn_clear = Button(root, text='Clear',padx=5,bg = "White", fg ="Blue",width = 30,borderwidth = 3,command = lambda: clear_field())
btn_clear.grid(row=6, column=0, columnspan=4)


root.mainloop()