import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#how to get a WPM
#user typing two words than it gets a wpm
# wpm is word per minute(60seconds)
#check input word and check time(seconds)

#start timer
def seconds_timer():
    global second
    #set flag
    entryLen = True if len(entry.get()) else False
    temp = int(second.get())
    if entryLen:
        while temp > -1 :
            second.set("{0:2d}".format(temp))
            app.update()
            time.sleep(1)



            if temp == 0:
                messagebox.showinfo("Minute End" , "Time's up")

            temp -= 1

#if given word and written word has not same
#then change the color of given word with red


#make Gui
if __name__ == "__main__":

    app = tk.Tk()
    #set title of program and size
    app.title("check speed of typing")
    app.geometry("296x200")

    #adding timer
    second = StringVar()


    second.set("60")

    secondEntry = Entry(app , width=3 , font=("Arial", 18,""),textvariable=second)
    secondEntry.grid(row=0 , column=0)

    #text widget
    testText = tk.Text(app, height=5, width=30)
    testText.grid(row=1 , columnspan=7)

    testText.insert(tk.INSERT , "apple applause more column tree")

    btn = Button(app, text='Set Time Countdown', bd='5',
                 command=seconds_timer)
    btn.grid(row=0 , column=1)
    #user input entry
    entry = tk.Entry(app, width=20)
    entry.grid(row=2 , columnspan=7)

    app.mainloop()