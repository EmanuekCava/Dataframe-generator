import pandas as pd
import functions as func

df = pd.DataFrame()

option = func.options()

def runAgain():
    newOption = func.options()
    runData(newOption)

def addColumn():
    print("\nAdd a column")
    column = input("Write a new column name: ")
    column = column.upper()
    df[column] = None
    runData(1)
def removeColumn():
    print("Columns: ", df.columns.tolist())
    column = input("\nWrite the name of column you want to delete: ")
    column = column.upper()

    try:
        del df[column]
        print(f"\nColumn {column} was removed!")
    except:
        print("Column does not exists.")

    newOption = func.options()
    runData(newOption)

def runData(option):
    if option == 1:
        optionAddColumn = func.optionOne()

        if optionAddColumn == 0:
            runAgain()
        elif optionAddColumn == 1:
            addColumn()
            
    elif option == 2:
        if len(df.columns != 0):
            values = []
            for i in range (0, len(df.columns)):
                print("\nAdd a value to {}".format(df.columns[i]))
                value = input("Write a value: ")
                values.append(value)
            df.loc[len(df.index)] = values
            runAgain()
        else:
            func.errorMessage("Columns do not exist. Try to add columns before to add values.")
            runAgain()

    elif option == 3:
        print("\nDATAFRAME: ")
        print("\n", df)
        runAgain()

    elif option == 4:
        writer = pd.ExcelWriter("dataframe.xlsx")
        pd.DataFrame(df).to_excel(writer)
        writer.save()
        print("\nExcel file generated successfully!")
        runAgain()

    elif option == 5:
        df.to_csv("dataframe.csv", sep="\t", encoding='utf-8')
        runAgain()

    elif option == 6:
        df.to_json("dataframe.json")
        runAgain()

    elif option == 7:
        removeColumn()

runData(option)    




    


