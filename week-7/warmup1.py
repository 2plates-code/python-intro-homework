# warmup1


with open('../python-intro-homework/week-7/data/notes.txt', 'r') as file:
    lines = file.readlines()  # Returns a list — one string per line
    print("Line 1:",lines[0].strip()) 
    print("Line 2:",lines[1].strip())
    print("Line 3:",lines[2].strip())
    print("Line 4:",lines[3].strip())    

