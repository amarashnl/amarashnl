def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binarySearch(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

def user_input():
    while True:
        try:
            n = int(input("Enter the number of elements: "))
            if 3 <= n <= 5:
                break
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input!.")

    arr = []
    for i in range(n):
        while True:
            try:
                element = int(input("Enter value: "))
                arr.append(element)
                break
            except ValueError:
                print("Please enter a valid input.")

    return arr

def main():
    while True:
        arr = user_input()

        print("Unsorted Array:", arr)

        bubbleSort(arr)
        print("Sorted Array:", arr)

        while True:
            try:
                target = int(input("Enter the number to be searched: "))
                break
            except ValueError:
                print("Please enter a valid input.")

        if binarySearch(arr, target):
            print(f"The element {target} is found!")
            break
        else:
            print(f"The element {target} is not in the list. Try again.")

if __name__ == "__main__":
    main()
