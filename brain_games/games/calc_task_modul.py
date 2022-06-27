from random import randint, choice


task_string = 'What is the result of the expression?'


def get_calc_task():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    operators = (' + ', ' - ', ' * ')
    random_operator = choice(operators)
    brain_task = str(random_number_1) + random_operator + str(random_number_2)
    correct_answer = str(eval(brain_task))
    return brain_task, correct_answer
