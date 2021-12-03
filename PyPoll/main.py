import os
import csv

poll_data_read = os.path.join("Resources/election_data.csv")
poll_data_write = os.path.join("Analysis/election_analysis.txt")

total_votes = 0
winning_votes = 0
candidate_choices = []
candidate_votes = {}
winning_candidate = ""

with open(poll_data_read, "r") as election_info:
    reader=csv.reader(election_info)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_choices:
            candidate_choices.append(candidate_name)
            candidate_votes[candidate_name] = 0

        if candidate_name in candidate_choices:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100

        if (votes > winning_votes):
            winning_votes = votes
            winning_candidate = candidate

with open(poll_data_write, "w") as poll_summary:

    output_one = (
        f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------\n"
    )
    print(output_one, end="")
    poll_summary.write(output_one)

    output_two = (
        f"{candidate}: {vote_percent}% ({votes})\n"
    )
    print(output_two, end="")
    poll_summary.write(output_two)

    output_three = (
        f"----------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------\n"
    )
    print(output_three, end="")
    poll_summary.write(output_three)