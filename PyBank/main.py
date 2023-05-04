import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

prev_value = None
total_change = 0
num_changes = 0
output_file = os.path.join("analysis", "analysis.txt")
    
with open(budget_data_csv, 'r') as csvfile, open(output_file, 'w') as outfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    outfile.write("Financial Analysis\n")
    print("Financial Analysis\n")
    outfile.write("---------------------------------\n")
    print("---------------------------------\n")
   # Skip the header row
    next(csvreader)
    # Create a set to store unique months
    months = set()
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Extract the month value from the current row
        month = row[0]
        # Add the month value to the set
        months.add(month)
    # Count the number of unique months
    num_months = len(months)
    outfile.write(f"Total Months: {num_months}\n")
    print(f"Total Months: {num_months}\n")

    # Re-open the CSV file to iterate over it again
    csvfile.seek(0)
    next(csvreader) # skip header row

    # Initialize variables to store the previous value and the total change
    prev_value = None
    total = 0 
    total_change = 0
    num_changes = 0
    max_increase = None
    max_decrease = None
    max_decrease_row = None
    max_increase_row = None

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Extract the value from the current row and convert it to an integer
        value = int(row[1])
        total += value # accumulate the total

        # If this is not the first row, calculate the difference from the previous row
        if prev_value is not None:
            change = value - prev_value
            total_change += change
            num_changes += 1
            
            # Check if this is the new maximum increase, and update the corresponding row
            if max_increase is None or change > max_increase:
                max_increase = change
                max_increase_row = row

            # Check if this is the new maximum decrease, and update the corresponding row
            if max_decrease is None or change < max_decrease:
                max_decrease = change
                max_decrease_row = row

        # Set the current value as the previous value for the next iteration
        prev_value = value

    # Write the total to the output file
    outfile.write(f"Total: ${total}\n")
    print(f"Total: ${total}\n")

    # Calculate the average change, or print a message if there were no changes
    if num_changes > 0:
        avg_change = total_change / num_changes
        outfile.write(f"Average Change: ${avg_change:.2f}\n")
        print(f"Average Change: ${avg_change:.2f}\n")
    if max_increase_row is not None:
        outfile.write(f"Greatest Increase in Profits: {max_increase_row[0]} (${max_increase:.0f})\n")
        print(f"Greatest Increase in Profits: {max_increase_row[0]} (${max_increase:.0f})\n")
    if max_decrease_row is not None:
        outfile.write(f"Greatest Decrease in Profits: {max_decrease_row[0]} (${max_decrease:.0f})\n")
        print(f"Greatest Decrease in Profits: {max_decrease_row[0]} (${max_decrease:.0f})\n")
        