# Import modules and list file path
import os
import csv

PyBank_csv = os.path.join("../PyBank", "Python_PyBank_Resources_budget_data.csv")

# Open and read PyBank_csv
with open(PyBank_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row first
    csv_header = next(csvfile)

    #create a two lists from csv data - one for dates and one for profit/loss
    Dates = []
    ProfitLoss = []
    
    for row in csvreader:
        Dates.append(str(row[0]))
        ProfitLoss.append(int(row[1]))

    #Calculate number of months in data and create variable to hold the number
    TotalMonths = len(Dates)
    
    #Calculate total profit/loss and create a variable to hold the sum
    TotalPL = sum(ProfitLoss)
    
    #Create new list based on the difference between each value in ProfitLoss list
    MonthlyChange = [ProfitLoss[i+1]-ProfitLoss[i] for i in range(len(ProfitLoss)-1)]

    #Calculate average of the values in MonthlyChange
    TotalMC = sum(MonthlyChange)
    LengthMC = len(MonthlyChange)
    AverageMC = float(TotalMC/LengthMC)

    #greatest increase = largest monthly change
    GreatestIncrease = max(MonthlyChange)
    GreatestMonth = Dates[MonthlyChange.index(GreatestIncrease)+1]

    #greatest decrease = smallest monthly change
    GreatestDecrease = min(MonthlyChange)
    MinMonth = Dates[MonthlyChange.index(GreatestDecrease)+1]

    #print results (look up how to go to next line so can print in one command) 
    print(f"Financial Analysis")   
        # spacer row of "---------------------------"
    print(f"---------------------------------------------------")    
        # "Total Months: " (total num of months)
    print(f"Total Months: {TotalMonths}")
        # "Total: " (sum profit/loss)
    print(f"Total: ${TotalPL}")
        # "Average Change: "
    print(f"Average Change: ${AverageMC:.2f}")
        # "Greatest Increase in Profits: "(month and amount)
    print(f"Greatest Increase in Profits: {GreatestMonth} (${GreatestIncrease})")
        # "Greatest Decrease in Profits: " (month and amount)
    print(f"Greatest Decrease in Profits: {MinMonth} (${GreatestDecrease})")

    #export a text file with results (how do we do that?)

