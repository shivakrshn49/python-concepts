import turtle

turtle.setup(500, 500)

window = turtle.Screen()
window.title("Event Handling")
window.bgcolor("lightblue")

nathan = turtle.Turtle()

def moveForward():
    nathan.forward(50)
    
def moveLeft():
    nathan.left(50)

def moveRight():
    nathan.right(50)

def moveBackward():
    nathan.backward(50)

def start():
    window.onkey(moveForward, "Up")
    window.onkey(moveLeft, "Left")
    window.onkey(moveRight, "Right")
    window.onkey(moveBackward, "Down")
    window.listen()
    # window.mainloop()

if __name__ == "__main__":
    start()


    