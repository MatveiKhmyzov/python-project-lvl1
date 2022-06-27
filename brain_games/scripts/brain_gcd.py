#! usr/bin/env python3


from brain_games.greetings.greet import greeting
from brain_games.greetings.welcome import welcome_user, get_user_name
from brain_games.games.gcd_task import task_string, get_gcd_task
from brain_games.engine.engine import generate_round


def main():
    greeting()
    user_name = get_user_name()
    welcome_user(user_name)
    generate_round(task_string, get_gcd_task, user_name)


if __name__ == '__main__':
    main()
