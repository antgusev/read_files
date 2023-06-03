import json

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        ingredient_count = int(file.readline())
        dish_list = []
        for i in range(ingredient_count):
            name, quantity, measure = file.readline().split(' | ')
            dish_list.append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish] = dish_list
    #res = json.dumps(cook_book, indent=0)
    #print(res)
    print(cook_book)

#for key, value in cook_book.items():
#    print(f'\n{key}\n')
#    for key in value:
#        print(f'{key}')
#print()