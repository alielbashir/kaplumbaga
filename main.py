import turtle

def kare_ciz():
    kaplumbaga = turtle.Turtle()
    for i in range(4):
        kaplumbaga.forward(100)
        kaplumbaga.right(90)

def ucgen_ciz():
    kaplumbaga = turtle.Turtle()
    for i in range(3):
        kaplumbaga.forward(100)
        kaplumbaga.right(90)

ucgen_ciz()
# kare_ciz()

turtle.exitonclick()
