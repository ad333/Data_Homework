###########################################################################################
#  Name:  Ashwini Devkota
#  Program:  PyPoll
#  Summary: 
#       This program analyzes votes of an election using poll data from a CSV
#       file.  Then it prints the analysis to the terminal as well as exports results 
#       to a text file ("outputfile_pypoll.txt").  Although the program was tested for both 
#       CSV files, the calculated results shown here were obtained using "election_data_2.csv" 
###########################################################################################

# import modules
import os  
import csv

# Set path for file
csvpath = ('election_data_2.csv')

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the title row
    next(csvreader) 
    
    # Declare variables as empty list
    voter_id = []
    county = []
    candidate = []

    # Loop through each row
    for row in csvreader:

        # Add voter id, county and candidate to rows 0, 1 and 2
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # Calculate total votes
    total_votes = len(voter_id)
    
    # Sort candidate names
    candidate.sort()
    
    # Declare list of all unique candidates as empty list
    unique_candidate_list = []
    
    # Loop through all candidate names
    for i in range(0,len(candidate)):
        
        # Compare two candidate names at a time.  If they are different, add to unique candidate list
        if candidate[i-1] != candidate[i]:
            unique_candidate_list.append(candidate[i])

        # Do nothing if they are same
        else:
            None
    
    # Assign variables to keep count of each unique candidates
    count1 = count2 = count3 = count4 = 0
    
    # Loop through all candidates
    for i in range(0,len(candidate)):    
        
        # Check to see which unique candidate list matches the candidate names.  If matches, update the respective count
        if unique_candidate_list[0] == candidate[i]:
            count1 = count1+1
        elif unique_candidate_list[1] == candidate[i]:
            count2 = count2+1
        elif unique_candidate_list[2] == candidate[i]:
            count3 = count3+1    
        elif unique_candidate_list[3] == candidate[i]:
            count4 = count4+1 
        else:
            None        

    # Calculate percent of votes for each candidates and format the values to 2 decimal places    
    votes1_percent = float((count1 / total_votes) * 100)
    votes1_percent = round(votes1_percent, 2)
    votes2_percent = float((count2 / total_votes) * 100)
    votes2_percent = round(votes2_percent, 2)
    votes3_percent = float((count3 / total_votes) * 100)
    votes3_percent = round(votes3_percent, 2)
    votes4_percent = float((count4 / total_votes) * 100)  
    votes4_percent = round(votes4_percent, 2)

    # Compare percent votes to determine who is the winner
    if votes1_percent > votes2_percent and votes1_percent > votes3_percent and votes1_percent > votes4_percent:
        winner = unique_candidate_list[0]
    elif votes2_percent > votes1_percent and votes2_percent > votes3_percent and votes2_percent > votes4_percent:
        winner = unique_candidate_list[1]
    elif votes3_percent > votes1_percent and votes3_percent > votes2_percent and votes3_percent > votes4_percent:
        winner = unique_candidate_list[2]    
    else:
        winner = unique_candidate_list[3]        

# Print results to the terminal
print("\nElection Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
print(str(unique_candidate_list[0]) + ": " + str(votes1_percent) + "% (" + str(count1) + ")")
print(str(unique_candidate_list[1]) + ": " + str(votes2_percent) + "% (" + str(count2) + ")")
print(str(unique_candidate_list[2]) + ": " + str(votes3_percent) + "% (" + str(count3) + ")")
print(str(unique_candidate_list[3]) + ": " + str(votes4_percent) + "% (" + str(count4) + ")")
print("--------------------------")
print("Winner: " + str(winner))
print("--------------------------\n")

# Create text output file to write and export the result
outputfile = open("outputfile_pypoll.txt", "w")
    
# Write results to the output file
outputfile.write("\nElection Results\n")
outputfile.write("--------------------------\n")
outputfile.write("Total Votes: " + str(total_votes) + "\n")
outputfile.write("--------------------------\n")
outputfile.write(str(unique_candidate_list[0]) + ": " + str(votes1_percent) + "% (" + str(count1) + ")\n")
outputfile.write(str(unique_candidate_list[1]) + ": " + str(votes2_percent) + "% (" + str(count2) + ")\n")
outputfile.write(str(unique_candidate_list[2]) + ": " + str(votes3_percent) + "% (" + str(count3) + ")\n")
outputfile.write(str(unique_candidate_list[3]) + ": " + str(votes4_percent) + "% (" + str(count4) + ")\n")
outputfile.write("--------------------------\n")
outputfile.write("Winner: " + str(winner) + "\n")
outputfile.write("--------------------------\n")
    
# Close the output file
outputfile.close()
