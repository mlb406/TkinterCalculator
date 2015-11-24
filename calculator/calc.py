# -*- coding: utf-8 -*-
#calc.py

from Tkinter import *
from tkSimpleDialog import askstring

#initial things

maincolour = '#%02x%02x%02x' % (240, 240, 237)

window = Tk()
window.title("Calculator")

#functions	

def click(n):	
    main_text.insert(END, n)

def operator(o):
    main_text.insert(END, o)

def clear():
    main_text.delete(1.0, END)

def equals():
    eqn = main_text.get(1.0, END)
    result = eval(eqn)
    floatTest = str(float(result)).split(".")
    if floatTest[1] != "0":
    	#print floatTest
    	#print result
        output = str(float(result))
    else:
        output = str(int(result))
    main_text.delete(1.0, END)
    main_text.insert(END, output)

def check_for_hex():
    # not finished...
    #or just add a hex button (with a new window, with a hex keypad)
    main_input = main_text.get(1.0, END)
    input_split = (main_text.get(1.0, END)).split("0x")
    if len(input_split[0]) == len(main_input):
        return "0x"
    elif r"(\+|-|\*|\/)" in input_split[-1]: # use regex to find +, -, *, / symbols. Needs work and testing
        return 0 # check this
    elif ["+", "-", "/", "*"] not in input_split[-1]:
        return ""

# and make the same for binary ^^

def ins_hex(event):
    #add in "check_for_hex" with prefix value
    result = askstring("Hex", "Enter valid hex sequence")
    try:
        int(result, 16)
        main_text.insert(END, "0x" + str(result))
        return 0
    except:
        if result == None: # checking for if the user just clicked "cancel"...
            pass
        else:
            return ins_hex(event)

def ins_bin(event):
    result = askstring("Binary", "Enter valid binary sequence")
    try:
        int(result, 2)
        main_text.insert(END, "0b" + str(result))
        return 0
    except:
        if result == None:
            pass
        else:
            return ins_bin(event)

def create_hex_pad(event):
    temp = hex_keypad()
    temp.run()

def create_bin_pad(event):
    temp = bin_keypad()
    temp.run()

class hex_keypad:
    def __init__(self):
        self.hex_pad = Tk()
        self.hex_pad.title("HexPad")
        self.hex_pad.attributes("-toolwindow",1)
        self.hex_button_0x = Button(self.hex_pad, height=2, width=4, text="0x", command=lambda: operator("0x")).grid(row=0, column=1, padx=2, pady=2)
        self.hex_button_a = Button(self.hex_pad, height=2, width=4, text="a", command=lambda: click("a")).grid(row=1, column=0, padx=2, pady=2)
        self.hex_button_b = Button(self.hex_pad, height=2, width=4, text="b", command=lambda: click("b")).grid(row=1, column=1, padx=2, pady=2)
        self.hex_button_c = Button(self.hex_pad, height=2, width=4, text="c", command=lambda: click("c")).grid(row=1, column=2, padx=2, pady=2)
        self.hex_button_d = Button(self.hex_pad, height=2, width=4, text="d", command=lambda: click("d")).grid(row=2, column=0, padx=2, pady=2)
        self.hex_button_e = Button(self.hex_pad, height=2, width=4, text="e", command=lambda: click("e")).grid(row=2, column=1, padx=2, pady=2)
        self.hex_button_f = Button(self.hex_pad, height=2, width=4, text="f", command=lambda: click("f")).grid(row=2, column=2, padx=2, pady=2)
    def run(self):
        self.hex_pad.mainloop()

