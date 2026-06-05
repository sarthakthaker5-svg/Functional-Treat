dataset = []
summary = {}

def input_data():
    "Input 1D array data"
    global dataset
    data = input("Enter data for a 1D array (separated by spaces): ")
    dataset = list(map(int, data.split()))
    print("\nData has been stored successfully!")

def display():
    "Display basic statistics using built-in functions"
    if not dataset:
        print("No data available!")
        return
    print("\nData Summary:")
    print("- Total elements:", len(dataset))
    print("- Minimum value:", min(dataset))
    print("- Maximum value:", max(dataset))
    print("- Sum of all values:", sum(dataset))
    print("- Average value:", round(sum(dataset)/len(dataset), 2))

def factorial(n):
    "Recursive factorial function"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    "Calculate factorial using recursion"
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"\nFactorial of {num} is: {factorial(num)}")

def filter_data():
    "Filter data using lambda"
    if not dataset:
        print("No data available!")
        return

    value = int(input("Enter a value value to filter out data above this value: "))

    result = list(filter(lambda x: x >= value, dataset))

    print(f"\nFiltered Data (values >= {value}):")
    print(*result, sep=", ")

def sort():
    "Sort data ascending or descending"
    if not dataset:
        print("No data available!")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    temp = dataset.copy()

    if choice == 1:
        temp.sort()
        print("\nSorted Data in Ascending Order:")
    else:
        temp.sort(reverse=True)
        print("\nSorted Data in Descending Order:")

    print(*temp, sep=", ")

def statistics():
    "Return multiple values"
    if not dataset:
        print("No data available!")
        return

    minimum = min(dataset)
    maximum = max(dataset)
    total = sum(dataset)
    average = round(total / len(dataset), 2)

    return minimum, maximum, total, average

def display_statistics():
    "Display returned statistics"
    result = statistics()

    if result:
        mn, mx, total, avg = result

        print("\nDataset Statistics:")
        print("- Minimum value:", mn)
        print("- Maximum value:", mx)
        print("- Sum of all values:", total)
        print("- Average value:", avg)

def show_args(*args):
    "Display multiple values using *args"
    print("\nValues using *args:")
    for i in args:
        print(i)

def show_kwargs(**kwargs):
    "Display summary using **kwargs"
    print("\nDataset Summary using **kwargs:")
    for key, value in kwargs.items():
        print(key, ":", value)

while True:

    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by value (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Display *args and **kwargs Demo")
    print("8. Exit Program")

    choice = input("\nPlease enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display()

    elif choice == "3":
        calculate_factorial()

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort()

    elif choice == "6":
        display_statistics()

    elif choice == "7":
        show_args(*dataset)

        if dataset:
            show_kwargs(
                Total_Elements=len(dataset),
                Minimum=min(dataset),
                Maximum=max(dataset),
                Sum=sum(dataset),
                Average=round(sum(dataset)/len(dataset), 2)
            )

    elif choice == "8":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice!")