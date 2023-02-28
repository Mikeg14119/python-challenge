import os
import csv

#Path to collect data from the Resources folder
budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Set initial values for Variables
total_months = 0
net_total = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]
total_change = 0
previous_profit_loss = 0

#Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csvreader)

    #Loop through the rows in the CSV file
    for row in csvreader:
        #Count the total number of months in the dataset - increases every row 
        total_months += 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        #Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_change += change
            average_change = round(total_change / (total_months - 1), 2)
            
            #Find the greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
                
            #Find the greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
        #Set previous profit/loss for next iteration
        previous_profit_loss = current_profit_loss

#Have the analysis print to the terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#Export text file with the results of the analysis
output_path = os.path.join('PyBank', 'Analysis', 'financial_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