class bin_keypad:
    def __init__(self):
        self.bin_pad = Tk()
        self.bin_pad.title("BinPad")
        self.bin_pad.attributes("-toolwindow",1)
        self.bin_button_0b = Button(self.bin_pad, height=2, width=4, text="0b", command=lambda: operator("0b")).grid(row=0, column=0, padx=5, pady=2)
        self.bin_button_0 = Button(self.bin_pad, height=2, width=4, text="0", command=lambda: click("0")).grid(row=1, column=0, padx=5, pady=2)
        self.bin_button_1 = Button(self.bin_pad, height=2, width=4, text="1", command=lambda: click("1")).grid(row=2, column=0, padx=20, pady=2)
    def run(self):
        self.bin_pad.mainloop()

#widgets

main_text = Text(window, height=2, width=24, font=("fixedsys", 11))
main_text.grid(row=0, column=0, sticky=N, columnspan=15, padx=2, pady=2)

button_7 = Button(window, text="  7  ", height=2, width=4, command=lambda: click(7))
button_7.grid(row=1, column=0, sticky=W, padx=2, pady=2)

button_8 = Button(window, text="  8  ", height=2, width=4, command=lambda: click(8))
button_8.grid(row=1, column=3, sticky=W, padx=2, pady=2)

button_9 = Button(window, text="  9  ", height=2, width=4, command=lambda: click(9))
button_9.grid(row=1, column=6, sticky=W, padx=2, pady=2)

button_4 = Button(window, text="  4  ", height=2, width=4, command=lambda: click(4))
button_4.grid(row=4, column=0, sticky=W, padx=2, pady=2)

button_5 = Button(window, text="  5  ", height=2, width=4, command=lambda: click(5))
button_5.grid(row=4, column=3, sticky=W, padx=2, pady=2)

button_6 = Button(window, text="  6  ", height=2, width=4, command=lambda: click(6))
button_6.grid(row=4, column=6, sticky=W, padx=2, pady=2)

button_1 = Button(window, text="  1  ", height=2, width=4, command=lambda: click(1))
button_1.grid(row=7, column=0, sticky=W, padx=2, pady=2)

button_2 = Button(window, text="  2  ", height=2, width=4, command=lambda: click(2))
button_2.grid(row=7, column=3, sticky=W, padx=2, pady=2)

button_3 = Button(window, text="  3  ", height=2, width=4, command=lambda: click(3))
button_3.grid(row=7, column=6, sticky=W, padx=2, pady=2)

button_0 = Button(window, text="  0  ", height=2, width=10, command=lambda: click(0))
button_0.grid(row=10, column=0, sticky=W, columnspan=6, rowspan=3, padx=2, pady=2)

button_dec = Button(window, text="  .  ", height=2, width=4, command=lambda: click("."))
button_dec.grid(row=10, column=6, sticky=W, padx=2, pady=2)

#operators

button_plus = Button(window, text="  +  ", height=2, width=4, command=lambda: operator("+"))
button_plus.grid(row=1, column=9, sticky=W, padx=2, pady=2)

button_minus = Button(window, text="  -  ", height=2, width=4, command=lambda: operator("-"))
button_minus.grid(row=4, column=9, sticky=W, padx=2, pady=2)

button_times = Button(window, text="  x  ", height=2, width=4, command=lambda: operator("*"))
button_times.grid(row=7, column=9, sticky=W, padx=2, pady=2)

button_div = Button(window, text="  ÷  ", height=2, width=4, command=lambda: operator("/"))
button_div.grid(row=10, column=9, sticky=W, padx=2, pady=4)

button_c = Button(window, text="  AC  ", height=2, width=4, command=clear)
button_c.grid(row=1, column=12, sticky=W, padx=2, pady=2)

button_equals = Button(window, text="  =  ", height=8, width=4, command=equals)
button_equals.grid(row=4, column=12, sticky=W, padx=2, pady=2, rowspan=10)

#finishing

window.bind("<Control-h>", create_hex_pad)
window.bind("<Control-Shift-h>", ins_hex)
window.bind("<Control-b>", create_bin_pad)
window.bind("<Control-Shift-b>", ins_bin)
window.iconbitmap("etc/calculator.ico")
window.mainloop()
