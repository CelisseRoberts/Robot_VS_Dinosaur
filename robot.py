from weapon import Weapon
from dinosaur import Dinosaur 


class Robot: 
    def __init__(self):
        self.robot = "Rosey"
        self.health = 100
        self.active_weapon = Weapon()
        


    def attack(self, dinosaur): 
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.robot} attacked {dinosaur.dinosaur} Dino health = {dinosaur.health}')
         

        
