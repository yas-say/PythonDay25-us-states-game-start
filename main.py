import pandas
from turtle import Screen, Turtle

screen = Screen()
tim = Turtle()
tim2 = Turtle()
tim2.hideturtle()
tim2.penup()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
tim.shape("blank_states_img.gif")
tim.penup()

state_list = pandas.read_csv("50_states.csv")
count = 0
guessed_list = []
while count <= len(state_list):
    guess = screen.textinput(f"Guess the state name?{count}/{len(state_list)}", "Enter a state name:")
    print(guess.title())
    # guess = input(f"You have guessed {count}/{len(state_list)}; Enter a state name: ").title()
    # print(guess)
    state_subset = state_list[state_list["state"] == guess.title()]

    # print(f"row count {len(state_subset)}")
    # input()
    if len(state_subset) > 0:
        if guess.title() not in guessed_list:
            guessed_list.append(guess.title())
            print(state_subset)
            print(f"X = {int(state_subset.x)} and Y = {int(state_subset.y)}")
            count += 1
            tim2.goto(int(state_subset.x), int(state_subset.y))
            tim2.write(guess.title(), align="center", font=("Courier", 10, "normal"))

screen.exitonclick()
