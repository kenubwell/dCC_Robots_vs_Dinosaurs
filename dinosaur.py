#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.  

class Dinosaur:
     
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def dino_attack(self, targeted_robot):
        targeted_robot.health -= self.attack_power

