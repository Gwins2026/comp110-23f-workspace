"""TODO: Describe your scene program."""

__author__ = "730561330"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    jan: Turtle = Turtle()
    jan.speed(50)
    sky(jan)
    clouds(jan, -300, 200)
    clouds(jan, -50, 100)
    clouds(jan, 250, 250)
    ocean(jan)
    i: int = 0
    x: int = -350
    y: int = -50
    while i < 5:
        waves(jan, x, y)
        x += 50
        y -= 75
        i += 1
    waves(jan, -25, -150)
    waves(jan, -75, -75)
    jan.goto(25, -400)
    jan.pendown()
    jan.fillcolor(221, 226, 90)
    jan.begin_fill()
    jan.circle(475, -180)
    jan.end_fill()
    done()


def sky(a_turtle: Turtle) -> None:
    """Draws the sky of a nice day on the turtle picture."""
    a_turtle.begin_fill()
    a_turtle.fillcolor(90, 193, 226)
    draw_square(a_turtle, -400, 800, 830)
    a_turtle.end_fill()
    a_turtle.penup()


def clouds(a_turtle: Turtle, x: float, y: float) -> None:
    """Distributes a puffy cloud in the sky at a given x, y coordinate."""
    a_turtle.setheading(0.0)
    a_turtle.goto(x, y)
    i: int = 0
    z: int = 25
    while i < 3:
        a_turtle.pendown() 
        a_turtle.begin_fill()
        a_turtle.fillcolor(236, 242, 248)
        a_turtle.circle(25, 360)
        a_turtle.end_fill()
        a_turtle.penup()
        a_turtle.goto(x + z, y - z)
        z *= -1
        i += 1
    a_turtle.goto(x - z, y - z)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor(236, 242, 248)
    a_turtle.circle(25, 360)
    a_turtle.end_fill()
    a_turtle.penup()


def ocean(a_turtle: Turtle) -> None:
    """Draws the nice ocean on a warm summer's day with a few waves."""
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor("blue")
    draw_square(a_turtle, -400, -30, 600)
    a_turtle.end_fill()
    a_turtle.penup()
    a_turtle.right(90)
    

def waves(a_turtle: Turtle, x: float, y: float) -> None:
    """Creates waves in the ocean."""
    a_turtle.goto(x, y)
    a_turtle.pencolor(30, 142, 244)
    i: int = 0
    while i < 3:
        a_turtle.pendown() 
        a_turtle.circle(25, 180)
        a_turtle.left(180)
        i += 1
    a_turtle.penup()
    a_turtle.pencolor("black")


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1

    
if __name__ == "__main__":
    main()