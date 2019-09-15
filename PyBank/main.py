import csv
import os

budgetCSV = os.path.join(".","Resources","budget_data.csv")
with open(budgetCSV, "r", encoding="UTF-8", newline="\n") as data:
    csvreader = csv.reader(data, delimiter=",")
    ignore_csv_header = next(csvreader)

    monthValues = []
    profitLossValues = []
    changes = []

    for row in csvreader: 
        monthValues.append( row[0] )
        profitLossValues.append( int(row[1]) )

    for i in range(len(profitLossValues)-1):
        changes.append( profitLossValues[i+1] - profitLossValues[i] )

max_increase = max(changes)
max_decrease = min(changes)
increase_month_index = changes.index( max_increase ) + 1
decrease_month_index = changes.index( max_decrease ) + 1

report = f'''
    Financial Analysis
    ----------------------------
    Total Months: {len(profitLossValues)}
    Total: ${sum(profitLossValues)}
    Average  Change: ${ round( sum(changes) / len(changes), 2) }
    Greatest Increase in Profits: {monthValues[ increase_month_index ]}  (${ max_increase })
    Greatest Decrease in Profits: {monthValues[ decrease_month_index ]} (${ max_decrease })
'''

file1 = open("PyBankReport.txt", "w")  # write mode
file1.write(report)
file1.close()

print(report)
