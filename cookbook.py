#Задача 1

import json

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        ingredient_count = int(file.readline())
        ingredient_list = []
        for i in range(ingredient_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_list.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingredient_list
    res = json.dumps(cook_book, ensure_ascii=False, indent=2)
    #print(res)


#Задача 2

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for person_dish in dishes:
        for dish in cook_book:
            if person_dish == dish:
                dish_ingr = cook_book[dish]
                #print(dish_ingr)
                for ingredient in dish_ingr:
                    name_ingr = ingredient.get('ingredient_name')
                    quantity_ingr = int(ingredient.get('quantity')) * person_count
                    measure_ingr = ingredient.get('measure')
                    ingr_dict = {name_ingr: {'measure': measure_ingr, 'quantity': quantity_ingr}}
                    ingredient_dict.update(ingr_dict)
    return ingredient_dict
                

#print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


#Задача 3

def join_files(files):
    
    count_str_list = []
    for some_file in files:
        with open(some_file, 'r', encoding='utf-8') as f_1:
            count_str_list.append(len(f_1.readlines()))
    count_str = sorted(count_str_list)
    #print(count_str)

    for some_file in files:
        count = 0
        with open(some_file, 'r', encoding='utf-8') as f_1:
            res_1 = f_1.readlines()
            if len(res_1) == count_str[count]:
                f = open('1_3.txt', 'a', encoding='utf-8')
                f.write(some_file + '\n')
                f.write(str(len(res_1)) + '\n')
                f.writelines(res_1)
                f.close()
            #elif count >= len(files):
                #break
            else:
                count +=1
            print(res_1)


join_files(['1.txt', '2.txt', '3.txt'])

