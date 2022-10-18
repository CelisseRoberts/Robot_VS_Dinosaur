from dinosaur import Dinosaur
from robot import Robot



class Battlefield: 
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur() 
        

    def run(self):
        self.greet()
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def greet(self):
        print("Hello!")
        

    def display_welcome(self):
        print("Welcome to the epic battle between Rosey and T Rex! Each player will battle til the end!")

    

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
           self.robot.attack(self.dinosaur)  
           if self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
           
    def display_winner(self):
        if self.robot.health > 0:
            print("Robot wins!")
        elif self.dinosaur.health > 0:
            print("Dinosaur wins!")

