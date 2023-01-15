import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0

candidates = []
num_votes = []
percent_votes = []


with open(csvpath) as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    csv_header = next(cr)
    
    for row in cr:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percent_votes.append(percentage)


    winner = max(num_votes)
    winner_index = num_votes.index(winner)
    winning_candidate = candidates[winner_index]


print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(round(percent_votes[i],3))}% ({str(num_votes[i])})")
print("----------------------------")
print(f"Winner: {winning_candidate}")
print("----------------------------")




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