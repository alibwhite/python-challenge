import os
import csv

budget_data_read = os.path.join("Resources/budget_data.csv")
budget_data_write = os.path.join("Analysis/budget_analysis.txt")

with open(budget_data_read) as financial_info:
    reader=csv.reader(financial_info)
    header = next(reader)