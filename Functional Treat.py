dataset_summary = {}
collected_data = []
is_2d = False

border = "═" * 58
divider = "─" * 58


def display_values(*args):
    """Accepts multiple values using *args and displays them."""
    print("  │  Values:", ", ".join(map(str, args)))


def print_summary(**kwargs):
    """Prints key-value pairs as a summary of dataset characteristics using **kwargs."""
    for key, value in kwargs.items():
        print(f"  │  - {key}: {value}")


def calculate_average(numbers):
    """User-defined function to calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_duplicates(numbers):
    """User-defined function to find duplicate values in a list."""
    duplicates = []
    seen = []
    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates


def display_unique_values(numbers):
    """User-defined function to return unique values from a list."""
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """Calculates the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def get_dataset_statistics(numbers):
    """Returns multiple statistics: minimum, maximum, sum, and average."""
    min_val = min(numbers)
    max_val = max(numbers)
    total_val = sum(numbers)
    avg_val = total_val / len(numbers)
    return min_val, max_val, total_val, avg_val


def display_grid(matrix):
    """Displays a 2D list in a formatted grid structure."""
    print("  │  [ Formatted 2D Grid ]")
    for row in matrix:
        print("  │    ", end="")
        for val in row:
            print(f"{val:4}", end=" ")
        print()


def input_data():
    """Input Data"""
    global collected_data, is_2d, dataset_summary

    print("\n" + divider + "\n")
    print("  ┌── [ STEP 1: INPUT DATA ] ────────────────────────────┐")
    print("  │  [1] Enter 1D Array Manually                         │")
    print("  │  [2] Enter 2D Array Manually                         │")
    print("  │  [3] Load Sample 1D Data                             │")
    print("  │  [4] Load Sample 2D Data                             │")
    print("  └──────────────────────────────────────────────────────┘")

    choice = input("  ➤ Enter your option (1-4): ").strip()

    print("\n  ┌── [ STATUS & OUTPUT ] " + ("─" * 32))
    if choice == "1":
        data_input = input("  ➤ Enter data for a 1D array (separated by spaces):\n  ➤ ")
        collected_data = [int(x) for x in data_input.split()]
        is_2d = False
        print("  │  [SUCCESS] Data has been stored successfully!")
    elif choice == "2":
        rows = int(input("  ➤ Enter number of rows: "))
        matrix = []
        for r in range(rows):
            row_input = input(f"  ➤ Enter values for row {r + 1} (separated by spaces):\n  ➤ ")
            matrix.append([int(x) for x in row_input.split()])
        collected_data = matrix
        is_2d = True
        print("  │  [SUCCESS] Data has been stored successfully!")
        display_grid(collected_data)
    elif choice == "3":
        collected_data = [34, 12, 56, 78, 43, 21, 90]
        is_2d = False
        print("  │  [INFO] Loaded Sample 1D Data: 34 12 56 78 43 21 90")
        print("  │  [SUCCESS] Data has been stored successfully!")
    elif choice == "4":
        collected_data = [[12, 34, 56], [78, 90, 21], [43, 65, 87]]
        is_2d = True
        print("  │  [SUCCESS] Loaded Sample 2D Data successfully!")
        display_grid(collected_data)
    else:
        print("  │  [!] Invalid choice, returning to menu.")
    print("  └" + ("─" * 54))

    if not is_2d and len(collected_data) > 0:
        dataset_summary = {"Total elements": len(collected_data), "Average value": round(calculate_average(collected_data), 2)}


def display_summary():
    """Display Data Summary (Built-in Functions)"""
    global dataset_summary
    print("\n" + divider + "\n")
    print("  ┌── [ STEP 2: DATA SUMMARY (BUILT-IN) ] ───────────────┐")

    if is_2d:
        flat = [item for sublist in collected_data for item in sublist]
        if not flat:
            print("  │  [!] No data available. Please input data first.     │")
            print("  └──────────────────────────────────────────────────────┘")
            return
        total_elements = len(flat)
        min_value = min(flat)
        max_value = max(flat)
        sum_value = sum(flat)
        avg_value = round(sum_value / total_elements, 2)
    else:
        if len(collected_data) == 0:
            print("  │  [!] No data available. Please input data first.     │")
            print("  └──────────────────────────────────────────────────────┘")
            return
        total_elements = len(collected_data)
        min_value = min(collected_data)
        max_value = max(collected_data)
        sum_value = sum(collected_data)
        avg_value = round(calculate_average(collected_data), 2)

    dataset_summary["Total elements"] = total_elements
    dataset_summary["Average value"] = avg_value

    print("  │  Data Summary:")
    print_summary(**{"Total elements": total_elements, "Minimum value": min_value, "Maximum value": max_value, "Sum of all values": sum_value, "Average value": avg_value})
    print("  └──────────────────────────────────────────────────────┘")


