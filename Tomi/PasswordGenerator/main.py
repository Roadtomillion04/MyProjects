# Let's create a random password generator by random module
import random
import string

available_char = string.ascii_uppercase +string.ascii_lowercase +string.digits +'!@#$%'
print(available_char)

try:
    no_of_times = int(input('How many passwords? '))
    password_length = int(input('How long? '))

    assert no_of_times > 0, 'Number must be greater than zero'
    assert password_length > 0, 'Number must be greater than zero'

    while no_of_times > 0:
        for i in range(password_length):
            print(random.choice(available_char), end='')
        print()
        no_of_times -= 1

except ValueError:
    print('Please Enter a number')
