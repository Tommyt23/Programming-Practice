class Enemy:
    def __init__(self, attack_strength, defence_strength, type):
        self._health = 100 # all enemies start with 100 health
        self._attack_strength = attack_strength # integer between 1  and 100
        self._defence_strength = defence_strength # integer between 1 and 100
        self._type = type # name of enemy or species

    def get_health(self):
        # returns the health of the enemy
        return self.health
    
    def attack(self):
        # returns the attack strength of the enemy
        return self._attack_strength