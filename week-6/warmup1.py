# warmup 1

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 1. Only a name (uses the default greeting)
greet("Maya")

# 2. Name and a custom greeting (both positional)
greet("Maya", "Good day!")

# 3. Greeting passed as a keyword argument
greet("Maya", greeting="Hello")