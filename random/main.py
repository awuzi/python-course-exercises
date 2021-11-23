import random


def random_number():
    mysterious_number = random.randint(0, 100)
    while True:
        prompt = int(input('Devinez le nombre : '))
        if prompt == mysterious_number:
            print('C\'est gagné : ', mysterious_number)
            break

        print('Trop Grand') if prompt > mysterious_number else print('Trop petit')


random_number()
