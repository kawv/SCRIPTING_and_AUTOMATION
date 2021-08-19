USER = input("Your Name: ")
print(f"\nGOOD DAY {USER.title()}!\nENTER\n\n1.To type curse words\n2.To list curse words\n3.To type the file path\n4.To Exit\n")

import json
import sys
import os

# importing the json module

curse_words = ['crap','sod','bugger','arse','git','bint','munter','balls','shit',
               'bitch','tit','gash','twat','punani','cock','dick','fuck','cunt','bint','pussy']

# creating a json file to store/write the curse words into it.
filename = "cursewords.json"
with open(filename,"w") as c:
    json.dump(curse_words,c)

new_curse_words = []


while True:
# The general looping statement.

    #p1
    prompt1 = input("Your selection: ")

    if prompt1 == "1":
        def enter_curse_words():
            # function for users to enter their own curse words.

            user_words = input("TYPE YOUR OWN CURSE WORDS: \n").split(",")
            new_curse_words.extend(user_words)
        enter_curse_words()

    elif prompt1 == "2":
        print(curse_words)

    elif prompt1 =="4":
        def print_bye():
            # function to tell the user Good Bye.
            global USER   # making user in the global scope available to the function.

            name = USER
            print(f"\nGOOD BYE {name.title()}!")
        print_bye()
    else:
        print("\nWRONG INPUT !")

    #p2
    prompt2 = input("\nTYPE 2 TO VIEW THE AVAILABLE CURSE WORDS, OR 1 TO ADD NEW ONES: \n")


    if prompt2 == "1":
        def enter_curse_words():
            # function for users to enter their own curse words.

            user_words = input("TYPE YOUR OWN CURSE WORDS: \n").split(",")
            new_curse_words.extend(user_words)
        enter_curse_words()

    elif prompt2 == "2":
        print(curse_words) # listing the available curse words.

    elif prompt2 == "4":
        print(f"\nGOOD BYE {USER.title()}!")
        break

    else:
        print("\nWRONG INPUT !")

    #p3
    prompt3 = input("\nTYPE 3 TO ENTER FILE PATH: \n")

    if prompt3 == "3":
        def enter_file_path():

        # function to enable users enter the file path to curse words.

            try:
                file_path_entry = input("\nENTER FILE PATH: \n")
                file_path = open(file_path_entry, "r+")
                file_contents = file_path.read()


                similar_words = [value for value in new_curse_words if value in file_contents]
                # checking for similar curse words between the file and the new ones entered by the user.

                if similar_words:
                    print(f"\n{len(similar_words)} SIMILAR WORDS FOUND,THEY ARE; \n")
                    print(similar_words)

                else:
                    print("\nNO SIMILAR  WORDS FOUND! ")

            except Exception:
                print("SORRY NO SUCH FILE FOUND !")

        enter_file_path()

    elif prompt3 == "4":
        print(f"\nGOOD BYE {USER.title()}!")
        break

    elif prompt3 == "1":
        def enter_curse_words():
            # function for users to enter their own curse words.

            user_words = input("TYPE YOUR OWN CURSE WORDS: \n").split(",")
            new_curse_words.extend(user_words)
        enter_curse_words()

    elif prompt3 == "2":
        print(curse_words)

    else:
        print("\nWRONG INPUT !")

    #p4
    prompt4 = input("\nENTER 4 TO EXIT: \n")


    if prompt4 =="4":
        print(f"\nGOOD BYE {USER.title()}!")
        break
    else:
        print("\nWRONG INPUT !")
