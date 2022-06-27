import prompt


def generate_round(task_string, get_brain_task, user_name):
    print(f'{task_string}')
    count_answer = 0
    result_phrase = ''
    while count_answer < 3:
        brain_task, correct_answer = get_brain_task()
        print('Question: ' + str(brain_task))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            count_answer += 1
            print('Correct!')
        else:
            count_answer = 4
            result_phrase = print(f'"{user_answer}" is wrong answer ;(.'
                                  f'Correct answer was "{correct_answer}".')
        if count_answer == 3:
            result_phrase = print(f'Congratulations, {user_name}!')
    return result_phrase
