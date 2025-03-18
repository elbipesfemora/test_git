import time
import random
import json
from colorama import Fore

# Константы
SAVE_FILE = "save.json"

def print_welcome_message():
    print("Добро пожаловать в игру про драки с монстром!")

def initialize_game():
    return {"player_hp": 100, "monster_hp": 100, "turn": 1}

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
    else:  # атака
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

def save_game(game_state):
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(game_state, file)
        print("Игра сохранена.")
    except Exception as e:
        print(f"Ошибка при сохранении игры: {e}")

def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            game_state = json.load(file)
        print("Игра загружена.")
        return game_state
    except FileNotFoundError:
        print("Сохранение не найдено. Начинаем новую игру.")
    except json.JSONDecodeError:
        print("Ошибка чтения файла сохранения. Начинаем новую игру.")
    except Exception as e:
        print(f"Ошибка при загрузке игры: {e}")
    return None

def main():
    print_welcome_message()

    # Проверка наличия сохранения
    game_state = None
    if input("Хотите загрузить сохранение? (да/нет): ").lower() == "да":
        game_state = load_game()

    # Если сохранение не загружено, начинаем новую игру
    if not game_state:
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

        print(f"\nХод {game_state['turn']}")
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

        # Обновление состояния игры
        game_state["player_hp"] = player["hp"]
        game_state["monster_hp"] = monster["hp"]
        game_state["turn"] += 1

        # Сохранение игры после каждого хода
        if input("Хотите сохранить игру? (да/нет): ").lower() == "да":
            save_game(game_state)

        if check_game_over(game_state["player_hp"], game_state["monster_hp"]):
            break

    print("Конец игры!")

if __name__ == "__main__":
    main()