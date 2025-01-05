import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
total_votes = 0 
candidate_votes = {}
candidates = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
results = []
results.append("Candidate Names:")
for name in candidate_votes.keys():
    results.append(name)
    
results.append(f'Total number of votes cast: {total_votes}')
for candidate in candidates:
    votes_for_candidate = candidate_votes.get(candidate, 0)
    results.append(f'{candidate}: {(votes_for_candidate/total_votes)*100:.2f}% OR {votes_for_candidate} VOTES ')
winner = ""
max_votes = 0
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate
results.append(f'The winner is: {winner} with {max_votes} votes.')
with open(file_to_output, 'w') as txt_file:
    for line in results:
        txt_file.write(line + '\n')