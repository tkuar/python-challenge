# Tameka Kuar
# Date: 06/05/2020
# Purpose: To analyze the data in budget_data.csv
# and print the analysis to the terminal and export
# a text file with the results

# Modules
import os
import csv 

# Set path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# List to store data
month = []
profit_losses = []

# Function that calcualtes the average of a lsit
def average(num):
    
    length = len(num)
    
    return (sum(num)/length)

# Open budget_data.csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
        
        month.append(row[0])
        profit_losses.append(row[1])

# Calulates the total months in budget_data.csv
total_months = len(month)

# Converts the values in profit_losses list to integers
num_profit_losses = list(map(int, profit_losses))

# Calulates the net total amount of Profit/Losses
total_profit_losses = sum(num_profit_losses)

# Initializes the variables that will be used to find
# the greatest increase/decrease in profit values
# and the corresponding dates
great_increase = 0
great_decrease = 0
great_increase_date = ""
great_decrease_date = ""

# Loop that find the greatest increase/decrease in profit values
for row in num_profit_losses:
    if row > great_increase:
        great_increase = row

    if row < great_decrease:
        great_decrease = row

# Reopen budget_data to assign find the date of the
# greatest increase/decrease in profit
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    
    # Loop that finds the date of greatest increase and decrease
    for row in csvreader:
        if int(row[1]) == great_increase:
            great_increase_date = row[0]
        if int(row[1]) == great_decrease:
            great_decrease_date = row[0]

# Prints the analysis to the terminal
print(f'Financial Analysis\n----------------------------\nTotal Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print('Average Change: $'+'{:.2f}'.format(average(num_profit_losses)))
print(f'Greatest Increase in Profits: {great_increase_date} (${great_increase})')
print(f'Greatest Decrease in Profits: {great_decrease_date} (${great_decrease})')

# Set variable for output file
filename = os.path.join("analysis", "financial_analysis.txt")

# Exports a text file with the results  
with open(filename, "w") as datafile:
    print(f'Financial Analysis\n----------------------------\nTotal Months: {total_months}', file=datafile)
    print(f'Total: ${total_profit_losses}', file=datafile)
    print('Average Change: $'+'{:.2f}'.format(average(num_profit_losses)), file=datafile)
    print(f'Greatest Increase in Profits: {great_increase_date} (${great_increase})', file=datafile)
    print(f'Greatest Decrease in Profits: {great_decrease_date} (${great_decrease})', file=datafile)