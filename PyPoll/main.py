# Tameka Kuar
# Date: 06/05/2020
# Purpose: To analyze the data in election_data.csv
# and print the results and winner to the terminal
# and export a text file with the results

# Modules
import os
import csv 

# Set path for csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data from election_data.csv
voter = []
county = []
candidate = []

# Open and read election_data.csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    # Add Voter IDs to voter list
    # Add Counties to county list
    # Add Candidates to candidate list
    for row in csvreader:

        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Calculates the total number of votes cast
total_votes = len(voter)

# ----------------------------------------------------------------------
# Code that was used to get the all of the unique candidates
#    unique_candidate = list(set(candidate))
#    print(unique_candidate)
# ['Khan', 'Li', "O'Tooley", 'Correy'] all of the candidates
# ----------------------------------------------------------------------

# Counts the total number of votes each candidate won
khan_votes = candidate.count("Khan")
correy_votes = candidate.count("Correy")
li_votes = candidate.count("Li")
otooley_votes = candidate.count("O'Tooley")

# Calculates the percentage of votes each candidate won
khan_percent = khan_votes/total_votes
correy_percent = correy_votes/total_votes
li_percent = li_votes/total_votes
otooley_percent = otooley_votes/total_votes

# Finds the greatest number of votes
candidate_votes = [khan_votes, correy_votes, li_votes, otooley_votes]
popular_vote = max(candidate_votes)

# A dictionary whose keys are the candidates
# with vaules of their percentage of votes and total number of votes
total_candidate_vote = {"Khan": [khan_percent, khan_votes],
                        "Correy": [correy_percent, correy_votes],
                        "Li": [li_percent, li_votes],
                        "O'Tooley": [otooley_percent, otooley_votes]}

# Finds the candidate with the greatest number of votes
popular_candidate = [key for key,values in total_candidate_vote.items() if values[1] == popular_vote]

# Prints the results to the terminal
print("Election Results\n-------------------------")
print(f"Total Votes: {total_votes}\n-------------------------")
# Loop to print out candidates results
for key,values in total_candidate_vote.items():
    print(key + ": " + "{:.3%}".format(values[0]) + " (" + str(values[1]) + ")")
print(f"-------------------------\nWinner: {popular_candidate[0]}\n-------------------------")

# Set variable name for output file
output_file = os.path.join("analysis", "election_results.txt")

# Exports a text file with the results
with open(output_file, "w") as datafile:
    print("Election Results\n-------------------------", file=datafile)
    print(f"Total Votes: {total_votes}\n-------------------------", file=datafile)
    # Loop to print out candidates results
    for key,values in total_candidate_vote.items():
        print(key + ": " + "{:.3%}".format(values[0]) + " (" + str(values[1]) + ")", file=datafile)
    print(f"-------------------------\nWinner: {popular_candidate[0]}\n-------------------------", file=datafile)

