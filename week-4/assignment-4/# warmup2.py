# warmup2
# key value pairs
# A student record
student = {"name": "Chris", "grade": "C", "subjects": ["basket-weaving", "freediving", "interpretative dancing"]}

for a, b in student.items():
    print(f"{a}: {b}")

student["graduated"] = False
print(student)

for a, b in student.items():
    print(f"{a}: {b}")