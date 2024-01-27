import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
states = state_data["state"].to_list()

game_over = False
guesses = []

while len(guesses) < 50:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct", prompt="What is another state's name?")

    if answer_state is None:
        game_over = True
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missed_states = [state for state in states if state not in guesses]
        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    current_state = state_data[state_data["state"] == answer_state]

    if answer_state in states:
        if answer_state not in guesses:
            state_label = turtle.Turtle()
            state_label.hideturtle()
            state_label.penup()
            x_cor = int(current_state.x.iloc[0])
            y_cor = int(current_state.y.iloc[0])
            state_label.setpos(x_cor, y_cor)
            state_label.write(answer_state, align='center', font=('Arial', 8, 'bold'))
            guesses.append(answer_state)
        else:
            messagebox.showerror(title="Duplicate entry", message=f"{answer_state} has already been picked. Try again.")
    else:
        messagebox.showerror(title="Incorrect", message="That is not a state. Try again.")

if len(guesses) == 50:
    messagebox.showinfo(title="Game Over", message="You've guessed all 50 states.")
