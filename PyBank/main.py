import os
import csv

budget_data_read = os.path.join("Resources/budget_data.csv")
budget_data_write = os.path.join("Analysis/budget_analysis.txt")

net_total_pf = 0
total_months = 0
change_pf = []
change_month = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999999999999999999]

with open(budget_data_read, "r") as financial_info:
    reader=csv.reader(financial_info)
    header = next(reader)
    first_row = next(reader)
    total_months = total_months + 1
    net_total_pf = net_total_pf + int(first_row[1])
    net_previous = int(first_row[1])

    for row in reader:
        total_months = total_months + 1
        net_total_pf = net_total_pf + int(row[1])
        net_change = int(row[1]) - net_previous
        net_previous = int(row[1])
        change_pf = change_pf + [net_change]
        change_month = change_month + [row[0]]

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

average_net_change = sum(change_pf)/len(change_pf)

output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total_pf}\n"
    f"Average Change: ${average_net_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

print(output)

with open(budget_data_write, "w") as budget_summary:
    budget_summary.write(output)