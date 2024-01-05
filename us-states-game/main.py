import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_label = turtle.Turtle()
state_label.hideturtle()
state_label.penup()


answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?").title()

state_data = pandas.read_csv("50_states.csv")

states = state_data["state"].to_list()
current_state = state_data[state_data["state"] == answer_state]
x_cor = int(current_state.x.iloc[0])
y_cor = int(current_state.y.iloc[0])

if answer_state in states:
    state_label.setpos(x_cor, y_cor)
    state_label.write(answer_state, align='center', font=('Arial', 8, 'bold'))

else:
    print("Incorrect")

# TODO: Use a loop to allow the user to keep guessing

# TODO: Record the correct guesses in a list

# TODO: Keep track of the score


turtle.mainloop()
