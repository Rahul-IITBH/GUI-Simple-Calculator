from tkinter import *
import tkinter.font as font
expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equalpress(data):
    try:
        global expression
        global res
        total=str(eval(data))
        rest.set(total)
        expression=""

    except:
        equation.set("Error")
        expression=""

def clearall():
    global expression
    global res
    expression=""
    res=""
    equation.set("")
    rest.set("")

def clear():
    global expression
    expression=expression[0:-1]
    equation.set(expression)

if __name__=='__main__':
    screen = Tk()
    screen.title("Calculator")
    screen.geometry('250x480')
    screen.config(bg='red')
    screen.wm_minsize(width=250, height=480)
    screen.wm_maxsize(width=250, height=480)
    equation=StringVar()
    rest=StringVar()

    mf = font.Font(family="Calibri", size=25)

    new = Button(screen, text='Clear all', bg='orange', fg='blue',command=clearall)
    new.place(x=10, y=182, width=120, height=50)
    new['font'] = mf

    clear = Button(screen, text='Clear', bg='orange', fg='blue', command=clear)
    clear.place(x=155, y=182, width=85, height=50)
    clear['font'] = mf

    one = Button(screen, text='1', bg='orange', fg='blue', command=lambda: press(1))
    one.place(x=10, y=240, width=50, height=50)
    one['font'] = mf

    two = Button(screen, text='2', bg='orange', fg='blue', command=lambda: press(2))
    two.place(x=70, y=240, width=50, height=50)
    two['font'] = mf

    three = Button(screen, text='3', bg='orange', fg='blue', command=lambda: press(3))
    three.place(x=130, y=240, width=50, height=50)
    three['font'] = mf

    four = Button(screen, text='4', bg='orange', fg='blue', command=lambda: press(4))
    four.place(x=10, y=300, width=50, height=50)
    four['font'] = mf

    five = Button(screen, text='5', bg='orange', fg='blue', command=lambda: press(5))
    five.place(x=70, y=300, width=50, height=50)
    five['font'] = mf

    six = Button(screen, text='6', bg='orange', fg='blue', command=lambda: press(6))
    six.place(x=130, y=300, width=50, height=50)
    six['font'] = mf

    seven = Button(screen, text='7', bg='orange', fg='blue', command=lambda: press(7))
    seven.place(x=10, y=360, width=50, height=50)
    seven['font'] = mf

    eight = Button(screen, text='8', bg='orange', fg='blue', command=lambda: press(8))
    eight.place(x=70, y=360, width=50, height=50)
    eight['font'] = mf

    nine = Button(screen, text='9', bg='orange', fg='blue', command=lambda: press(9))
    nine.place(x=130, y=360, width=50, height=50)
    nine['font'] = mf

    zero = Button(screen, text='0', bg='orange', fg='blue', command=lambda: press(0))
    zero.place(x=70, y=420, width=50, height=50)
    zero['font'] = mf

    decimal = Button(screen, text='.', bg='orange', fg='blue', command=lambda: press('.'))
    decimal.place(x=10, y=420, width=50, height=50)
    decimal['font'] = mf

    plus = Button(screen, text='+', bg='orange', fg='blue', command=lambda: press('+'))
    plus.place(x=190, y=420, width=50, height=50)
    plus['font'] = mf

    minus = Button(screen, text='-', bg='orange', fg='blue', command=lambda: press('-'))
    minus.place(x=190, y=360, width=50, height=50)
    minus['font'] = mf

    multiply = Button(screen, text='x', bg='orange', fg='blue', command=lambda: press('*'))
    multiply.place(x=190, y=300, width=50, height=50)
    multiply['font'] = mf

    divide = Button(screen, text='/', bg='orange', fg='blue', command=lambda: press('/'))
    divide.place(x=190, y=240, width=50, height=50)
    divide['font'] = mf

    equalto= Button(screen, text='=', bg='orange', fg='blue', command=lambda: equalpress(expression))
    equalto.place(x=130, y=420, width=50, height=50)
    equalto['font'] = mf

    l1 = Label(screen, text='INPUT: ', bg='orange', fg='blue')
    l1.config(borderwidth=2, relief='solid', font=('calibri', 20))
    l1.place(x=10, y=4)

    data = Entry(screen, textvariable=equation)
    data.config(borderwidth=2, relief='solid', bg='orange', fg='blue', font=('calibri', 20))
    data.place(x=10, y=48, width=230, height=40)

    l2 = Label(screen, text='OUTPUT: ', bg='orange', fg='blue')
    l2.config(borderwidth=2, relief='solid', font=('calibri', 20))
    l2.place(x=10, y=92)

    result = Entry(screen,textvariable=rest)
    result.config(borderwidth=2, relief='solid', bg='orange', fg='blue', font=('calibri', 20))
    result.place(x=10, y=136, width=230, height=40)

    screen.mainloop()