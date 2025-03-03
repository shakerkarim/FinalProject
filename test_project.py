import pytest
import turtle
from project import move_red_turtle, move_green_turtle, check_winner

def test_move_red_turtle():
    test_turtle = turtle.Turtle()
    test_turtle.penup()
    test_turtle.goto(-200, 50)
    initial_position = test_turtle.xcor()
    move_red_turtle()
    assert test_turtle.xcor() == initial_position + 10, "Red Turtle did not move as expected."

def test_move_green_turtle():
    test_turtle = turtle.Turtle()
    test_turtle.penup()
    test_turtle.goto(-200, -50)
    initial_position = test_turtle.xcor()
    move_green_turtle()
    assert test_turtle.xcor() == initial_position + 10, "Green Turtle did not move as expected."

def test_check_winner_red():
    red_turtle = turtle.Turtle()
    green_turtle = turtle.Turtle()

    red_turtle.penup()
    green_turtle.penup()

    red_turtle.goto(200, 50)
    green_turtle.goto(100, -50)

    result = check_winner()
    assert result == "Red Turtle Wins!", f"Expected 'Red Turtle Wins!', got {result}"

def test_check_winner_green():
    red_turtle = turtle.Turtle()
    green_turtle = turtle.Turtle()

    red_turtle.penup()
    green_turtle.penup()

    red_turtle.goto(100, 50)
    green_turtle.goto(200, -50)

    result = check_winner()
    assert result == "Green Turtle Wins!", f"Expected 'Green Turtle Wins!', got {result}"

def test_no_winner():
    red_turtle = turtle.Turtle()
    green_turtle = turtle.Turtle()

    red_turtle.penup()
    green_turtle.penup()

    red_turtle.goto(50, 50)
    green_turtle.goto(50, -50)

    result = check_winner()
    assert result == "Nobody wins", f"Expected 'Nobody wins', got {result}"
