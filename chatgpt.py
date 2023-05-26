from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('./icons/ai_lt.ico')

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add text widget to get ChatGPT responses
my_text = Text(text_frame,
    bg="#343638",       # background "light grey"
    width=65,
    bd=1,
    fg="#d6d6d6",       # foreground color - text inside
    relief="flat",
    wrap=WORD,
    selectbackground="#1f538d")     # background of selection "blue"
my_text.grid(row=0, column=0)

# Create scroll bar widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
    command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)


root.mainloop()