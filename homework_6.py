import time
import random
from colorama import Fore

def print_welcome_message():
    print("Добро пожаловать в игру про драки с монстром!")

def initialize_game():
    return {"player_hp": 100, "monster_hp": 100}

def get_choice(prompt, variants):
    while True:
        choice = input(prompt).lower()
        if choice in variants:
            return choice
        print("Такого варианта нет!")

def calculate_damage(attacker_damage, defender_armor):
    damage = defender_armor - attacker_damage
    return damage if damage < 0 else 0

def handle_action(attacker, defender, action):
    if action == "защита":
        print(f"{attacker['name']} защищается (armor: {attacker['armor']})")
        if defender["action"] == "атака":
            damage = calculate_damage(defender["damage"], attacker["armor"])
            attacker["hp"] += damage
            print(f"{attacker['name']} получил урон: {damage}")
        else:
            print("Оба защищаются! Ничего не происходит!")
    else:  
        if defender["action"] == "защита":
            damage = calculate_damage(attacker["damage"], defender["armor"])
            defender["hp"] += damage
            print(f"{defender['name']} получил урон: {damage}")
        else:
            damage = attacker["damage"]
            defender["hp"] -= damage
            print(f"{defender['name']} получил урон: {damage}")

    print(f"Здоровье {attacker['name']}: {attacker['hp']}")
    print(f"Здоровье {defender['name']}: {defender['hp']}")

def check_game_over(player_hp, monster_hp):
    if player_hp <= 0:
        print(Fore.RED + "Ты погиб!" + Fore.RESET)
        print(Fore.YELLOW + "МОНСТР WINS!!!" + Fore.RESET)
        return True
    if monster_hp <= 0:
        print(Fore.GREEN + "Монстр погиб!" + Fore.RESET)
        print(Fore.YELLOW + "ТЫ WINS!!!" + Fore.RESET)
        return True
    return False

def main():
    print_welcome_message()
    game_state = initialize_game()
    delay = 3
    variants = ["защита", "атака"]

    while True:
        player = {
            "name": "Ты",
            "hp": game_state["player_hp"],
            "damage": random.randint(0, 10),
            "armor": random.randint(0, 10),
            "action": None
        }
        monster = {
            "name": "Монстр",
            "hp": game_state["monster_hp"],
            "damage": random.randint(0, 10),
            "armor": random.randint(0, 10),
            "action": None
        }

        print(f"{player['name']}: здоровье {player['hp']}")
        print(f"{monster['name']}: здоровье {monster['hp']}\n")

        player["action"] = get_choice("Что ты выберешь (защита/атака)? ", variants)
        print(f"{player['name']} выбрал {player['action']}")

        time.sleep(1)
        monster["action"] = random.choice(variants)
        print(f"{monster['name']} выбрал {monster['action']}")
        time.sleep(1)

        handle_action(player, monster, player["action"])
        handle_action(monster, player, monster["action"])

        time.sleep(delay)

        game_state["player_hp"] = player["hp"]
        game_state["monster_hp"] = monster["hp"]

        if check_game_over(game_state["player_hp"], game_state["monster_hp"]):
            break

    print("Конец игры!")

if __name__ == "__main__":
    main()