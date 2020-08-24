import turtle


def draw_square(some_turtle) :

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle() :
    window = turtle.Screen()
    window.bgcolor("YELLOW")
    

    rob = turtle.Turtle()
    rob.shape("turtle")
    rob.color("RED")
    for i in range(1,80):
        draw_square(rob)
        rob.right(5)





    window.exitonclick()

draw_circle()





