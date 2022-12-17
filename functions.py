
def errorMessage(message):
    print("\n{}".format(message))

def options():

    option = -1

    while option < 0 or option > 7:

        print("\n\t.:: OPTIONS ::.")
        print("0: EXIT")
        print("1: ADD COLUMNS")
        print("2: ADD VALUES")
        print("3: SHOW DATAFRAME")
        print("4: GENERATE EXCEL FILE")
        print("5: GENERATE CSV FILE")
        print("6: GENERATE JSON FILE")
        print("7: REMOVE A COLUMN")
        optionString = input("Select an option: ")

        try:
            option = int(optionString)

            if option < 0 or option > 7:
                errorMessage("Option does not exists. Please try again")

        except:
            errorMessage("Option does not exists. Please try again")

    return option
    
def optionOne():

    optionAddColumn = -1

    while optionAddColumn < 0 or optionAddColumn > 1:
        print("\n\t.:: ADD COLUMNS ::.")
        print("0: BACK")
        print("1: ADD A COLUMN")
        optionAddColumnString = input("Select an option: ")

        try:
            optionAddColumn = int(optionAddColumnString)

            if optionAddColumn < 0 or optionAddColumn > 1:
                errorMessage("Option does not exists. Please try again")

        except:
            errorMessage("Option does not exists. Please try again")

    return optionAddColumn