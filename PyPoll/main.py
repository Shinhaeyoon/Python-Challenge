# import modules
import os
import csv

# set path of csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# counter for total number of votes
total_votes = 0

# make the lists of candidates, number of votes, percentage of votes
candidates = []
num_votes = []
percent_votes = []

# open csv file
with open(csvpath) as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    csv_header = next(cr)

    # add name of candidates in the list of candidates, add one more vote to number of votes   
    for row in cr:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)

        # if the candidate is already in the list, skip adding in the list of candidates, only add one more vote to number of votes        
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # calculate the percentage of votes and add to the list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percent_votes.append(percentage)

    # find out winner by getting the maximum value from the list
    winner = max(num_votes)
    winner_index = num_votes.index(winner)
    winning_candidate = candidates[winner_index]

# print the output
print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(round(percent_votes[i],3))}% ({str(num_votes[i])})")
print("----------------------------")
print(f"Winner: {winning_candidate}")
print("----------------------------")



# export output as text file
output = os.path.join('analysis', 'PyPoll.txt')
PP_output = open(output, "w")

line1 = "Election Results"
line2 = "----------------------------"
line3 = f"Total Votes: {total_votes}"
line4 = "----------------------------"
PP_output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(round(percent_votes[i],3))}% ({str(num_votes[i])})")
    PP_output.write('{}\n'.format(line))
line5 = "----------------------------"
line6 = f"Winner: {winning_candidate}"
line7 = "----------------------------"
PP_output.write('{}\n{}\n{}\n'.format(line5, line6, line7))