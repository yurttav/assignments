#try ile daha kısa olurdu ama henüz gelinmedi o konuya :)

numbers = set("0123456789.-")

isvalid = False

while not isvalid:

    isstring = False

    text = input("Please enter a positive integer for Armstrong Number Checking : ")

    if (set(text)-numbers != set()) or (text.count('-') > 1) or (text.count('-') == 1) and (text[0] != '-') or (text.count('.') > 1) :

        isstring = True 

    if isstring:

        print(f"You entered {text}. It is a string. It is not a positive integer. Please try again.")    

    else:

        number = float(text)

        if number.is_integer():

            if (number > 0):

                isvalid = True

            else:

                print(f"You entered {text}. It is a negative integer. It is not a positive integer. Please try again.")

        else:

            print(f"You entered {text}. It is a float number. It is not a positive integer. Please try again.")

if isvalid:

    arm = 0

    number = int(number)

    processed_text = str(number)

    root = len(processed_text)

    for i in range(root):

        arm += int(processed_text[i])**root

    if arm == number:

        print(f"You entered {text}. It is an Armstrong Number.")

    else:

        print(f"You entered {text}. It is not an Armstrong Number.")