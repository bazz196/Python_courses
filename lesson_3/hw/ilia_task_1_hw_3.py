print('Tell me please - Your age', end=': ')
user_age = int(input())

if user_age == 18:
    print('Wait a little bit')
elif user_age > 18:
    print('You are welcome')
else:
    print('Go back to school')
