from random import randint


min_number = 0
max_number = 0

def input_numbers():
    min_number = int(input('Please enter min number: '))
    max_number = int(input('Please enter max number: '))

    if (max_number < min_number):
        print('Invalid input - try again')
        input_numbers
    else:
        rnd_number = randint(min_number, max_number)
        print(rnd_number)

input_numbers()
