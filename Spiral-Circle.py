import turtle
turtle.bgcolor("Black")
spiral = turtle.Turtle()
spiral.speed(200000)
for i in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    for color in ["red", "turquoise", "yellow", "green", "azure", "crimson", "blue", "gold", "silver", "limegreen", "skyblue", "teal", 
                  "cyan", "orange", "brown", "#964000", "#3B270C", "#0E4C92", "#1134A6", "black"]:
        spiral.pencolor(color)
        spiral.width(30)
        spiral.forward(i)
        spiral.left(20)
        spiral.right(10)
