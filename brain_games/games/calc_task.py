from random import randint, choice


TASK_STRING = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_calc_task():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    operators = (' + ', ' - ', ' * ')
    operator = choice(operators)
    math_expression = f'{number_1}{operator}{number_2}'
    if operator == ' + ':
        correct_answer = number_1 + number_2
    elif operator == ' * ':
        correct_answer = number_1 * number_2
    elif operator == ' - ':
        correct_answer = number_1 - number_2
    return math_expression, str(correct_answer)
