from array import *

def selection_sort(array):
    for int in range(len(arr)):
        index = int
        
        for j in range(int+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
                
        arr[int], arr[index] = arr[index], arr[int]
        
arr = array('i', [6, 8, 67, 1, 78, 2, 9, 4, 22, 18, 30])

print("Unsorted array: ")
for x in arr:
    print(x, end= " ")
selection_sort(arr)
print("\nSorted array: ")
for x in arr:
    print(x, end = " ")