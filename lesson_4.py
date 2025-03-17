user_status = input('Это VIP-клиент (Да/Нет): ').lower()
summary_price = int(input('Введите сумму покупки: '))

if summary_price > 1000 and user_status == 'да':
    summary_price *= 0.75
    summary_price = round(summary_price, 2)
elif summary_price > 1000 and user_status == 'нет':
    summary_price *= 0.8
    summary_price = round(summary_price, 2)
elif 500 < summary_price < 1000:
    summary_price *= 0.9
    summary_price = round(summary_price, 2)
else:
    print('Что-то погло не так! попробуйте повторить.')

print(f'Сумма покупки составила: {summary_price} деняк, с учетом всех скидок.')

