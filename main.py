import pandas
from turtle import Turtle, Screen


screen = Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer = screen.textinput("Guess the state name?", "Enter a state name:")
print(answer)

state_list = pandas.read_csv()

screen.exitonclick()