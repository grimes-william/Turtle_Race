# William Grimes
# Turtle Race
# Day 19 of 100 Days of Code

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
screen.setup(width=400, height=400)


# Get turtles on the starting line
def set_starting_pos(turtle, y_cor):
    turtle.penup()
    turtle.goto(x=-175, y=y_cor)


# Make the turtle racers
def create_racers():
    turtle_start = -100
    turtle_colors = ["red", "blue", "yellow", "purple", "pink", "black"]
    for _ in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_colors[_])
        set_starting_pos(new_turtle, turtle_start)
        turtle_start += 40
        turtles.append(new_turtle)


# Move the turtle, can be variable length between steps
def move_forward(turtle):
    move_distance = randint(1, 10)
    turtle.forward(move_distance)


# Get user input
def get_user_guess(screen_var):
    user_guess = screen_var.textinput("guess", "Make a guess:\nBlack\nPink\nPurple\nYellow\nBlue\nRed")
    return user_guess


# Determine if guess was right, display accordingly
def did_you_win(user_guess, winning_turtle):
    if user_guess.lower() == winning_turtle.lower():
        print(f"You got it!  {user_guess.title()} is the winner!")
    else:
        print(f"You lose!  You guessed {user_guess.title()} but the winner was {winning_turtle.title()}!")


# List to hold the racers
turtles =[]
create_racers()
winner = ""

race_over = False
guess = get_user_guess(screen)

# Loop until one turtle reaches end of screen
while not race_over:
    who_moves = randint(0, 5)
    move_forward(turtles[who_moves])
    if turtles[who_moves].xcor() >= 160:
        race_over = True
        winner = turtles[who_moves].fillcolor()

did_you_win(guess, winner)

screen.exitonclick()
