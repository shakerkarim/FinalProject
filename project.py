import turtle
import time

screen = turtle.Screen()
screen.title("Turtle Race with Timer")
screen.bgcolor("lightblue")

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200, 100)
finish_line.pendown()
finish_line.goto(200, -100)
finish_line.hideturtle()

red_turtle = turtle.Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.penup()
red_turtle.goto(-200, 50)

green_turtle = turtle.Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.penup()
green_turtle.goto(-200, -50)

timer_display = turtle.Turtle()
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(0, 120)

label_turtle = turtle.Turtle()
label_turtle.penup()
label_turtle.hideturtle()
label_turtle.goto(-240, 55)
label_turtle.write("Q", align="left", font=("Arial", 14, "bold"))
label_turtle.goto(-240, -45)
label_turtle.write("E", align="left", font=("Arial", 14, "bold"))

time_left = 15
game_over = False

def update_timer():
    global time_left, game_over
    if game_over:
        return
    if time_left > 0:
        time_left -= 1
        timer_display.clear()
        timer_display.write(f"Time Left: {time_left}s", align="center", font=("Arial", 16, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        handle_timeout()

def move_red_turtle():
    if not game_over:
        red_turtle.forward(10)
        check_winner()

def move_green_turtle():
    if not game_over:
        green_turtle.forward(10)
        check_winner()

def check_winner():
    global game_over
    if red_turtle.xcor() >= 200:
        game_over = True
        show_popup("Race Over", "Red Turtle Wins!")
    elif green_turtle.xcor() >= 200:
        game_over = True
        show_popup("Race Over", "Green Turtle Wins!")

def handle_timeout():
    global game_over
    if not game_over:
        game_over = True
        show_popup("Time's Up!", "Nobody Wins!")

def show_popup(title, message):
    screen.textinput(title, message)
    screen.bye()

screen.listen()
screen.onkey(move_red_turtle, "q")
screen.onkey(move_green_turtle, "e")

update_timer()
screen.mainloop()
