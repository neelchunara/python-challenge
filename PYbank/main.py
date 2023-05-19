#Import modules os and csv.This will allow us to create file paths across operating systems
import os

#Module for reading CSV files
import csv

#Set the path for the CSV file in budget data
budget_data =os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')

#Variables
total_months = 0
total_profit = 0
value = 0
change = 0

dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)
    
    #To skip header , so that we can consider only the data for calculation
    first_row = next(csvreader)
    
    total_months += 1
    total_profit += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_profit = total_profit + int(row[1])

    #Greatest increase in profits
    greatest_inc = max(profits)
    greatest_index = profits.index(greatest_inc)
    best_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_dec = min(profits)
    worst_index = profits.index(greatest_dec)
    worst_date = dates[worst_index]

    #Average change in Profit/Losses over entire period
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {best_date} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_dec)})")

#Exporing to text file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {best_date} (${str(greatest_inc)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_dec)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))