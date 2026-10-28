# Mini-Project — Student Roster Analyzer
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
# part 1 - highest score 
high_score = 0
high_scoring_student = "nobody"

for student in students:
    score = student["score"]

    if score > high_score:
        high_score = score
        high_scoring_student = student["name"]

print(f"High Scorer: {high_scoring_student}; {high_score}")
print("---------------")

# part 2 - average score
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")
print("_______________")

# part 3 - unique subjects
unique_subjects = set()
for student in students:
    subject = student["subject"]
    unique_subjects.add(subject)

print(f"Subjects offered: {unique_subjects}")
print("_______________")

# part 4 - list of high scorers
high_scorers = []
for student in students:
    if student["score"] >75:
        high_scorers.append(student["name"])
print(high_scorers)   