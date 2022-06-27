#! usr/bin/env python3


from brain_games.greetings.greet_modul import greeting
from brain_games.greetings.welcome_modul import welcome_user, get_user_name
from brain_games.games.calc_task_modul import task_string, get_calc_task
from brain_games.logic.game_logic_modul import game


def main():
    greeting()
    user_name = get_user_name()
    welcome_user(user_name)
    game(task_string, get_calc_task, user_name)


if __name__ == '__main__':
    main()
