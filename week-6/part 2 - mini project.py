# part 2 -  mini project (week 6 version)
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    min_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def find_max(numbers):
    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = (
                    sorted_numbers[i + 1],
                    sorted_numbers[i],
                )
                swapped = True

    return sorted_numbers


def show_menu():
    print(
        "=== Number Cruncher ===\n"
        "1. Find minimum\n"
        "2. Find maximum\n"
        "3. Search for a number\n"
        "4. Sort the list\n"
        "5. Quit\n"
    )
    choice = input("Enter a number option (1-5): ")
    return choice


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            result = find_min(numbers)
            print("Minimum number: ", result)

        elif choice == "2":
            result = find_max(numbers)
            print("Maximum number: ", result)

        elif choice == "3":
            search_num = int(input("Enter a number to search: "))
            index = search(numbers, search_num)

            if index != -1:
                print(f"Found {search_num} at index {index}.")
            else:
                print(f"{search_num} was not found in the list.")

        elif choice == "4":
            sorted_list = bubble_sort(numbers)
            print("Original list is as follows: ", numbers)
            print("Sorted list is as follows: ", sorted_list)

        elif choice == "5":
            print("Ok. See you next time. Goodbye.")
            break

        else:
            print("This is not a valid number/entry. Please enter a number 1-5: ")


if __name__ == "__main__":
    main()
    

    