import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import *
windows = tk.Tk()
windows.title("Пошукова система")


text_field = ttk.Entry(windows, width=30)
text_field.grid(row=3, column=1)
search_engine = StringVar()
search_engine.set('google')


def search():
    if text_field.get().strip():
        if search_engine.get() == 'google':
            webbrowser.open(
                url="https://www.google.com.ua/search?q=" + text_field.get())
    elif search_engine.get() == 'yandex':
        webbrowser.open(
            url="https://yandex.ua/search/?text=" + text_field.get())


def search_info():
    search()


def enterBtn(event):
    search()


text_field.focus()
text_field.bind("<Return>", enterBtn)
btn_search = ttk.Button(windows, text="Search", width=15, command=search_info)
btn_search.grid(row=3, column=2)

radio_google = ttk.Radiobutton(
    windows, text="Google", value='google', variable=search_engine)
radio_google.grid(row=1, column=1, sticky=W)


radio_yandex = ttk.Radiobutton(
    windows, text="Yandex", value='yandex', variable=search_engine)
radio_yandex.grid(row=1, column=1, sticky=E)


windows.wm_attributes("-topmost", TRUE)

windows.mainloop()
