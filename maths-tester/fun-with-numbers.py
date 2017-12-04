#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import random
import datetime


def question_window():
    root = Toplevel(start_window)
    root.geometry('2000x2000')

    top_frame = Frame(root)
    top_frame.pack(side=TOP)

    welcome_label = Label(top_frame,text="\nHaving fun with maths..\nTake a test..!!",height=4,width=80,font=(None,20))
    welcome_label.pack(pady=20,side=LEFT)

    Timer_label = Label(top_frame,font=(None,20))
    Timer_label.pack(side=LEFT)

    middle_frame = Frame(root)
    middle_frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack()

    left_frame = Frame(middle_frame)
    left_frame.pack(side=LEFT)

    right_frame = Frame(middle_frame)
    right_frame.pack(side=LEFT)

    list_of_answers = []
    entry_list = [str(x) for x in range(10)]

    for i in range(10):

        operator_list = [' x ', ' ÷ ', ' + ', '   ̶ ']
        operator = random.choice(operator_list)

        if operator == ' + ':
            number_list = range(50,345)
            first_number = random.choice(number_list)
            second_number = random.choice(number_list)
            answer = first_number + second_number

        elif operator == '   ̶ ':
            number_list = range(20,345)
            first_number = random.choice(number_list)
            number_list = range(first_number)
            second_number = random.choice(number_list)
            answer = first_number - second_number

        elif operator == ' x ':
            number_list = range(101)
            first_number = random.choice(number_list)
            number_list = range(2,11)
            second_number = random.choice(number_list)
            answer = first_number * second_number

        else:
            number_list = range(0,100)
            first_number = random.choice(number_list)
            while(1):
                number_list = range(2, 20)
                second_number = random.choice(number_list)
                if first_number/second_number == first_number//second_number:
                    answer = first_number // second_number
                    break

        list_of_answers.append(answer)

        frame = Frame(left_frame)
        frame.pack()

        Label_first_number = Label(frame,text=first_number,font=(None,44))
        Label_first_number.grid(row=0,column=0)

        Label_operator = Label(frame,text=operator,font=(None,44))
        Label_operator.grid(row=0,column=1)

        Label_second_number = Label(frame,text=second_number,font=(None,44))
        Label_second_number.grid(row=0,column=2)

        frame = Frame(right_frame)
        frame.pack()

        Label_equals_operator = Label(frame,text=' = ',font=(None,44))
        Label_equals_operator.grid(row=0,column=3)

        entry_list[i] = Entry(frame,font=(None,35))
        entry_list[i].grid(row=0,column=4)

    def clock():
        elapsed = end - datetime.datetime.now()
        m,s = elapsed.seconds//60,int(elapsed.seconds % 60)
        if m <= 0 and s <= 0:
            Timer_label.config(text='TIME OVER')
            submit_button.invoke()
            return
        Timer_label.config(text=datetime.time(0,m,s))
        root.after(1000,clock)

    end = datetime.datetime.now() + datetime.timedelta(minutes=10)
    clock()

    def taking_entries():
        user_ans = []
        for i in range(10):
            ans = entry_list[i].get()
            user_ans.append(ans)
        marks = 0
        for i in range(10):
            if str(list_of_answers[i]) == user_ans[i]:
                marks += 1
        new_window = Toplevel(root)
        new_window.geometry('500x300+700+300')
        finish_label = Label(new_window,text='\nSCORE\n {} / 10\n'.format(marks),font=(None,30))
        finish_label.pack()
        exit_button = Button(new_window,text="FINISH",command=root.quit,font=(None,25))
        exit_button.pack()

    submit_button = Button(bottom_frame,text="SUBMIT", height=2, width=15,command=taking_entries,font=(None,25))
    submit_button.pack(pady=40)


# start
start_window = Tk()
start_window.geometry('500x250+700+300')

start_label = Label(start_window,text='\nWanna Test Your Maths Skills..??\nWhy Not Take a Test..!!\n',font=(None,20))
start_label.pack()

start_button = Button(start_window,text='START',font=(None,25),command=question_window)
start_button.pack()

start_window.mainloop()