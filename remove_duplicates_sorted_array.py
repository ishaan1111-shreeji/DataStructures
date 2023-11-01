# Remove duplicates from Sorted Array
# -------------------------------------------------------------------------
def removeDuplicates(array, length):
    temp = list(range(length))
    # print(">>>>>>",temp)
    # print("length temp>>>",len(temp))
    j = 0
    for i in range(0, length - 1):
        # print(array[i])
        # print(">>>>>>>>>>>>>>>>",temp[j])
        if array[i] != array[i + 1]:
            temp[j] = array[i]
            j += 1
    # print(temp)
    temp[j] = array[length - 1]
    j += 1
    # print(">>>>t", temp)
    arr=list(range(j))
    for i in range(0, j):
        array[i] = temp[i]
        arr[i]=array[i]
    return arr


if __name__ == "__main__":
    a = input("Enter elements: ")
    ls = list(a.split(","))
    ls.sort()
    array = []
    for i in range(len(ls)):
        ls[i].isdigit()
        ls[i] = int(ls[i])
        array.append(ls[i])
    print("Input Array : ", array)
    n = len(array)
    # print("length arr>>>",len(array))
    ls =list(ls)
    ls = removeDuplicates(array, n)
    #
    print("Output Array : ",ls)
