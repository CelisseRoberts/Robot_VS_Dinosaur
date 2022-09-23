 

class Dinosaur:
    def __init__(self):
        self.dinosaur = "T Rex"
        self.health = 100 
        self.attack_power = 20 
        

    def attack(self, robot):
        robot.health -= self.attack_power 
        print(f'{self.dinosaur} attacked {robot.robot}) Robot health = {robot.health}')
        

