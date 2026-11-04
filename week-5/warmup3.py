# warmup3 linear search
guess = input("Enter a name to search the database: ")
names = ["Aaron", "Bamford", "Charlie", "Derrick", "Edmund", "Falcon", "Gary", "Hannah"]



def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

result = linear_search(names, guess)
if result == -1:
    print(f"The name: '{guess}' was not found in the list")
else:
    print(f"We found {guess} at index {result}")
