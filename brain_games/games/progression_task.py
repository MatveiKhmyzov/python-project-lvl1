from random import randint


TASK_STRING = 'What number is missing in the progression?'


def get_progression_task():
    row = []
    first_element = randint(1, 100)
    step = randint(1, 100)
    row_length = randint(5, 15)
    hidden_element = randint(0, row_length - 1)
    for i in range(row_length):
        first_element += step
        row.append(first_element)
    correct_answer = str(row[hidden_element])
    row[hidden_element] = '..'
    progression = ' '.join(str(row[i]) for i in range(len(row)))
    return progression, correct_answer
