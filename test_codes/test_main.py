from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('../icons/ai_lt.ico')

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

filename = "api_key"

# Buttons (send, clear, api, save_key)
def send():
    if chat_entry.get():
        try:
            if os.path.isfile(filename):
                input_file = open(filename, 'rb')
                key = pickle.load(input_file)
                # Add user message to the chat
                my_text.insert(END, "User: \n\n"+ chat_entry.get() + "\n")
                #my_text.insert(END, "Thinking...")
                # Define API Key to ChatGPT
                openai.api_key = key
                # Create an instance
                openai.Model.list()
                # Define Querry / Response
                response = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt=chat_entry.get(),
                            max_tokens=320,
                            n=1,
                            stop=None,
                            temperature=0.5,
                            frequency_penalty=0.5,
                            presence_penalty=0.5,
                            best_of=1,
                            )
                my_text.insert(END,"\n\nChatGPT: "+ (response["choices"][0]["text"]))
                my_text.insert(END,"\n\n\n")
            else:
                input_file = open(filename, 'wb')
                input_file.close()
                my_text.insert(END, "\n> Error: you need a valid API Key to use application,\n get Key from here: [https://platform.openai.com/account/api-keys]")
        except Exception as e:
            my_text.insert(END, f"\n\n There was an error: \n{e}")
    chat_entry.delete(0, END)   # Clear chat entry

def clear():
    my_text.delete(1.0, END)    # Clear chat histoy
#    chat_entry.delete(0, END)   # Clear entry history

def api():
    try:
        if os.path.isfile(filename):
            input_file = open(filename, 'rb')
            key = pickle.load(input_file)
            api_entry.insert(END, key)
        else:
            input_file = open(filename, 'wb')
            input_file.close()
    # Error handling
    except Exception as e:
        my_text.insert(END, f"\n\n There was an error: \n{e}")

    root.geometry('600x730')    # resize app to 730 at y
    api_frame.pack(pady=30)

def save_key():
    filename = "api_key"
    
    try:
        output_file = open(filename, 'wb')
        pickle.dump(api_entry.get(), output_file)
        
        api_entry.delete(0, END)
        
        api_frame.pack_forget()
        root.geometry('600x600')    # resize app to 600 at y
    # Error handling
    except Exception as e:
        my_text.insert(END, f"\n\n There was an error: \n{e}")

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

# Entry Widget to type stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
    placeholder_text="Type something to ChatGPT...",
    width=535,
    height=50,
    border_width=1)
chat_entry.pack(pady=10)

# Function to be called when Enter is pressed
def enter_pressed(event):
    send()

# Function to be called when Shift+Enter is pressed
def shift_enter_pressed(event):
    # Add a newline character to the current chat entry
    chat_entry.insert(END, '\n')

# Bind the functions to the Entry widget
chat_entry.bind('<Return>', enter_pressed)
chat_entry.bind('<Shift-Return>', shift_enter_pressed)

# Create buttons frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)


# Configure grid weights / 4 column - columnspan
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)


# send button
submit_button = customtkinter.CTkButton(button_frame,
    text="Send message",
    command=send)
submit_button.grid(row=0, column=0, columnspan=4, sticky='we', padx=10, pady=5)

# clear button
clear_button = customtkinter.CTkButton(button_frame,
    text="Clear conversation",
    command=clear)
clear_button.grid(row=1, column=0, columnspan=2, sticky='we', padx=10, pady=5)

# Api key button
api_button = customtkinter.CTkButton(button_frame,
    text="Insert API Key",
    command=api)
api_button.grid(row=1, column=2, columnspan=2, sticky='we', padx=10, pady=5)

# Add API Key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=20)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame,
    placeholder_text="Enter your API Key",
    width=335, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

# Add API Button
api_save_button = customtkinter.CTkButton(api_frame,
    text="Save key",
    command=save_key)
api_save_button.grid(row=0, column=1, padx=10, pady=20)



root.mainloop()