# calculates how many years until you become an octagenarian
age = int(input("Enter your age: "))
years_until_octagenarian = 80 - age
print(f"You have {years_until_octagenarian} years left until you are an octagenarian.")

# 1 Enter your age: 30
# Traceback (most recent call last):
#  File "/Users/eddy/Desktop/Code the Dream/python_class/python-intro-homework/week-2/assignment-2/warmup4.py", line 3, in <module>
#    years_until_octagenarian = 80 - age
#                               ~~~^~~~~
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

# 2 mismatched variables caused the error.
# 3 I fixed the error by converting the input to an integer using int() function.

