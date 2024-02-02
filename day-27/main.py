from tkinter import *


def button_clicked():
    new_text = text_input.get()  # gets text in entry
    my_label.config(text=new_text)
    text_input.delete(0, len(new_text))  # clears the text from the text entry field


def clear_button():
    new_text = text_input.get()
    text_input.delete(0, len(new_text))


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click To Change Text", command=button_clicked)
button.grid(column=1, row=1)
#button.pack()
clear_button = Button(text="Clear", command=clear_button)
#clear_button.pack()
clear_button.grid(column=2, row=0)

# Entry
text_input = Entry(width=30)
text_input.insert(END, string="Some text to begin with")  # add text to begin with
#text_input.pack()
text_input.grid(column=3, row=2)

window.mainloop()