def calculate_factorial_menu():
    """Calculate Factorial (Recursion)"""
    print("\n" + divider + "\n")
    print("  ┌── [ STEP 3: FACTORIAL (RECURSION) ] ─────────────────┐")
    num = int(input("  ➤ Enter a number to calculate its factorial: "))

    print("\n  ┌── [ RESULT ] " + ("─" * 41))
    if num < 0:
        print("  │  [!] Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"  │  Factorial of {num} is: {result}")
    print("  └" + ("─" * 54))


def filter_data():
    """Filter Data by Threshold (Lambda Function)"""
    print("\n" + divider + "\n")
    print("  ┌── [ STEP 4: FILTER DATA (LAMBDA FUNCTION) ] ─────────┐")
    if len(collected_data) == 0:
        print("  │  [!] No data available. Please input data first.     │")
        print("  └──────────────────────────────────────────────────────┘")
        return

    threshold = int(input("  ➤ Enter a threshold value to filter data above this: "))

    if is_2d:
        flat = [item for sublist in collected_data for item in sublist]
        target = flat
    else:
        target = collected_data

    filtered = list(filter(lambda x: x >= threshold, target))

    print("\n  ┌── [ FILTERED RESULT ] " + ("─" * 32))
    print(f"  │  Filtered Data (values >= {threshold}):")

    formatted = ", ".join(map(lambda x: str(x), filtered))
    print(f"  │  ➤ {formatted}")
    print("  └" + ("─" * 54))


def sort_data():
    """Sort Data"""
    global collected_data
    print("\n" + divider + "\n")
    print("  ┌── [ STEP 5: SORT DATA ] ─────────────────────────────┐")
    if len(collected_data) == 0:
        print("  │  [!] No data available. Please input data first.     │")
        print("  └──────────────────────────────────────────────────────┘")
        return

    if is_2d:
        print("  │  [1] Sort rows by first value using sorted()         │")
        print("  │  [2] Sort each row in-place using sort()             │")
        print("  └──────────────────────────────────────────────────────┘")
        choice = input("  ➤ Enter your choice: ").strip()

        print("\n  ┌── [ SORTING RESULT ] " + ("─" * 33))
        if choice == "1":
            new_matrix = sorted(collected_data, key=lambda row: row[0])
            print("  │  [ Original 2D List (Preserved) ]")
            display_grid(collected_data)
            print("  │")
            print("  │  [ New Sorted 2D List (via sorted()) ]")
            display_grid(new_matrix)
        else:
            for row in collected_data:
                row.sort()
            print("  │  [ In-place Sorted 2D List (via sort()) ]")
            display_grid(collected_data)
        print("  └" + ("─" * 54))
    else:
        print("  │  [1] Ascending                                       │")
        print("  │  [2] Descending                                      │")
        print("  └──────────────────────────────────────────────────────┘")
        choice = input("  ➤ Enter your choice: ").strip()

        print("\n  ┌── [ SORTING RESULT ] " + ("─" * 33))
        if choice == "1":
            collected_data.sort()
            print("  │  Sorted Data in Ascending Order:")
            print(f"  │  ➤ {', '.join(map(str, collected_data))}")
        elif choice == "2":
            collected_data.sort(reverse=True)
            print("  │  Sorted Data in Descending Order:")
            print(f"  │  ➤ {', '.join(map(str, collected_data))}")
        else:
            print("  │  [!] Invalid sorting option.")
        print("  └" + ("─" * 54))


def display_dataset_stats():
    """Display Dataset Statistics (Return Multiple Values)"""
    print("\n" + divider + "\n")
    print("  ┌── [ STEP 6: DATASET STATISTICS ] ────────────────────┐")
    if len(collected_data) == 0:
        print("  │  [!] No data available. Please input data first.     │")
        print("  └──────────────────────────────────────────────────────┘")
        return

    if is_2d:
        target = [item for sublist in collected_data for item in sublist]
    else:
        target = collected_data

    min_val, max_val, total_val, avg_val = get_dataset_statistics(target)

    print("  │  Dataset Statistics (Returned as multiple values):   │")
    print(f"  │  - Minimum value : {min_val:<34}│")
    print(f"  │  - Maximum value : {max_val:<34}│")
    print(f"  │  - Sum of values : {total_val:<34}│")
    print(f"  │  - Average value : {avg_val:<34.2f}│")
    print("  └──────────────────────────────────────────────────────┘")


def main():
    print("\n" + border)
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║      DATA ANALYZER AND TRANSFORMER PROGRAM           ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print(border)

    while True:
        print("\n┌── [ MAIN MENU ] ───────────────────────────────────────┐")
        print("│  [1] Input Data                                        │")
        print("│  [2] Display Data Summary                              │")
        print("│  [3] Calculate Factorial                               │")
        print("│  [4] Filter Data                                       │")
        print("│  [5] Sort Data                                         │")
        print("│  [6] Display Dataset Statistics                        │")
        print("│  [7] Exit Program                                      │")
        print("└────────────────────────────────────────────────────────┘")

        choice = input(" ➤ Please enter your choice: ").strip()

        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            calculate_factorial_menu()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_dataset_stats()
        elif choice == "7":
            print("\n" + border)
            print("  [X] Exiting the Data Analyzer Program. Goodbye!")
            print(border + "\n")
            break
        else:
            print("\n  [!] Invalid choice. Please select an option from 1 to 7.")


main()
