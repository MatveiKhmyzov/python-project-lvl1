from random import randint


TASK_STRING = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_numbers():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    return number_1, number_2


def calculate_gcd(number_1, number_2):
    remainder = min(number_1, number_2)
    while remainder > 0:
        if abs(number_1) > abs(number_2):
            remainder = number_1 % number_2
            number_1 = number_2
            number_2 = remainder
        else:
            remainder = number_2 % number_1
            number_2 = number_1
            number_1 = remainder
    gcd = number_1 if abs(number_1) > abs(number_2) else number_2
    return gcd


def get_gcd_task():
    pair_number = get_numbers()
    number_1, number_2 = pair_number
    pair = ' '.join(str(pair_number[i]) for i in range(2))
    correct_answer = calculate_gcd(number_1, number_2)
    return pair, str(correct_answer)
