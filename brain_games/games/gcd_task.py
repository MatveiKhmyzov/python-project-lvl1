from random import randint


task_string = 'Find the greatest common divisor of given numbers.'


def get_gcd_task():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    pair_number = (number_1, number_2)
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
    correct_answer = number_1 if abs(number_1) > abs(number_2) else number_2
    pair = ' '.join(str(pair_number[i]) for i in range(2))
    return pair, str(correct_answer)
