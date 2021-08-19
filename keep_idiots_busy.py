import pyinputplus as pyip
while True:
    prompt = "want to know how to keep idiots busy for hours?\n"
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print("Thank you. Have a nice day.")