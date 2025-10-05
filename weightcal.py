weight = float(input("Enter your weight: "))
Units = input("Kilogram or Pound? (K or L): ")
if Units == "K":
    weight = weight * 2.205
    Units ="Lbs."
    print(f"Your weight is: {round(weight,1)} {Units}")
elif Units == "L":
        weight = weight / 2.205
        Units ="Kgs."
        print(f"Your weight is: {round(weight,1)} {Units}")
else:
    print(f"{Units} are not valid")

