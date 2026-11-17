#part2 miniproject expense report generator
# step 1 - verify that file exists
import os
if os.path.exists("../python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    
# step 2 - read the csv file into list of dictionaries

import csv
with open('../python-intro-homework/week-7/data/expenses.csv', 'r') as file:
    expenses = list(csv.DictReader(file))
    for item in expenses:
        item['amount'] = float(item['amount'])  # step 3 - Convert the amount field to float
    for row in expenses:
        print(row)

# part 4 - Filter the list to only rows where category is "Food"
food_item = [item for item in expenses if item['category'] == 'Food']

# part 5 - Compute the total amount spent on food
total_food_expense = sum(item['amount'] for item in food_item)
print(f"Total food expense: ${total_food_expense:.2f}")

# step 6 
from datetime import datetime
now = datetime.now()
with open('../python-intro-homework/week-7/food_report.txt', 'w') as file:
    file.write("Food Expense Report — generated [" + now.strftime("%B %d, %Y") + "]")
    file.write("\ntest line test") 
    food_item = [item for item in expenses if item['category'] == 'Food']
    for item in food_item:
        file.write(f"\n{item['date']}: ${item['amount']}")
    file.write(f"\nTotal food expense: ${total_food_expense:.2f}")


