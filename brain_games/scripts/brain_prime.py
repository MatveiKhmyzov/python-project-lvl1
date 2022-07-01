#! usr/bin/env python3


from brain_games.games.prime_task import TASK_STRING, get_prime_task
from brain_games.engine.engine import generate_game


def main():
    generate_game(TASK_STRING, get_prime_task)


if __name__ == '__main__':
    main()
