import turtle

trevor = turtle.Turtle()

trevor.speed(100)
trevor.shape('turtle')

def set_pos(x , y):
    trevor.penup()
    trevor.setpos(x,y)
    trevor.pendown()

set_pos(0, -100)

trevor.left(90)

def fractal(t, x):
    if (x<1):
        return
    else:
        t.forward(x)
        t.left(30)
        fractal(t, x*0.7)
        t.right(60)
        fractal(t, x*0.7)
        t.left(30)
        t.back(x)

fractal(trevor, 150)
