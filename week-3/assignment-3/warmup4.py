# warmup4.py
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
elif number == 0:
    print(f"{number} is zero.")

if number % 2 == 0:
    print(f"{number} is an even number.")
elif number % 2 != 0:
    print(f"{number} is an odd number.")