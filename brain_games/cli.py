#! usr/bin/env python3


import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    result = print(f'Hello, {name}!')
    return result


if __name__ == '__main__':
    welcome_user()
