from passwordgenerator.lib.definitions import *


def menu():
    while True:
        try:
            pass_len = int(input('Enter the length of the password: '))
            generate_password(pass_len)


        except Exception as e:
            print("Invalid length")
            print('Enter a valide number\nRecommended: (greater than 12)')
        go = str(input('Generate another passoword? Y/n: ')).strip().upper()[0]
        if go == 'N':
            break
        else:
            continue
