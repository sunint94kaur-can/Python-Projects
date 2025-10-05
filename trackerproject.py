from datetime import date
import csv
date.today
dt = date.today()
filename = "text.csv"

with open(filename,'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow([dt])
    file.close()

exp = []
stopped = False
with open(filename,'a') as file:
    csvwriter = csv.writer(file)
    
    while not stopped:
        xp = int(input("What are your expenses? (type 0 to stop) "))
        if xp==0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
             
    file.close()