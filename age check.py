name = input("What is your name? ")
age = int(input("How old are you? "))
Yearsto50 = 50 - age
if Yearsto50 >0:
    print ("Hello" + name.title() +",you will be 50 in "+ str(Yearsto50)+ "years.")
else:
    print("Hello " + name.title() +",You were 50 "+str(-Yearsto50)+ "years ago.")
        
