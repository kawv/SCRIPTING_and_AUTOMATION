# This is a simple multiplication game I made, I do hope you enjoy it

import pyinputplus as pyip
import random, time

name = pyip.inputStr('***** HELLO, TELL ME YOUR NAME! *****: ').title()

print(f"********************************* \nWelcome TO YOUR MULTIPLICATION QUIZ {name} \n********************************* ")
print("\n 1. ***** YOU HAVE 8 SECONDS TO ANSWER EACH QUESTION. *****")
print("\n 2. ***** YOU HAVE 3 Tries for each failed QUESTION *****")

choice_to_continue = pyip.inputYesNo("\n***** ARE YOU READY ? *****  yes/no ?: ")

if choice_to_continue.lower() == 'yes':

    no_ofquetions = 10
    correct_answers = 0

    for questionNumber in range(no_ofquetions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = "#{}: {} x {} = ".format(questionNumber, num1, num2)

        try:
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8,
                          limit=3)

        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries !')

        else:
            # This block runs if there was no exception raised in the try block.
            print('Correct!')
            correct_answers += 1

        time.sleep(1)  # this gives a brief pause to let user see the result.

    if correct_answers > 5:
        print("\nGREAT JOB {}!\n YOU Scored: {} / {}".format(name, correct_answers, no_ofquetions))
    else:
        print(f"\n***** Don't Worry {name}! You will do better next time. *****")
        print("YOU Scored: {} / {}".format(name, correct_answers, no_ofquetions))
else:
    print(f"\n***** Good bye {name}! *****")
    quit()
