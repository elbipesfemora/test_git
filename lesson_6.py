import time
import random
from colorama import Fore

def print_welcome_message():
    print("Добро пожаловать в игру про драки с монстром!")

def initialize_game():
    player_hp = 100
    monster_hp = 100
    return player_hp, monster_hp

def get_player_choice():
    variants = ["защита", "атака"]
    while True:
        player_choice = input("Что ты выберешь (защита/атака)? ").lower()
        if player_choice in variants:
            return player_choice
        else:
            print("Такого варианта нет!")

def get_monster_choice():
    variants = ["защита", "атака"]
    return random.choice(variants)

def calculate_damage(attacker_damage, defender_armor):
    damage = defender_armor - attacker_damage
    return damage if damage < 0 else 0

def handle_defense(player_armor, monster_damage, player_hp):
    print(f"Ты защищаешься (armor: {player_armor})")
    print(f"Монстр атакует! (damage: {monster_damage})")
    damage = calculate_damage(monster_damage, player_armor)
    player_hp += damage
    print(f"Ты получил урон: {damage}")
    print(f"Твоё здоровье: {player_hp}")
    return player_hp

def handle_attack(attacker_damage, defender_armor, defender_hp, defender_name):
    print(f"Атакующий наносит удар! (damage: {attacker_damage})")
    print(f"Защитник защищается! (armor: {defender_armor})")
    damage = calculate_damage(attacker_damage, defender_armor)
    defender_hp += damage
    print(f"{defender_name} получил урон: {damage}")
    print(f"Здоровье {defender_name}: {defender_hp}")
    return defender_hp

def handle_both_attack(player_damage, monster_damage, player_hp, monster_hp):
    print(f"Ты атакуешь! (damage: {player_damage})")
    print(f"Монстр атакует! (damage: {monster_damage})")
    player_hp -= monster_damage
    print(f"Ты получил урон: {monster_damage}")
    print(f"Твоё здоровье: {player_hp}")
    monster_hp -= player_damage
    print(f"Монстр получил урон: {player_damage}")
    print(f"Здоровье монстра: {monster_hp}")
    return player_hp, monster_hp

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
    player_hp, monster_hp = initialize_game()
    delay = 3

    while True:
        monster_damage = random.randint(0, 10)
        monster_armor = random.randint(0, 10)
        player_damage = random.randint(0, 10)
        player_armor = random.randint(0, 10)

        print("Твоё здоровье:", player_hp)
        print("Здоровье монстра:", monster_hp, "\n")

        player_choice = get_player_choice()
        print("Ты выбрал", player_choice)

        time.sleep(1)
        monster_choice = get_monster_choice()
        print("Монстр выбрал", monster_choice)
        time.sleep(1)

        if player_choice == "защита":
            if monster_choice == "защита":
                print("Два дурачка стоят и защищаются! Ахахахах!")
            else:
                player_hp = handle_defense(player_armor, monster_damage, player_hp)
        else:
            if monster_choice == "защита":
                monster_hp = handle_attack(player_damage, monster_armor, monster_hp, "Монстр")
            else:
                player_hp, monster_hp = handle_both_attack(player_damage, monster_damage, player_hp, monster_hp)

        time.sleep(delay)

        if check_game_over(player_hp, monster_hp):
            break

    print("Конец игры!")

if __name__ == "__main__":
    main()