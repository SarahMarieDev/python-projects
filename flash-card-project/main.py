from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card.create_image(400, 263, image=card_front_img)
card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bd=0)
known_button.grid(column=1, row=1)

window.mainloop()
