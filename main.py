from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# TODO : create a screen
src = Screen()
src.listen()
src.setup(width=800, height=600)
src.bgcolor('black')
src.title('Ping Pong Game')
src.tracer(0)

# TODO : create and move a paddle for Player A
player_r = Paddle((380, 0))

# TODO : create and move a paddle for Player B
player_l = Paddle((-385, 0))

# TODO : create a ball and make it move inside the screen
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    src.update()
    ball.move()
# TODO : check its collision with wall on up and down areas and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# TODO : check its collision with paddle and bounce back
    if (ball.distance(player_r) < 50 and ball.xcor() > 360) or (ball.distance(player_l) < 50 and ball.xcor() < -360):
        ball.bounce_x()

    # player_r.movement()
    # player_l.movement()
# TODO : check if it misses paddles
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    src.onkey(player_r.up, 'Up')
    src.onkey(player_l.up, 'w')
    src.onkey(player_r.down, 'Down')
    src.onkey(player_l.down, 's')

# TODO : scoreboard of player A
# TODO : scoreboard of player B
src.exitonclick()
