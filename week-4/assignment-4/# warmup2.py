# warmup2
# key value pairs
# A student record
student = {"name": "Chris", "grade": "C", "subjects": "basket-weaving", "height": 6.0}

for a, b in student.items():
    print(f"{a}: {b}")

student["graduated"] = "false"
print(student)

for a, b in student.items():
    print(f"{a}: {b}")