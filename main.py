from tkinter import *
from tkinter import colorchooser
import pyperclip

chosen_colour = ''

def click():
    global chosen_colour
    chosen_colour = colorchooser.askcolor()
    window.configure(bg=chosen_colour[1])
    heading.configure(bg=chosen_colour[1])
    update_color_labels()

def update_color_labels():
    rgb_code.config(text=f"RGB code: {chosen_colour[0][0]:.0f}, {chosen_colour[0][1]:.0f}, {chosen_colour[0][2]:.0f} (click to copy)")
    hex_code.config(text=f"HEX code: {chosen_colour[1]} (click to copy)")

def rgb_click():
    pyperclip.copy(f'{chosen_colour[0][0]:.0f}, {chosen_colour[0][1]:.0f}, {chosen_colour[0][2]:.0f}')

def hex_click():
    pyperclip.copy(f'{chosen_colour[1]}')


window = Tk()
window.geometry('500x420')

icon = PhotoImage(file="Color_picker.png")
window.iconphoto(True, icon)
window.title("Simple Colour Picker Python")

heading = Label(window, text="Simple Color Picker", font=('Impact', 40, 'bold'))
heading.pack(pady=40)

button = Button(window, text="Choose color", font=(20), command=click)
button.pack()

button_frame = Frame(window, bg="black")
button_frame.pack( pady=50, padx=35)

rgb_code = Button(button_frame, text="RGB code: ", font=("Arial", 10), command=rgb_click)
rgb_code.pack()

hex_code = Button(button_frame, text="HEX code: ", font=("Arial", 10), command=hex_click)
hex_code.pack()

window.mainloop()
