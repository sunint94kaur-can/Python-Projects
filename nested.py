rows = int(input("Enter any number of rows: "))
columns = int(input("Enter any number of columns: "))
symbol = input("Enter the symbol you want to print: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end ="")
    print()    