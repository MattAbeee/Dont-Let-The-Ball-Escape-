import turtle
wn = turtle.Screen()
wn.title("Dont Let The Ball Escape!")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#*******************************************************************************
#
#
#
#*******************************************************************************


#Left Paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square") #CHANGE
paddle_left.color("red")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

#Down Paddle
paddle_down = turtle.Turtle()
paddle_down.speed(0)
paddle_down.shape("square") #CHANGE
paddle_down.color("red")
paddle_down.shapesize(stretch_wid=1, stretch_len=5)
paddle_down.penup()
paddle_down.goto(0, -250)


# Up Paddle
paddle_up = turtle.Turtle()
paddle_up.speed(0)
paddle_up.shape("square") #CHANGE
paddle_up.color("red")
paddle_up.shapesize(stretch_wid=1, stretch_len=5)
paddle_up.penup()
paddle_up.goto(0,  250)



#Right Paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square") #CHANGE
paddle_right.color("red")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(+350, 0)

#Ball In Middle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") #CHANGE
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#Ball In Middle #2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle") #CHANGE
ball2.color("white")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -1
ball2.dy = -1


#Functions to move stuff ;P

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

def paddle_up_right():
    x = paddle_up.xcor()
    x += 20
    paddle_up.setx(x)

def paddle_up_left():
    x = paddle_up.xcor()
    x -= 20
    paddle_up.setx(x)

def paddle_down_right():
    x = paddle_down.xcor()
    x += 20
    paddle_down.setx(x)

def paddle_down_left():
    x = paddle_down.xcor()
    x -= 20
    paddle_down.setx(x)

# Bind Keyboard
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")
wn.onkeypress(paddle_up_right, "Right")
wn.onkeypress(paddle_up_left, "Left")
wn.onkeypress(paddle_down_right, "d")
wn.onkeypress(paddle_down_left, "a")

#TURN CAPS LOCK OFF TO MOVE ^



#MAIN LOOP :)
while True:
    wn.update()

    # Ball Moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)


 # border
    if ball.ycor() >=  360:
        turtle.clearscreen()
        turtle.write("You Lost!", font=("Arial", 25, "bold"))
        

    if ball.xcor() >=  360:
        turtle.clearscreen()
        turtle.write("You Lost!", font=("Arial", 25, "bold"))
        
# Hit Paddle
    if paddle_left.distance(ball) < 25:
        ball.dx *= -1
    if paddle_right.distance(ball) < 25:
        ball.dx *= -1
    if paddle_down.distance(ball) < 25:
        ball.dy *= -1
    if paddle_up.distance(ball) < 25:
        ball.dy *= -1

    if paddle_left.distance(ball2) < 25:
        ball2.dx *= -1
    if paddle_right.distance(ball2) < 25:
        ball2.dx *= -1
    if paddle_down.distance(ball2) < 25:
        ball2.dy *= -1
    if paddle_up.distance(ball2) < 25:
        ball2.dy *= -1
        
