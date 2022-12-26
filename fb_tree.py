import turtle

bg = turtle.Screen()
bg.bgcolor("sky blue")

tree = turtle.Turtle()
tree.color("forest green")

tree.penup()

trunk = turtle.Turtle()
trunk.color("chocolate")
trunk.penup()

def make_tree_segment(size, top_position):
    tree.setposition(0,top_position)
    tree.begin_fill()
    tree.setposition(size, top_position-size)
    tree.setposition(-size, top_position-size)
    tree.setposition(0, top_position)
    tree.end_fill()
    tree.setposition(0,500)
    trunk.setposition(-size/12, top_position-size)
    trunk.begin_fill()
    trunk.setposition(size/12, top_position-size)
    trunk.setposition(size/12, top_position-size-size/6)
    trunk.setposition(-size/12, top_position-size-size/6)
    trunk.setposition(-size/12, top_position-size)
    trunk.end_fill()
    trunk.setposition(0,500)

for i in range(12):
    make_tree_segment(50+i*20, 300-(i*30))

turtle.done()