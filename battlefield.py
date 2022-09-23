
from dinosaur import Dinosaur
from robot import Robot

random_select = [{robot}, {dinosaur}] 

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
        self.random_select(Robot, Dinosaur)
        
        if Robot == True: 
            return self.robot.attack - self.dinosaur.health 
        self.robot.attack()
        
        if Dinosaur == True: 
            return self.dinosaur.attack - self.robot.health 
        self.dinosaur.attack()
        

        

       
        


    def display_winner(self):
        pass


