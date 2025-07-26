import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# objects

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # check if player is on the top
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_increment()

    # update car manager
    car_manager.do_every_frame()

    # check collisions
    for car in car_manager.cars:
        if player.distance(car) < 30:
            # game_is_on = False
            time.sleep(.5)
            scoreboard.lives_decrement()
            player.reset_position()

    if scoreboard.lives == 0:
        scoreboard.render_game_over()
        game_is_on = False


screen.exitonclick()
