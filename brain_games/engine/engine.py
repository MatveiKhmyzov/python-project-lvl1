import prompt


ROUNDS = 3


def generate_game(task_string, get_brain_task):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'{task_string}')
    count_answer = 0
    while count_answer < ROUNDS:
        brain_task, correct_answer = get_brain_task()
        print('Question: ' + str(brain_task))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            count_answer += 1
            print('Correct!')
        else:
            print(f''''{user_answer}' is wrong answer ;(.'''
                  f'''Correct answer was '''
                  f''''{correct_answer}'.\n'''
                  f'''Let's try again, {user_name}!''')
            break
    else:
        print(f'Congratulations, {user_name}!')
