from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
score = Score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.scoreboard()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        game_is_on=False
        score.game_over()
        
    #detect collision with tail
    #if head collides with any segment in the tail
    for segment in range(1,len(snake.segments)-1):
        if snake.head.distance(snake.segments[segment])<10:
            #trigger game_over
            game_is_on=False
            score.game_over()

        

screen.exitonclick()
