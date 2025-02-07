import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt") 

total_months = 0
net_total = 0
changes = []  
previous_month_profit_loss = None  


with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)  

    for row in reader:
        total_months += 1
        current_month_profit_loss = int(row[1])
        net_total += current_month_profit_loss

        
        if previous_month_profit_loss is not None:
            change = current_month_profit_loss - previous_month_profit_loss
            changes.append(change)
        previous_month_profit_loss = current_month_profit_loss

average_change = sum(changes) / len(changes) if changes else 0
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0
results = [
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase} (${greatest_increase})",
    f"Greatest Decrease in Profits: {greatest_decrease} (${greatest_decrease})"
]
with open(file_to_output, 'w') as txt_file:
    for line in results:
        txt_file.write(line + '\n')
    print(f"Analysis saved to {file_to_output}")