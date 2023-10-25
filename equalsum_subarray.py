# Split an array into two equal Sum subarrays
length = int(input("Enter length of Array: "))
elements = input("Enter elements:")
ls = list(elements.split(","))
ls = ls[:length]
array = []
for i in range(length):
    if ls[i].isdigit():
        a = int(ls[i])
        array.append(a)
print("ls: ", ls)
print("Array: ", array)


def SplitPoint(array, length):
    leftsum = 0
    for i in range(length):
        leftsum += array[i]
    print("leftsum: ", leftsum)
    rightsum = 0
    for i in range(length - 1, -1, -1):
        rightsum += array[i]
        print("rightsum: ", rightsum)
        leftsum -= array[i]
        print(">>>>",leftsum)
        if (rightsum == leftsum):
            return i
    return -1
def printTwoParts(array,length):
    splintpoint=SplitPoint(array,length)
    if (splintpoint==-1 or splintpoint==length):
        print("Not Possible To Split")
        return
    for i in range(0,length):
        if (splintpoint==i):
            print(" ")
        print(array[i],end=" ")
printTwoParts(array, length)
