# warmup 1 - letter grades
# scores range from 0 to 100
# grades range from A to F
# the score is hardcoded and displays score along with corresponding letter grade
score = 89
print(f"Score: {score}")
grade = ""

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")