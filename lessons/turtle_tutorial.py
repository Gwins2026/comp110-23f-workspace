"""Turtle Tutorial Practice."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

"""Excersize 1"""

leo.forward(50)
leo.right(30)
leo.left(40)
done()

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)

"""Excersize 2"""

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i += 1

"""GoTo Penup and Pendown"""

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

"""Pen Color"""

loe.color(99, 204, 250)

"""Fill Color"""

leo.begin_fill()
# code for shape to be filled
leo.end_fill()

"""Excersize 3"""









def main() -> none:
    """The entrypoint of my scene."""
    jan: Turtle = Turtle()
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()
 
# TODO: Define the procedures for other components in your scene here.
 
# TODO: Use the __name__ is "__main__" idiom shown in class


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -5, 5, 10)
    draw_square(ertle, -10, 10, 20)
    draw_square(ertle, -15, 15, 30)
    draw_square(ertle, -20, 20, 40)
    done()
    # Challenge: Try rewriting those four repeated calls in a loop
    # and using arithmetic expressions to calculate each of the arguments
    # based on your counter variable's value rather than hard coded int
    # literals. For example, the first argument could be: (i + 1) * -5


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)  # Disable delay in tracing
    ...  # TODO: your code
    update()  # Now update the rendering
    done()