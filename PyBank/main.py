import os
import csv

pybank_csv = os.path.join("resources/budget_data.csv")

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    date = []
    PL = []
    for row in csvreader:
        date.append(row[0])
        PL.append(int(row[1]))
        
    total_months = (len(date))
    
    total_amount = sum(PL)
        
    PL_change = []
    for i in range(len(PL) - 1):
        PL_change.append(PL[i + 1] - PL[i])

    def average(numlist):
        numbers = []
        for number in numlist:
            numbers.append(number)
        x = sum(numbers)
        y = x/len(numlist)
        return(y)     
    avg_change = average(PL_change)
    avg_change_round=round(avg_change,2)

    max_change = max(PL_change)
    for j in range(len(PL_change)):
        if PL_change[j] == max_change:
            max_date = date[j+1]
    
    min_change = min(PL_change)
    for j in range(len(PL_change)):
        if PL_change[j] == min_change:
            min_date = date[j+1]
    
    print(" ")
    print("Finacial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_amount))
    print("Average Change: $" + str(avg_change_round))
    print("Greatest Increase in Profits: " + max_date + " ($" + str(max_change) + ")" )
    print("Greatest Decrease in Profits: " + min_date + " ($" + str(min_change) + ")" )
    print(" ")