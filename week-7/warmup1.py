# warmup1
# Open ../data/notes.txt using a with block, read it line by line, and print each line with its number.
with open('../python-intro-homework/week-7/data/notes.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")

        

