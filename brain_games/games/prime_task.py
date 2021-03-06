from random import randint


TASK_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 100


def get_number():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    return random_number


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_prime_task():
    number = get_number()
    result = is_prime(number)
    correct_answer = 'yes' if result else 'no'
    return number, correct_answer
