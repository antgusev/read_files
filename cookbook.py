import json

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        ingredient_count = int(file.readline())
        dish_list = []
        for i in range(ingredient_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            dish_list.append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish.strip()] = dish_list
    res = json.dumps(cook_book, ensure_ascii=False, indent=2)
    print(res)
