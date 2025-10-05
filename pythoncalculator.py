#Python Calculator
#if I put only round in result, it shall round to the nearest integer and if I put round(result,3),it shall round uoto 3 decimal places.
operator = input("Enter any operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+" :
  result = num1 + num2
  print(round(result))
elif operator =="-":
  result = num1 - num2
  print(result)
elif operator =="*":
  result = num1 * num2
  print(result)
elif operator =="/":
  result = num1/ num2
  print(result)
else:
  print(f"{operator} is NOT a valid operator")

  #python weight Calculator
  weight = float(input("Enter your weight: "))
  Units = input("Kilogram or Pound? (K or L): ")
  if Units == "K":
    weight = weight * 2.205
    Units ="Lbs."
  elif Units == "L":
        weight = weight / 2.205
        Units ="Kgs."
  else:
    print(f"{Units} are not valid")
  print(f"Your weight is: {weight}{Units}")


  

