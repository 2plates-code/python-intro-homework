# warmup2
import csv

with open('../python-intro-homework/week-7/data/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings

print("\n", "*" * 20, "\n")

import csv

with open('../python-intro-homework/week-7/data/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'],": ", row['score'])