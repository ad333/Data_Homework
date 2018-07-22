###########################################################################################
#  Name:  Ashwini Devkota
#  Program:  PyBank
#  Summary: 
#       This program analyzes financial records of a company using revenue data from a CSV
#       file.  Then it prints the analysis to the terminal as well as exports results 
#       to a text file ("outputfile_pybank.txt").  Although the program was tested for both 
#       CSV files, the calculated results shown here were obtained using "budget_data_2.csv" 
###########################################################################################

# import modules
import os
import csv

# Set path for file
csvpath = ('budget_data_2.csv')

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the title row
    next(csvreader) 
    
    # Declare variables as empty list
    revenue = []
    date = []
    revenue_change = []

    # Loop through each row
    for row in csvreader:

        # Add date to row 0 and revenue to row 1
        date.append(row[0])
        revenue.append(int(row[1]))

    # Calculate total months and total revenue
    total_months = len(date)
    total_revenue = sum(revenue)

    # Loop through all revenue values
    for i in range(1,len(revenue)):
        
        # Calculate revenue change for every month
        revenue_change.append(revenue[i] - revenue[i-1])   
        
        # Calculate average, maximum and minimum revenue change
        avg_revenue_change = sum(revenue_change)/len(revenue_change)
        max_revenue_change = max(revenue_change)
        min_revenue_change = min(revenue_change)

        # Calculate corresponding dates for maximum and minimum revenue change
        max_revenue_change_date = str(date[revenue_change.index(max_revenue_change)])
        min_revenue_change_date = str(date[revenue_change.index(min_revenue_change)])

    # Print results to the terminal
    print("\nFinancial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(total_revenue))
    print("Avereage Revenue Change: $" + str(round(avg_revenue_change)))
    print("Greatest Increase in Revenue: " + max_revenue_change_date + " ($" + str(max_revenue_change) + ")")
    print("Greatest Decrease in Revenue: " + min_revenue_change_date + " ($" + str(min_revenue_change) + ")\n")

    # Create text output file to write and export the result
    outputfile = open("outputfile_pybank.txt", "w")
    
    # Write results to the output file
    outputfile.write("\nFinancial Analysis\n")
    outputfile.write("-----------------------------------------\n")
    outputfile.write("Total Months: " + str(total_months) + "\n")
    outputfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    outputfile.write("Avereage Revenue Change: $" + str(round(avg_revenue_change)) + "\n")
    outputfile.write("Greatest Increase in Revenue: " + max_revenue_change_date + " ($" + str(max_revenue_change) + ")\n")
    outputfile.write("Greatest Decrease in Revenue: " + min_revenue_change_date + " ($" + str(min_revenue_change) + ")\n")
    
    # Close the output file
    outputfile.close()
