import turtle
import time
from tkinter import simpledialog, messagebox
wn = turtle.Screen()
wn.bgcolor('light blue')
wn.title('Calculator')
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(0,300)
t.pendown()
t.hideturtle()
t.turtlesize(20)
t.write('Calculator', 'Agency FB', 'left', 'normal')
t.penup()
t.goto(-300,300)
t.pendown()
t.write('Answers')
t.penup()
t.right(90)
t.forward(30)
time.sleep(2)
def x(x):
    y= x
    ans=0
    for i in range(x):
        ans+=y
        y-=1
while True:
    x = ('+', '-', '*', '/', '^')
    exit = simpledialog.askstring("exit","Press any button to continue of # to exit: ")
    if exit == "#":
        simpledialog.askstring("ERRORR", "Thanks for using the calculator")
        break
    num1 = simpledialog.askfloat("num2", "Enter a number: ")
    equation = simpledialog.askstring('equation', "Enter a operation [+, -, /, *, ^, !]: ")
    if equation == '!':
            x(float(num1))
    else:
        num2 = simpledialog.askfloat('num2',"Enter a number: ")
        ans = 0
        if equation in x:
            if equation == '+':
                ans = (num1+num2)
            elif equation == '-':
                ans = (num1-num2)
            elif equation == '/':
                ans = (num1/num2)
            elif equation == '*':
                ans = (num1*num2)
            elif equation == '^':
                ans = (num1**num2)
            elif equation == '!':
                x(num1)
            else:
                ans = ("Error")
    ansstatement = (num1, equation, num2, '=', ans)
    t.pendown()
    t.write(ansstatement)
    t.penup()
    t.forward(30)
    messagebox.askokcancel('Answer is:', ans)
