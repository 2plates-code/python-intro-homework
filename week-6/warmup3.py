# warmup3
# limited scope error
def add(a, b):
    total = a + b
result = add(42, 6)
#print(total)
#  File "/Users/eddy/local_Code_the_Dream/python-intro-homework/week-6/warmup3.py", line 6, in <module>
#    print(total)
#          ^^^^^
#NameError: name 'total' is not defined

# return value solution
def add(a, b):
    return a + b
result = add(42, 6)
print(result)

