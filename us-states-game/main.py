import turtle
import pandas
from tkinter import *
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_label = turtle.Turtle()
state_label.hideturtle()
state_label.penup()

game_over = False

while not game_over:
    answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?")

    if answer_state == None:
        game_over = True
        break
        
    answer_state = answer_state.title()

    state_data = pandas.read_csv("50_states.csv")

    states = state_data["state"].to_list()
    current_state = state_data[state_data["state"] == answer_state]

    if answer_state in states:
        x_cor = int(current_state.x.iloc[0])
        y_cor = int(current_state.y.iloc[0])
        state_label.setpos(x_cor, y_cor)
        state_label.write(answer_state, align='center', font=('Arial', 8, 'bold'))

    else:
        messagebox.showerror(title="Incorrect", message="That is not a state. Try again.")

    

        # TODO: Record the correct guesses in a list

        # TODO: Keep track of the score


    turtle.mainloop()
