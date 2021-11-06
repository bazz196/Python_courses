print('Let\'s tell me please - Who are You!', '1. Admin', '2. User', '3. Not Authorized', 'Please make your choice', sep='\n', end=': ')
user_type = input()
user_type = int(user_type)

if user_type == 1:
    print('User')
elif user_type == 2:
    print('Admin')
else:
    print('403 not authorized')
