# Linear Search is defined as a sequential search algorithm that starts at one end and
# goes through each element of a list until the desired element is found,
# otherwise the search continues till the end of the data set.

def linearSearch(array, key):
    for i in range(len(array)):
        if (key == array[i]):
            return i
    return -1


if __name__ == '__main__':
    elements = input("Enter Array Elements: ")
    ls = list(elements.split(","))
    arr = []
    for i in range(len(ls)):
        ls[i].isdigit()
        ls[i] = int(ls[i])
        arr.append(ls[i])
    key = int(input("Element to Search:"))
    print("Array Elements: ", arr)
    result = linearSearch(arr, key)
    if result==-1:
        print("Element Not Present in Array")
    else:
        print("Element is at index: ", i)

# Complexity Analysis of Linear Search:
# Time Complexity:  Best Case:O(1)    Worst Case:O(n)     Average case:o(n)
# Space Complexity: O(1)