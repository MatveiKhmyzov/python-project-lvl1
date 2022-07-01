from random import randint, choice


TASK_STRING = 'What is the result of the expression?'


def get_calc_task():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = (' + ', ' - ', ' * ')
    operator = choice(operators)
    if operator == ' + ':
        math_expression = f'{number_1} + {number_2}'
        correct_answer = number_1 + number_2
    elif operator == ' * ':
        math_expression = f'{number_1} * {number_2}'
        correct_answer = number_1 * number_2
    elif operator == ' - ':
        math_expression = f'{number_1} - {number_2}'
        correct_answer = number_1 - number_2
    return math_expression, str(correct_answer)
