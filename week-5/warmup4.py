# warmup4 - FizzBuzz
x = range(1,31)

for number in x:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(number)
