def maxProduct(array, n):
    maxVal = array[0]
    minVal = array[0]
    maxProduct = array[0]
    for i in range(1,n):
        if (array[i] < 0):
            temp = maxVal
            maxVal = minVal
            minVal = temp

        maxVal = max(array[i], maxVal * array[i])
        minVal = min(array[i], minVal * array[i])
        maxProduct = max(maxVal, maxProduct)
        # print("maxVal",maxVal)
        # print("minVal",minVal)
    return maxProduct
if __name__=='__main__':
    # arr = [-1,-3,-10,0,60]
    elements = input("Enter Array Elements: ")
    ls=list(elements.split(","))
    arr=[]
    for i in range (len(ls)):
        ls[i].isdigit()
        ls[i]=int(ls[i])
        arr.append(ls[i])
    print("Array Elements: ",arr)
    n = len(arr)
    print("Maximum Subarry product is",maxProduct(arr,n))