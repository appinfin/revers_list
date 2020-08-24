import random

def generation_random_number():
    """Ф-ция генерирует список случайных целых чисел"""
    random_list = []
    for n in range(10): # кол-во чисел в списке 10
        
        random_list.append(random.randint(0, 100))
    
    return random_list

#получаем случайный список
right_list = generation_random_number()
#проход по списку от конца к началу с шагом 1
revers_list = right_list[::-1] 

print('Правильный      список:', right_list)
print('Инвертированный список:', revers_list)

input()
