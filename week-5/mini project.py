# mini project - number cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print(
        "=== Number Cruncher ===\n"
        "1. Find minimum\n"
        "2. Find maximum\n"
        "3. Search for a number\n"
        "4. Sort the list\n"
        "5. Quit\n"
    )
    try:
        guess = input("Enter a number option (1-5): ")

        if guess == "1":
            minimum = numbers[0]
            for num in numbers:
                if num < minimum:  
                    minimum = num
            print("Minimum number: " , minimum)
            
        elif guess == "2":
            maximum = numbers[0]
            for num in numbers:
                if num > maximum:
                    maximum = num
            print("Maximum number: " , maximum)
            
        elif guess == "3":
            search_num = int(input("Enter a number to search: "))

            found = False

            for i in range(len(numbers)):
                if numbers[i] == search_num:
                    print(f"Found {search_num} at index {i}.")
                    found = True
                    break

            if not found:
                         print(f"{search_num} was not found in the list.")

            
        elif guess == "4":
            swapped = True

            while swapped:
                swapped = False

                for i in range(len(numbers)-1):
                     if numbers[i] > numbers[i+1]:
                        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                        swapped = True
            print("Sorted list is as follows: ", numbers)
            
        elif guess == "5":
            print("Ok. See you next time. Goodbye.")
            break
            
        else:
            print("This is not a valid number/entry. Please enter a number 1-5: ")
            
    except ValueError:
        print("This is not a valid number/entry. Please enter a number 1-5: ")

    
    

    