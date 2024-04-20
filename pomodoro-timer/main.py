from tkinter import *
import math

# CONSTANTS
BLUE = "#496989"
DKGREEN = "#58A399"
GREEN = "#A8CD9F"
LTGREEN = "#E2F4C5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# TIMER RESET

# TIMER MECHANISM
def start_timer():
    count_down(WORK_MIN * 60)


# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LTGREEN)

canvas = Canvas(width=200, height=224, bg=LTGREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 55), fg=DKGREEN, bg=LTGREEN)
timer_label.grid(column=1, row=0)
timer_label.config(pady=10)

checkmark_label = Label(text="✔", fg=DKGREEN, bg=LTGREEN)
checkmark_label.grid(column=1, row=3)
checkmark_label.config(pady=10)

start_button = Button(text="Start", highlightbackground=LTGREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=LTGREEN)
reset_button.grid(column=2, row=2)

window.mainloop()
