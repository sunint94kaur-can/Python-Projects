num = int(input("What is your multiplication table? "))
mx = [x * num for x in range(1,21)]
mx1 = [f'{num}*{x}={num*x}' for x in range(1,21)]
print(mx1)

