import turtle

# Prepare the screen
wind = turtle.Screen() 
wind.title("Pong by MYA") 
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0) # Prevent the screen from updating itself automatically allowing me to have control

# Prepare the first racket
firstRacket = turtle.Turtle()
firstRacket.speed(0) # This is the speed of drawing the racket on the screen
firstRacket.shape("square")
firstRacket.color("blue")
firstRacket.shapesize(stretch_wid=5, stretch_len=1) # Default = 20 pixels, here it is 5*20
firstRacket.penup() # Prevents lines behind the racket
firstRacket.goto(-350, 0) # Locate the racket

# Prepare the second racket
secondRacket = turtle.Turtle()
secondRacket.speed(0)
secondRacket.shape("square")
secondRacket.color("red")
secondRacket.shapesize(stretch_wid=5, stretch_len=1) 
secondRacket.penup()
secondRacket.goto(350, 0) 

# Prepare the ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.2 # The rate of change is 2.5 pixels
ball.dy = -0.2

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle() # Hide the object
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("courier",24,"normal"))

# Movement functions
def firstRacketUp():
    y = firstRacket.ycor() # Returns the y-cord of the object
    y += 20
    firstRacket.sety(y) # Change the y-cord

def firstRacketDown():
    y = firstRacket.ycor() 
    y -= 20
    firstRacket.sety(y) 

def secondRacketUp():
    y = secondRacket.ycor() 
    y += 20
    secondRacket.sety(y) 

def secondRacketDown():
    y = secondRacket.ycor() 
    y -= 20
    secondRacket.sety(y) 

# Keyboard bindings
wind.listen() # Waits for a keyboard stroke
wind.onkeypress(firstRacketUp, 'w') # Call firstRacketUp() if 'w' was hit, 'W' is wrong
wind.onkeypress(firstRacketDown, 's')
wind.onkeypress(secondRacketUp, 'Up') 
wind.onkeypress(secondRacketDown, 'Down') 

while True:
    wind.update() # Constant update
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borders check
    if ball.ycor() > 290: # 290 because the ball is 20 pixels and half of it is 10
        ball.sety(290)
        ball.dy *= -1 # Revert

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()

        score.write("Player 1: {} Player 2: {}".format(score1,score2), align='center', font=('courier',24,'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1,score2), align='center', font=('courier',24,'normal'))

    # If hit by a racket
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < secondRacket.ycor() + 40 and ball.ycor() > secondRacket.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < firstRacket.ycor() + 40 and ball.ycor() > firstRacket.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1

