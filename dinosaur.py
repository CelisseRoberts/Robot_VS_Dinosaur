
class Dinosaur:
    def __init__(self):
        self.name = "T Rex"
        self.health = 100 
        self.attack_power = 20 
        

    def attack(self, robot):
        robot.health -= self.attack_power 
        print(f'{self.name} attacked {robot.name}. Robot health = {robot.health}')
        

