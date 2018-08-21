import os
import csv

pypoll_csv = os.path.join("C:/Users/matt/Desktop/election_data.csv")

with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    voter_id = []
    county = []
    candidate = []
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    total_votes = (len(voter_id))

    individual_candidate = set(candidate)
    
    print(" ")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    
    counts=[]
    candidate_counts=[]
    for each in individual_candidate:
        count = 0
        percent = 0
        for row in candidate:
            if row == each:
                count = count + 1
        percent = round(((count/total_votes)*100),2)  
        print(each + ": " + str(percent) + "% (" + str(count) + ") ") 
        counts.append(count)
        candidate_counts.append(each)
    
    print("-------------------------")
        
    winner = max(zip(counts,candidate_counts))[1]
    print("Winner: " + winner)
    
    print("-------------------------")
    print(" ")    