from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)







window.mainloop()
