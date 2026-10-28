# warmup1.py
# hardcoded list of 8 numbers
list = [34, 95, -5, 7084, 0, -584, 33, 12]
print(list[0]) # should print first number in list; 34
print(list[-1]) # should print last number in list; 12
print(list[2:6]) # should print the middle 4 numbers in list; -5, 7084, 0, -584
print(list[::-1]) # should print the list in reverse order 
my_set = set(list)
my_set.add(33)
print(my_set)