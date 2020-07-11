

import os
import csv

# IMPORTANT: Was unable to get "election_data.csv" into a csv file on VSC
# I created the code based off the previous code (PyBank) and made syntax as if I could run it
# The file was too large and kept freezing my computer, and I am still working on GitBash mastery to pull such files
# Hints on how to pull such a large file would be great

with open("..", "Resources", "election_data.csv") as csv_file:
    file = csv.reader(csv_file)
    next(file)

votes = []
candidates = []
percent_won = []
total_votes = []
popular_winner = []

votes_count = 0
candidate_votes = 0

# The total number of votes cast
# A complete list of candidates who received votes

with open(election_data.csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        votes_counts += 1

# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

for i in set(candidates):
    total_votes.append(i)
    votes.eppend(candidates.count(i))
    percent_won.append((candidates.count(i)/total_votes)*100)
    popular_winner += 1

# Same issue with PyBank, however; I was unable to run the election_data.csv file as it was too big and would not load on computer
with open(election_data.csv, "w") as textfile:
    print("Election Results", file=textfile)
    print("-----------------------------------", file=textfile)
    print(f'Total Votes: {str(total_votes)}', file=textfile)
    for i in range(candidate_votes):
        print(f'{total_votes[i]}: {percent_won)}% ({votes[i]})', file=textfile)
    winner = total_votes[votes.index(max(votes))]
    print(f'Winner: {winner}', file=textfile)