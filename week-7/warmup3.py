# warmup3 - part 1
import os
print(os.getcwd())  # printing current working directory

print("\n", "*" * 20, "\n") # part 2

import os
if os.path.exists("../python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print("\n", "*" * 20, "\n") # part 3

import os
path = os.path.join("../python-intro-homework/week-7", "data", "expenses.csv")
print(path)