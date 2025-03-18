products = input('Введите список продуктов в формате «товар:количество» через запятую: ')

products_split = products.split(',')

product_pairs = [item.split(':') for item in products_split]

products_dict = {
    product: sum(
        int(item) for p, item in product_pairs if p == product
    )
    for product in set(p for p, i in product_pairs)
}

sorted_dict = sorted(products_dict.items(), key = lambda item: item[0])

column_output = [f'{product} - {item}' for product, item in sorted_dict]
for str_line in column_output:
    print(str_line)