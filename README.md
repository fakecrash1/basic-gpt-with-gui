# Basic ChatGPT App with a Graphical User Interface (GUI)

This application is a simple chatbot that uses OpenAI's GPT-3 model to generate responses. The chatbot communicates with the user via a graphical user interface (GUI) built with Tkinter and the customtkinter package.

## Features
- User can type messages to the chatbot
- Chatbot responses are displayed in a text box
- User can clear the conversation
- User can insert and save their OpenAI API key

## Requirements
- Python 3.6+
- Packages: `openai`, `tkinter`, `customtkinter`, `pickle`, `os`

## How to Use?

1. First, clone this repository to your local machine using `https://github.com/[Your Github Username]/[Your Repository Name].git`.
2. Navigate to the directory of the project.
3. Open a terminal in the project directory.
4. Create a virtual environment. You can create it by running `python -m venv gptgui` (or `python3 -m venv gptgui` depending on your system).
5. Activate the virtual environment; On Windows, use `gptgui\Scripts\activate`; On Unix or MacOS, use `source gptgui/bin/activate`.
6. Install the necessary Python packages by running `pip install -r requirements.txt` (or `pip3 install -r requirements.txt` depending on your system).
7. Run `python chatbot.py` (or `python3 chatbot.py` depending on your system) to start the application.
8. Enter your OpenAI API Key if it's your first time using the application. This will be saved for future use (on your local machine, don't worry). Get openai API Key: `https://platform.openai.com/account/api-keys`
9. Start chatting with the bot!

If you don't want to use a virtual environment, you can skip steps 4 and 5.

## Future Improvements
- Add support for multi-line user input
- Improve error handling

Please feel free to contribute to this project. If you encounter any problem or have any suggestions, please open an issue. 
