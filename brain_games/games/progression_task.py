from random import randint


TASK_STRING = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_ROW = 5
MAX_ROW = 15


def get_progression_task():
    row = []
    first_element = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER, MAX_NUMBER)
    row_length = randint(MIN_ROW, MAX_ROW)
    hidden_element = randint(0, row_length - 1)
    for i in range(row_length):
        first_element += step
        row.append(first_element)
    correct_answer = str(row[hidden_element])
    row[hidden_element] = '..'
    progression = ' '.join(str(row[i]) for i in range(len(row)))
    return progression, correct_answer
