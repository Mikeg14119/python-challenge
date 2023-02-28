import os

#Set path for file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#Initialize variables
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

#Open the CSV file and read in the data
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip the header row
    next(csvreader)
    #Loop through each row in the CSV file
    for row in csvreader:
        #Increment the total vote count
        total_votes += 1
        #Get the candidate name from the row
        candidate = row[2]
        #If the candidate hasn't been seen before, add them to the dictionary with a vote count of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        #If the candidate has been seen before, increment their vote count
        else:
            candidates[candidate] += 1

#Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#Loop through the dictionary of candidates and calculate their vote percentages
for candidate in candidates:
    votes = candidates[candidate]
    percent = votes / total_votes * 100
    print(f"{candidate}: {percent:.3f}% ({votes})")
    #Check if this candidate has more votes than the current winning candidate
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Export the results to a text file
output_path = os.path.join("election_results.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        votes = candidates[candidate]
        percent = votes / total_votes * 100
        txtfile.write(f"{candidate}: {percent:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
