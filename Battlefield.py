from random import random
from dinosaur import Dinosaur
from robot import Robot

 

class Battlefield: 
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur() 
        

    def run(self):
        self.greet()
        self.display_welcome()
        

    def greet(self):
        print("Hello!")
        

    def display_welcome(self):
        print("Welcome to the epic battle between Rosey and T Rex!")

    def battle_phase(self):
        self.robot.attack()
        self.dinosaur.attack()
        self.random_select(Robot, Dinosaur)

        if Robot:
            return self.robot.attack - self.dinosaur.health 

        elif Dinosaur:
            return self.dinosaur.attack - self.robot.health 
        


    def display_winner(self):
        pass


