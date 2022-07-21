from random import randint


TASK_STRING = 'Answer "yes" if number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_even_task():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer
