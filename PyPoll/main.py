import os
import csv

poll_data_read = os.path.join("Resources/election_data.csv")
poll_data_write = os.path.join("Analysis/election_analysis.txt")

with open(poll_data_read) as election_info:
    reader=csv.reader(election_info)
    header = next(reader)