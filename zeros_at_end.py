def moveZeroes(array, length):
    j = 0
    for i in range(0, length):
        # print("Before>>>>>>>>array_i_{}".format(i), array[i])
        # print("Before>>>>>>>>array_j_{}".format(j), array[j])
        if array[i] != 0:
            # Partitioning the array
            array[j], array[i] = array[i], array[j]
            # print("AFTER>>>>array_i_{}".format(i), array[i])
            # print("AFTER>>>>>>>>>array_j_{}".format(j), array[j])
            j += 1

    return array


if __name__ == "__main__":
    # array = [5, 6, 0, 4, 6, 0, 9, 0, 8]
    elements = (input("Enter Elements of Array: "))
    ls = list(elements.split(","))
    arr = []
    for i in range(len(ls)):
        ls[i].isdigit()
        ls[i] = int(ls[i])
        arr.append(ls[i])
    print("Input Array: ",arr)
    n = len(arr)
    array = moveZeroes(arr, n)
    print("Output Array : ",array)
