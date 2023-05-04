import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

output_file = os.path.join("analysis", "analysis.txt")
    
with open(election_data_csv, 'r') as csvfile, open(output_file, 'w') as outfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print("Election Results\n")
    print("Election Results\n", file=outfile)
    print("------------------------------\n")
    print("------------------------------\n", file=outfile)
    # Skip the header row
    next(csvreader)
    vote_counts = {}
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Extract the candidate name from the current row
        candidate = row[2]
        # Increment the vote count for the candidate in the dictionary
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1
    # Count the total number of votes
    total_votes = sum(vote_counts.values())
    outfile.write(f"Total Votes: {total_votes}\n")
    print(f"Total Votes: {total_votes}\n")
    outfile.write("------------------------------\n")
    print("------------------------------\n")
    # Iterate over the candidates in the vote counts
    for candidate, count in vote_counts.items():
        # Calculate the percentage of votes for the candidate
        percentage = count / total_votes * 100
        # Write the candidate name, vote count, and percentage to the output file
        print(f"{candidate}: {percentage:.3f}% ({count})\n")
        outfile.write(f"{candidate}: {percentage:.3f}% ({count})\n")
        
  
    print("------------------------------\n")   
    outfile.write("------------------------------\n")
        # Find the candidate with the highest vote count
    winner = max(vote_counts, key=vote_counts.get)
    outfile.write(f"Winner: {winner}\n")
    print(f"Winner: {winner}\n")
    outfile.write("------------------------------\n")
    print("------------------------------\n")