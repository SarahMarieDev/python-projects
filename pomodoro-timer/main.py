from tkinter import *
import math

# CONSTANTS
ORANGE = "#FAA300"
PINK = "#F4538A"
BLUE = "#59D5E0"
BEIGE = "#FFF8DC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# TIMER RESET

# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=ORANGE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=BLUE)


# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text=marks)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 55), fg="black", bg=BEIGE)
timer_label.grid(column=1, row=0)
timer_label.config(pady=10)

checkmark_label = Label(text="", fg=BLUE, bg=BEIGE)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightbackground=BEIGE, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=BEIGE)
reset_button.grid(column=2, row=2)

window.mainloop()
