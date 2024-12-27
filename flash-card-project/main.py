from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    print("No file found")
    exit()

to_learn = word_data.to_dict(orient="records")
current_card = {}
is_known = False

def next_card():
    global current_card, flip_timer, is_known
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_card["French"], fill="black")
    card.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")
    card.itemconfig(card_background, image=card_back_img)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = card.create_image(400, 263, image=card_front_img)
card_title = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card, bd=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known, bd=0)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
