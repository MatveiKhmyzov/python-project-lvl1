from random import randint


task_string = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    number = randint(2, 100)
    for i in range(2, number):
        if number % i == 0:
            return (False, number)
    return (True, number)


def get_prime_task():
    result, number = is_prime()
    correct_answer = 'yes' if result else 'no'
    return number, correct_answer
