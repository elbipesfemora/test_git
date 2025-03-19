def calculate_damage(attacker_damage, defender_armor):
    damage = defender_armor - attacker_damage
    return damage if damage < 0 else 0

def handle_action(attacker, defender):
    if attacker.action == "защита":
        print(f"{attacker.name} защищается (броня: {attacker.armor})")
        if defender.action == "атака":
            damage = calculate_damage(defender.damage, attacker.armor)
            attacker.take_damage(damage)
            print(f"{attacker.name} получил урон: {damage}")
        else:
            print("Оба защищаются! Ничего не происходит!")
    else:  # атака
        if defender.action == "защита":
            damage = calculate_damage(attacker.damage, defender.armor)
            defender.take_damage(damage)
            print(f"{defender.name} получил урон: {damage}")
        else:
            damage = attacker.damage
            defender.take_damage(damage)
            print(f"{defender.name} получил урон: {damage}")

    print(attacker)
    print(defender)