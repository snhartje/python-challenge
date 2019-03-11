# Import modules and list file path
import os
import csv

PyBank_csv = os.path.join("../PyBank", "Python_PyBank_Resources_budget_data.csv")

# Open and read PyBank_csv
with open(PyBank_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row first (check that its reading csv file properly)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #create a dictionary of the values in PyBank_csv (and print to check that it works)
    mydict = {rows[0]:int(rows[1]) for rows in csvreader}
    print(mydict)

    #Calculate number of months in data and create variable to hold the number
    NumMonths = len(mydict)
    
    #Calculate total profit/loss and create a variable to hold the sum
    TotalProfit = sum(mydict.values())
    
    #average change = (sum profit/loss - first profit/loss)/total num of months
    AverageChange = TotalProfit/NumMonths

    #add monthly change to dictionary - monthly change equals current profit/loss - previous profit/loss
    oldkey="Jan-2010"
    for key in mydict.keys():
        MonthlyChange = mydict(key)-mydict(oldkey)
        oldkey = key
        print(MonthlyChange)

        #greatest increase = largest monthly change

        #greatest decrease = smallest monthly change

    #print results (look up how to go to next line so can print in one command) 
    print(f"Financial Analysis")   
        # spacer row of "---------------------------"
    print(f"---------------------------------------------------")    
        # "Total Months: " (total num of months)
    print(f"Total Months: {NumMonths}")
        # "Total: " (sum profit/loss)
    print(f"Total: {TotalProfit}")
        # "Average Change: "
    print(f"Average Change: {AverageChange}")
        # "Greatest Increase in Profits: "(month and amount)
    print(f"Greatest Increase in Profits: ")
        # "Greatest Decrease in Profits: " (month and amount)
    print(f"Greatest Decrease in Profits: ")

    #export a text file with results (how do we do that?)

