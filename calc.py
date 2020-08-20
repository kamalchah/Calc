from tkinter import*

def buttonClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)


def cleardisplay():
    global operator
    operator = ''
    text_input.set('')

def equalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=''
    return sumup

def dont():
    print("dont click me please")

calc = Tk()
clicks = 0
calc.title("Kamal's Calculator")
operator = ''
text_input = StringVar()

txtDisplay = Entry(calc, font = ('helvetica', 25, 'bold'), textvariable = text_input, bd=28, insertwidth = 4,bg = "light grey", justify = 'right').grid(columnspan=4)

#ROW 1
btnC=Button(calc,padx=19,pady=6,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='C',bg="darkgoldenrod2",command=cleardisplay).grid(row=1,column=1)
btnAC=Button(calc,padx=22,pady=22,bd=1,fg='gray1',font = ('helvetica', 20, 'bold'),text='AC',bg="darkgoldenrod2",command=exit).grid(row=1,column=0)
btnON=Button(calc,padx=2,pady=6,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='ON',bg="darkgoldenrod2",command=cleardisplay).grid(row=1,column=2)
btndivide=Button(calc,padx=28,pady=6,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='/',bg="light grey",command=lambda:buttonClick('/')).grid(row=1,column=3)

#ROW 2
btn7=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='7',bg="azure",command=lambda:buttonClick(7)).grid(row=2,column=0)
btn8=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='8',bg="azure",command=lambda:buttonClick(8)).grid(row=2,column=1)
btn9=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='9',bg="azure",command=lambda:buttonClick(9)).grid(row=2,column=2)
btnmulti=Button(calc,padx=26,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='*',bg="light grey",command=lambda:buttonClick('*')).grid(row=2,column=3)

#ROW 3
btn4=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='4',bg="azure",command=lambda:buttonClick(4)).grid(row=3,column=0)
btn5=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='5',bg="azure",command=lambda:buttonClick(5)).grid(row=3,column=1)
btn6=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='6',bg="azure",command=lambda:buttonClick(6)).grid(row=3,column=2)
btnminus=Button(calc,padx=28,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='-',bg="light grey",command=lambda:buttonClick('-')).grid(row=3,column=3)

#ROW 4
btn1=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='1',bg="azure",command=lambda:buttonClick(1)).grid(row=4,column=0)
btn2=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='2',bg="azure",command=lambda:buttonClick(2)).grid(row=4,column=1)
btn3=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='3',bg="azure",command=lambda:buttonClick(3)).grid(row=4,column=2)
btnplus=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='+',bg="light grey",command=lambda:buttonClick('+')).grid(row=4,column=3)

#ROW 5
btn0=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='0',bg="azure",command=lambda:buttonClick(0)).grid(row=5,column=0)
btndot=Button(calc,padx=28,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='.',bg="azure",command=lambda:buttonClick('.')).grid(row=5,column=1)
btnx10=Button(calc,padx=2,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='*10',bg="azure",command=lambda:buttonClick('*10')).grid(row=5,column=2)
btnequal=Button(calc,padx=22,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='=',bg="light grey",command=equalsinput).grid(row=5,column=3)

#ROW 6
btnpara1=Button(calc,padx=28,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text='(',bg="azure",command=lambda:buttonClick('(')).grid(row=6,column=0)
btnpara2=Button(calc,padx=28,bd=1,fg='gray1',font = ('helvetica', 32, 'bold'),text=')',bg="azure",command=lambda:buttonClick(')')).grid(row=6,column=1)
btnANS=Button(calc,padx=20,bd=1,fg='gray1',state=DISABLED,font = ('helvetica', 32, 'bold'),text='A',bg="azure",command=print('DISABLED')).grid(row=6,column=2)
btnequal=Button(calc,padx=4,pady=4,bd=1,fg='gray1',font = ('helvetica', 30, 'bold'),text='N/A',bg="light grey",command=dont).grid(row=6,column=3)

calc.mainloop()









