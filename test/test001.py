# test001.py
# AIzaSyDAubPeGIc8nM8CR-yA4MOwWacmpHkz0X0
# 🏠

import tkinter
import customtkinter

text = 'I Wasted $1000 On A Tactical Stroller'

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

def foo(text):
    if len(text) >= 41:
        text = text[:35]+"..."
        print(text)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text=foo(text), command=button_function, width=250)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()