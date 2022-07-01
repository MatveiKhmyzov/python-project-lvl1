from random import randint


TASK_STRING = 'Answer "yes" if number is even, otherwise answer "no".'


def get_even_task():
    random_number = randint(1, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, correct_answer
