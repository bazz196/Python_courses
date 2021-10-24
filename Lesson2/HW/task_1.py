print("Enter Your age:")
age = int(input())  # Ввожу int число
print(type(age))  # Проверяю тип
age = str(age)  # Преобразую в стрингу
print("Age object was converted to", type(age))  # Для красоты вывожу буквы с выводом типа данных
print("Enter Your name:")
name = str(input())  # Ввожу str имя
age_and_name = 'Hi ' + name + ', now I known that You ' + age + ' years old.'
print(age_and_name)