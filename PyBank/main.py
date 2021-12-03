import os
import csv

budget_data_read = os.path.join("Resources/budget_data.csv")
budget_data_write = os.path.join("Analysis/budget_analysis.txt")

net_total_pf = 0
total_months = 0
change_pf = []
change_month = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

with open(budget_data_read) as financial_info:
    reader=csv.reader(financial_info)
    header = next(reader)
    first_row = next(reader)
    


output = (
    f"Financial Analysis"
    f"------------------"
    f"Total Months: {total_months}"
    f"Total: ${net_total}"
    f"Average Change: ${average_change}"
    f"Greatest Increase in Profits: {greatest_increase}"
    f"Greatest Decrease in Profits: {greatest_decrease}"

print(output)

with open(budget_data_write, "w") as budget_summary:
    budget_summary.write(output)