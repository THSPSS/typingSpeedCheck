import tkinter as tk

#how to get a WPM
#user typing two words than it gets a wpm
# wpm is word per minute(60seconds)


#make Gui
if __name__ == "main" :

    app = tk.Tk()
    scrollbar = tk.Scrollbar(app, orient=tk.VERTICAL)

    #set title of program and size
    app.title("check speed of typing")
    app.geometry("296*200")