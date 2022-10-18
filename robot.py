from weapon import Weapon
 


class Robot: 
    def __init__(self):
        self.name = "Rosey"
        self.health = 100
        self.active_weapon = Weapon()
        


    def attack(self, dinosaur): 
        dinosaur.health -= self.active_weapon.attack_power 
        print(f'{self.name} attacked {dinosaur.name}. Dino health = {dinosaur.health}')
         

        
