#! usr/bin/env python3


from brain_games.greet_modul import greeting
from brain_games.welcome_modul import welcome_user, get_user_name
from brain_games.even_task_modul import is_even


def main():
    greeting()
    user_name = get_user_name()
    welcome_user(user_name)
    is_even(user_name)


if __name__ == '__main__':
    main()
