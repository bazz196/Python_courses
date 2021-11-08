'''
Первая версия
user_input = input("Please enter a sentence: ")
user_input = user_input.lower()
user_input = user_input.replace('черт', '####')
print(user_input)
'''

# Вторая и рабочая версия
import re
user_input = input("Please enter a sentence: ")
replaced_input = re.sub(r'(Ч|ч)(Е|е)(Р|р)(Т|т)\s', '#### ', user_input)
print(replaced_input)
