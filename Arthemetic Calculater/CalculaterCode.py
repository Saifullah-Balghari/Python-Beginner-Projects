from tkinter import *


def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():

    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("Syntax Error!")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("Math Error!")
        equation_text = ""


def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""


root = Tk()

root.title("Basic Arithmetic Calculator".title())
root.iconphoto(True, PhotoImage(file="Icon.png"))
equation_text = ""
equation_label = StringVar()

label = Label(root, textvariable=equation_label, font=('consolas', 25, 'bold'), width=19, bd='6', foreground='black',
              bg='white', height=2, relief=RIDGE,)
label.pack()

Button(root, text='Clear', height=1, width=23, bd='5', font=('consolas', 20, 'bold'), relief=RIDGE, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white', command=clear).pack()

frame = Frame(root)
frame.pack()

Button(frame, text=1, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(1)).grid(row=0, column=0)
Button(frame, text=2, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(2)).grid(row=0, column=1)
Button(frame, text=3, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(3)).grid(row=0, column=2)
Button(frame, text=4, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(4)).grid(row=1, column=0)
Button(frame, text=5, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(5)).grid(row=1, column=1)
Button(frame, text=6, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(6)).grid(row=1, column=2)
Button(frame, text=7, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(7)).grid(row=2, column=0)
Button(frame, text=8, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(8)).grid(row=2, column=1)
Button(frame, text=9, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(9)).grid(row=2, column=2)
Button(frame, text=0, height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d', foreground='white',
       activebackground='#363e40', activeforeground='white', command=lambda: button_press(0)).grid(row=3, column=0)
Button(frame, text='+', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=lambda: button_press('+')).grid(row=0, column=3)
Button(frame, text='-', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=lambda: button_press('-')).grid(row=1, column=3)
Button(frame, text='*', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=lambda: button_press('*')).grid(row=2, column=3)
Button(frame, text='/', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=lambda: button_press('/')).grid(row=3, column=3)
Button(frame, text='=', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=equals).grid(row=3, column=2)
Button(frame, text='.', height=1, width=4, font=('consolas', 28, 'bold'), relief=RAISED, bg='#3f403d',
       foreground='white', activebackground='#363e40', activeforeground='white',
       command=lambda: button_press('.')).grid(row=3, column=1)

root.mainloop()
