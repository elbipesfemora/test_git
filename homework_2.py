grass = int(input('Количество добавляемой травы: '))
crystals = int(input('Количество кристаллов: '))
water = int(input('Количество воды: '))
samogon = int(input('Сколько раз светила луна: '))
fire_dust = int(input('Количество огненной пыли: '))

magick_power = (grass * 0.5 + crystals * 1.5 + water * 0.8 + fire_dust * 1 + 
                samogon * 1.2)

bonus = (magick_power > 150) * 20 + magick_power

print('Магическая сила равна:', bonus)