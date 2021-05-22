from questions import QUESTIONS
from babel.numbers import format_currency


def isAnswerCorrect(question, answer):
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question['answer'] else False  # remove this


def lifeLine(ques):
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    #  For now, the below code works for only one question without LIFE-LINE and QUIT checks

    prize = 0
    minimum_prize = 0
    print("\t\t\t* * WELCOME TO KBC!! * *")

    for i in range(15):
        if i == 5:
            minimum_prize = 10000
            print("CONGRATULATIONS YOU HAVE CROSSED 1st LEVEL")
            print(f'Minimum Prize: {format_currency(minimum_prize, "INR", locale="en_IN")}')
        if i == 10:
            minimum_prize = 320000
            print("CONGRATULATIONS YOU HAVE CROSSED 2nd LEVEL")
            print(f'Minimum Prize: {format_currency(minimum_prize, "INR", locale="en_IN")}')

        print(f'\nPrize for Next Question: {format_currency(QUESTIONS[i]["money"], "INR", locale="en_IN")}')
        print(f'Question {i + 1}: {QUESTIONS[i]["name"]}')
        print(f'\tOptions:')
        print(f'\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\tOption 4: {QUESTIONS[i]["option4"]}')
        print('Enter "quit" if you want to quit the game and take your prize money')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations

        if ans == 'quit':
            print("You have QUIT the game")
            if i == 0:
                print("You Didn't win Anything, YOU LOSER!!")
            else:
                print(f'CONGRATULATIONS!! YOU WIN: {format_currency(QUESTIONS[i-1]["money"], "INR", locale="en_IN")}')
            break

        if isAnswerCorrect(QUESTIONS[i], int(ans)):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('Correct Answer!')
            if i == 14:
                print(f'CONGRATULATIONS!! YOU WIN: {format_currency(QUESTIONS[i]["money"], "INR", locale="en_IN")}')
                break
            print(f'Total Prize: {format_currency(QUESTIONS[i]["money"], "INR", locale="en_IN")}')


        else:
            # end the game now.
            # also print the correct answer
            print('Incorrect Answer!')
            print(f'Correct Answer was Option {QUESTIONS[i]["answer"]}')
            print("\n* * GAME OVER!! * *")
            if minimum_prize == 0:
                print("You Didn't win Anything, YOU LOSER!!")
            else:
                print(f'CONGRATULATIONS!! YOU WIN: {format_currency(minimum_prize, "INR", locale="en_IN")}')
            break

    # print the total money won in the end.


kbc()
