"""
Text Editor GUI

This program demonstrates a basic text editor implemented using the Tkinter GUI library in Python.
It allows users to open, edit, and save text files. The main features include:

1. Open File: Opens a file dialog for selecting and loading a text file into the Text widget.
2. Save File: Opens a file dialog for selecting a location and saving the content of the Text widget to a text file.

The program utilizes the Tkinter framework to create the main window, buttons, and text editing area.
File operations are handled using the askopenfilename and asksaveasfilename functions from tkinter.filedialog.
The text editing area is implemented using the Text widget, and the program ensures proper resizing of the interface.

Author: Mahmoud Khalil
Date: 11-12-2023
"""

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """
    Open a file dialog to select and load a text file into the Text widget.
    """
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    # Clear existing text in the Text widget
    text_edit.delete("1.0", END)
    
    # Read the contents of the selected file and insert it into the Text widget
    with open(file_path, "r") as in_file:
        text = in_file.read()
        text_edit.insert(END, text)
    
    # Set the file_var to the selected file path
    file_var.set(file_path)

def save_file():
    """
    Open a file dialog to select a location and save the content of the Text widget to a text file.
    """
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    # Get the content of the Text widget
    text = text_edit.get("1.0", END)
    
    # Write the content to the selected file
    with open(file_path, "w") as out_file:
        out_file.write(text)
    
    # Set the file_var to the saved file path
    file_var.set(file_path)

# Create the main Tkinter window
window = Tk()
window.title("Text Editor")

# Configure weights for resizing
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# StringVar to hold the current file path
file_var = StringVar()

# Frame for buttons
frame_buttons = Frame(master=window)
open_button = Button(frame_buttons, text="Open File", command=open_file)
save_button = Button(frame_buttons, text="Save File", command=save_file)

frame_buttons.grid(column=0, row=0, sticky='ns', padx=1, pady=1)
open_button.grid(column=0, row=1, sticky='ew')
save_button.grid(column=0, row=2, sticky='ew')

# Frame for text editing
frame_text = Frame(master=window)
frame_text.grid_rowconfigure(0, weight=1)
frame_text.grid_columnconfigure(0, weight=1)
text_edit = Text(master=frame_text)

frame_text.grid(column=1, row=0, sticky='nsew', padx=3, pady=3)
text_edit.grid(column=0, row=0, sticky='nsew')

# Start the Tkinter event loop
window.mainloop()
