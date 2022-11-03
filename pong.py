import turtle as t 

window=t.Screen()
window.title("Pong Game")
window.bgcolor("grey")
window.setup(width=800, height=600)
window.tracer(0)

leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

pen=t.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center",font=('Roboto', 24,'normal'))

player_1_score = 0
player_2_score = 0


def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)
    
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballxdirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection= ballxdirection *-1
        player_1_score = player_1_score +1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {} ".format(player_1_score,player_2_score),align="center",font=('Monaco',24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ballxdirection = ballxdirection *-1
        player_2_score = player_2_score +1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {} ".format(player_1_score,player_2_score),align="center",font=('Monaco',24,"normal"))

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection *= -1
        ballxdirection -=0.15

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection *= -1
        ballxdirection +=0.15
