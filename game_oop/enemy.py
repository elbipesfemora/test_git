import random

class Enemy:
    def __init__(self, name="Монстр", hp=100):
        self.name = name
        self.hp = hp
        self.damage = random.randint(0, 10)
        self.armor = random.randint(0, 10)
        self.action = None

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def choose_action(self):
        self.action = random.choice(["защита", "атака"])

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: здоровье {self.hp}, урон {self.damage}, броня {self.armor}"