import turtle
# define leaves of tree
def tree(d, s):
    if d <= 0:
        return
    turtle.forward(s)
    tree(d - 1, s * .8)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    turtle.backward(s)
n = 100
# set speed of draw 0-10-1
turtle.speed('fastest') # set speed
turtle.left(90)
turtle.forward(3 * n)
turtle.color("orange", "yellow")
turtle.left(126)
# turtle.begin_fill()
for i in range(5):
    turtle.forward(n / 5)
    turtle.right(144)
    turtle.forward(n / 5)
    turtle.left(72)
    turtle.end_fill()
    turtle.right(126)
    turtle.color("dark green")
    turtle.backward(n * 4.8)
# run method
tree(15, n)
turtle.backward(n / 5)
