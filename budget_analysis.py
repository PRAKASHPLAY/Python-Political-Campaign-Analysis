import pandas as pd
budget_data = pd.read_csv('/Users/prakashmaddirala/Downloads/Starter_Code-2/PyBank/Resources/budget_data.csv')
total_months = budget_data.shape[0]
print(f'total numebr of motnhs: {total_months}')
net_total = budget_data['Profit/Losses'].sum()
print(f'Net total amount of Profit/Losses:{net_total}')
budget_data['Change'] = budget_data['Profit/Losses'].diff()
average_change = budget_data['Change'].mean()
print(f'average change in profit/losses: {average_change}')
greatest_increase = budget_data.loc[budget_data['Change'].idxmax()]
print(f'Greatest Increase in profits: {greatest_increase["Date"]} (${greatest_increase["Change"]})')
greatest_decrease = budget_data.loc[budget_data['Change'].idxmin()]
print(f'Greatest Decrease in profits: {greatest_decrease["Date"]} (${greatest_decrease["Change"]})')
output_text = f""" Budget Analysis Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["Date"]} (${greatest_increase["Change"]})
GreatestDecrease in Profits: {greatest_decrease["Date"]} (${greatest_decrease["Change"]})"""
output_file =('/Users/prakashmaddirala/python-challenge/PyBank/Analysis/budget_analysis.txt')
with open(output_file, 'w') as file:
    file.write(output_text)
    print(f"Analysis saved to {output_file}")