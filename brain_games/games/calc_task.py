from random import randint, choice


task_string = 'What is the result of the expression?'


def get_calc_task():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operators = (' + ', ' - ', ' * ')
    operator = choice(operators)
    math_expression = str(number_1) + operator + str(number_2)
    correct_answer = str(eval(math_expression))
    return math_expression, correct_answer
