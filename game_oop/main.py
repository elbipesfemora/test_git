import time
import json
from colorama import Fore
from player import Player
from enemy import Enemy
from game_logic import handle_action

SAVE_FILE = "save.json"

def print_welcome_message():
    print("Добро пожаловать в игру про драки с монстром!")

def save_game(player, enemy, turn):
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump({
                "player_hp": player.hp,
                "monster_hp": enemy.hp,
                "turn": turn
            }, file)
        print("Игра сохранена.")
    except Exception as e:
        print(f"Ошибка при сохранении игры: {e}")

def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        print("Игра загружена.")
        return data
    except FileNotFoundError:
        print("Сохранение не найдено. Начинаем новую игру.")
    except json.JSONDecodeError:
        print("Ошибка чтения файла сохранения. Начинаем новую игру.")
    except Exception as e:
        print(f"Ошибка при загрузке игры: {e}")
    return None

def main():
    print_welcome_message()

    # Загрузка сохранения
    game_state = load_game()
    if game_state:
        player = Player(hp=game_state["player_hp"])
        enemy = Enemy(hp=game_state["monster_hp"])
        turn = game_state["turn"]
    else:
        player = Player()
        enemy = Enemy()
        turn = 1

    delay = 3
    variants = ["защита", "атака"]

    while True:
        print(f"\nХод {turn}")
        print(player)
        print(enemy)

        # Выбор действия игрока
        action = input("Что ты выберешь (защита/атака)? ").lower()
        while action not in variants:
            print("Такого варианта нет!")
            action = input("Что ты выберешь (защита/атака)? ").lower()
        player.choose_action(action)

        # Выбор действия монстра
        enemy.choose_action()
        print(f"{enemy.name} выбрал {enemy.action}")

        # Обработка действий
        handle_action(player, enemy)
        handle_action(enemy, player)

        time.sleep(delay)

        # Проверка конца игры
        if not player.is_alive():
            print(Fore.RED + "Ты погиб!" + Fore.RESET)
            print(Fore.YELLOW + "МОНСТР WINS!!!" + Fore.RESET)
            break
        if not enemy.is_alive():
            print(Fore.GREEN + "Монстр погиб!" + Fore.RESET)
            print(Fore.YELLOW + "ТЫ WINS!!!" + Fore.RESET)
            break

        # Сохранение игры
        if input("Хотите сохранить игру? (да/нет): ").lower() == "да":
            save_game(player, enemy, turn)

        turn += 1

    print("Конец игры!")

if __name__ == "__main__":
    main()