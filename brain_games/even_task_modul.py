import prompt
from random import randint


def is_even(user_name):
    count_answer = 0
    print('Answer "yes" if number is even, otherwise answer "no".')
    result_phrase = ''
    while count_answer < 3:
        number = randint(1, 100)
        print('Question: ' + str(number))
        user_answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and user_answer == 'yes'
                or number % 2 != 0 and user_answer == 'no'):
            count_answer += 1
            print('Correct!')
        elif number % 2 == 0 and user_answer != 'yes':
            count_answer = 4
            result_phrase = print(f'"no" is wrong answer ;(.'
                                  f'Correct answer was "yes".'
                                  f' Let`s try again, {user_name}!\n')
        elif number % 2 != 0 and user_answer != 'no':
            count_answer = 4
            result_phrase = print(f'"yes" is wrong answer ;(.'
                                  f'Correct answer was "no".'
                                  f'Let`s try again, {user_name}!\n')
    if count_answer == 3:
        result_phrase = print(f'Congratulations, {user_name}!\n')
    return result_phrase
