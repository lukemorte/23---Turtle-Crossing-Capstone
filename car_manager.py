from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CHANCE_FOR_NEW_CAR = 0.1


class Car(Turtle):

    speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()        
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 3)
        self.penup()
        self.setx(325)
        self.set_random_y()

    def set_random_y(self):
        self.sety(random.choice(range(-200, 200, STARTING_MOVE_DISTANCE)))

    def move(self):
        self.setx(self.xcor() - Car.speed)


class CarManager:

    def __init__(self):
        self.cars: Car = []

    def do_every_frame(self):
        self.try_add_car()

        for car in self.cars:
            car.move()
            if car.xcor() < -340:
                car.hideturtle()
                self.cars.remove(car)
                del car

    def try_add_car(self):
        if random.random() < CHANCE_FOR_NEW_CAR:
            self.add_car()

    def add_car(self):
        car = Car()
        self.cars.append(car)

    def speed_up(self):
        Car.speed += MOVE_INCREMENT
