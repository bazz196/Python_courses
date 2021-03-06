my_tuple = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
new_list = [list(elem) for elem in my_tuple]
print(new_list)

# Короткая версия
print([list(elem) for elem in [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]])

'''
Задача 7. 10 баллов
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
'''
