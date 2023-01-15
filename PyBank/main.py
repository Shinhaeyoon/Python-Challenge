# import modules
import os
import csv

# set path of csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# counter for total months, net profit, value, change between consecutive row
total_months = 0
total_profit = 0
value = 0
change = 0

# set the lists of date and profit/loss
dates = []
profits = []

# open csv file
with open(csvpath) as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    csv_header = next(cr)
    
    first_row = next(cr)

    # total_months counter
    total_months += 1

    # get net profit by keep adding each profit (from column #1)
    total_profit += int(first_row[1])
    value = int(first_row[1])

    # add date, change between profit in each list
    for row in cr:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_months += 1

        # sum of total_profit (=net profit)
        total_profit = total_profit + int(row[1])

        # Calculate average by dividing sum of profits by number of elements in the list
        avg = sum(profits)/len(profits)

    # define greatest increase/decrease as max/min value in the list, and find the date by using index
    greatest_increase = max(profits)
    greatest_increase_index = profits.index(greatest_increase)
    greatest_increase_date = dates[greatest_increase_index]

    greatest_decrease = min(profits)
    greatest_decrease_index = profits.index(greatest_decrease)
    greatest_decrease_date = dates[greatest_decrease_index]

# print output
printoutput = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: {total_profit}\n"
f"Average Change: ${str(round(avg, 2))}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})" )
print(printoutput)


# export output as text file
output = os.path.join('analysis', 'PyBank.txt')
PB_output = open(output, "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = f"Total Months: {total_months}"
line4 = f"Total: {total_profit}"
line5 = f"Average Change: ${str(round(avg, 2))}"
line6 = f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}"
line7 = f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
PB_output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
