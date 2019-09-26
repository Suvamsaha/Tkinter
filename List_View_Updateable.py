from tkinter import Tk, mainloop
from tkinter.ttk import Button, Label


def label_inc():
    global i
    i = i + 1
    label.configure(text='Counting UP: {}'.format(i))
    root.update_idletasks()


def label_dec():
    global i
    i = i - 1
    label.configure(text='Counting Down: {}'.format(i))
    root.update_idletasks()


def close_window():
    root.destroy()


if __name__ == '__main__':
    i = 0
    root = Tk()
    root.geometry("250x80")
    root.title("Up & Down Counter")
    label = Label(root)
    label.place(x=5, y=10)
    label.configure(text='Count: 0')
    Button(root, text=' Count up ', command=label_inc).place(x=5, y=40)
    Button(root, text='Count down', command=label_dec).place(x=85, y=40)
    Button(root, text='Exit', command=close_window).place(x=170, y=40)
    mainloop()
