import random

class Ya:
    def __init__(self, name="Ты", hp=100):
        self.name = name
        self.hp = hp
        self.damage = random.randint(0, 10)
        self.armor = random.randint(0, 10)
        self.action = None

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def choose_action(self, action):
        self.action = action

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: здоровье {self.hp}, урон {self.damage}, броня {self.armor}"