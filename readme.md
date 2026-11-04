# Functional Treat: Data Analyzer and Transformer

A menu-driven Python console application to analyze, transform, and sort 1D lists and 2D arrays. Built to demonstrate fundamental and functional Python concepts including recursion, lambda functions, `*args`, `**kwargs`, global state, and multi-value returns.

---

## What's Inside

Here is a quick breakdown of what the program practices:

* **Built-in Functions:** Computing basic statistics with `len()`, `min()`, `max()`, and `sum()`.
* **User-Defined Functions (UDFs):** Custom logic for calculating averages, finding duplicate values, extracting unique elements, and printing clean 2D grids.
* **Flexible Arguments (`*args` & `**kwargs`):** Printing multiple values dynamically with `*args` and displaying formatted summaries using `**kwargs`.
* **Function Docstrings (`__doc__`):** Using built-in docstrings to describe functions and display them directly in the menu.
* **Recursion:** Solving factorials and Fibonacci sequences recursively.
* **Lambda Functions:** Inline lambda expressions with `filter()` and `map()` to filter data by custom conditions or thresholds and format outputs.
* **Global Variables:** Storing dataset metadata in a shared `dataset_summary` dictionary using the `global` keyword.
* **Returning Multiple Values:** Returning tuples containing min, max, sum, and average, then unpacking them in the caller.
* **1D & 2D Lists:** Working with space-separated numbers or multi-row nested grids, with built-in sample data for quick testing.
* **Sorting Lists:** In-place mutable sorting with `.sort()` (ascending/descending) on 1D lists, and non-destructive row sorting with `sorted()`.

---

## Original Menu Interface

When you run `Functional Treat.py`, the terminal displays the original main menu interface:

```text
══════════════════════════════════════════════════════════
  ╔══════════════════════════════════════════════════════╗
  ║      DATA ANALYZER AND TRANSFORMER PROGRAM           ║
  ╚══════════════════════════════════════════════════════╝
══════════════════════════════════════════════════════════

┌── [ MAIN MENU ] ───────────────────────────────────────┐
│  [1] Input Data                                        │
│  [2] Display Data Summary                              │
│  [3] Calculate Factorial                               │
│  [4] Filter Data                                       │
│  [5] Sort Data                                         │
│  [6] Display Dataset Statistics                        │
│  [7] Exit Program                                      │
└────────────────────────────────────────────────────────┘
 ➤ Please enter your choice: 
```

---

## Step-by-Step Walkthrough & Screenshots

Here is how each menu option works in `Functional Treat.py`, showing the exact terminal interface alongside each screenshot from the repo:

### [1] Input Data
Allows you to enter a 1D array manually, construct a 2D matrix row by row, or load pre-set sample data.

```text
  ┌── [ STEP 1: INPUT DATA ] ────────────────────────────┐
  │  [1] Enter 1D Array Manually                         │
  │  [2] Enter 2D Array Manually                         │
  │  [3] Load Sample 1D Data                             │
  │  [4] Load Sample 2D Data                             │
  └──────────────────────────────────────────────────────┘
  ➤ Enter your option (1-4): 1                   

  ┌── [ STATUS & OUTPUT ] ────────────────────────────────
  ➤ Enter data for a 1D array (separated by spaces):
  ➤ 34 12 56 78 43 21 90
  │  [SUCCESS] Data has been stored successfully!
  └──────────────────────────────────────────────────────
```



---

### [2] Display Data Summary
Calculates essential metrics using Python's built-ins and displays them as key-value pairs via `**kwargs`.

```text
  ┌── [ STEP 2: DATA SUMMARY (BUILT-IN) ] ───────────────┐
  │  Data Summary:
  │  - Total elements: 7
  │  - Minimum value: 12
  │  - Maximum value: 90
  │  - Sum of all values: 334
  │  - Average value: 47.71
  └──────────────────────────────────────────────────────┘
```



---

### [3] Calculate Factorial
Prompts for a non-negative integer and computes its factorial recursively using the `factorial(n)` function.

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

```text
  ┌── [ STEP 3: FACTORIAL (RECURSION) ] ─────────────────┐
  ➤ Enter a number to calculate its factorial: 5

  ┌── [ RESULT ] ─────────────────────────────────────────
  │  Factorial of 5 is: 120
  └──────────────────────────────────────────────────────
```



---

### [4] Filter Data
Filters elements based on user criteria (such as filtering values greater than or equal to a threshold, or filtering even/odd numbers) using lambda functions inside `filter()` and formatting with `map()`.

```python
# Lambda threshold filtering and mapping
filtered = list(filter(lambda x: x >= threshold, current_data))
formatted = ", ".join(map(lambda x: str(x), filtered))
```

```text
  ┌── [ STEP 4: FILTER DATA (LAMBDA FUNCTION) ] ─────────┐
  ➤ Enter a threshold value to filter data above this: 50

  ┌── [ FILTERED RESULT ] ────────────────────────────────
  │  Filtered Data (values >= 50):
  │  ➤ 56, 78, 90
  └──────────────────────────────────────────────────────
```



---

### [5] Sort Data
Sorts a 1D array in-place using `.sort()` in ascending or descending order, or demonstrates non-destructive row sorting for 2D arrays using `sorted()`.

```text
  ┌── [ STEP 5: SORT DATA ] ─────────────────────────────┐
  │  [1] Ascending                                       │
  │  [2] Descending                                      │
  └──────────────────────────────────────────────────────┘
  ➤ Enter your choice: 1

  ┌── [ SORTING RESULT ] ─────────────────────────────────
  │  Sorted Data in Ascending Order:
  │  ➤ 12, 21, 34, 43, 56, 78, 90
  └──────────────────────────────────────────────────────
```



---

### [6] Display Dataset Statistics
Calls `get_dataset_statistics()`, which computes and returns multiple values in a single tuple (`min_val`, `max_val`, `total_val`, `avg_val`), then unpacks and displays them individually.

```python
def get_dataset_statistics(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    total_val = sum(numbers)
    avg_val = total_val / len(numbers)
    return min_val, max_val, total_val, avg_val
```

```text
  ┌── [ STEP 6: DATASET STATISTICS ] ────────────────────┐
  │  Dataset Statistics (Returned as multiple values):   │
  │  - Minimum value : 12                                │
  │  - Maximum value : 90                                │
  │  - Sum of values : 334                               │
  │  - Average value : 47.71                             │
  └──────────────────────────────────────────────────────┘
```



---

### [7] Exit Program
Exits the application loop cleanly and prints a closing message.

```text
══════════════════════════════════════════════════════════
  [X] Exiting the Data Analyzer Program. Goodbye!
══════════════════════════════════════════════════════════
Thank you for using the Data Analyzer and Transformer Program. Goodbye!
```



---

## File Overview

* **`Functional Treat.py`** — The primary script containing the main menu, user-defined functions, data structures, recursion, and transformation logic.
* **`Screenshots/`** — Folder containing the 7 step-by-step terminal screenshots (`image (1).png` to `image (7).png`).
