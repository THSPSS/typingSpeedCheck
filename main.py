import tkinter as tk

#how to get a WPM
#user typing two words than it gets a wpm
# wpm is word per minute(60seconds)
#check input word and check time(seconds)

#start timer

#if given word and written word has not same
#then change the color of given word with red


#make Gui
if __name__ == "__main__":

    app = tk.Tk()
    #set title of program and size
    app.title("check speed of typing")
    app.geometry("296x200")

    #adding timer

    #text widget
    testText = tk.Text(app, height=5, width=30)
    testText.grid(row=0 , columnspan=7)

    testText.insert(tk.INSERT , "apple applause more column tree")


    #user input entry
    entry = tk.Entry(app, width=20)
    entry.grid(row=1 , columnspan=7)

    app.mainloop()