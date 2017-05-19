from tkinter import *
import webbrowser

root = Tk()
root.title('Search')

String_Entry = Entry(root)
String_Entry.grid(row=0, column=0)

def search():
    url = "https://www.google.com/search?q=" + str(String_Entry.get())
    webbrowser.open(url)

def quit():
    root.destroy()

Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=1)

Quit_Button = Button(root, text='Quit', command=quit)
Quit_Button.grid(row=0, column=2)

mainloop()
