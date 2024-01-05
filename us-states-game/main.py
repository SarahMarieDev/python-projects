import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another stata's name?")

state_data = pandas.read_csv("50_states.csv")
current_state = state_data[state_data.state == answer_state]

print(current_state.x)

state_label = turtle.Turtle()
state_label.hideturtle()
state_label.penup()
state_label.write(answer_state, align='center', font=('Arial', 8, 'bold'))
state_label.position()

turtle.mainloop()
