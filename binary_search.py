# Binary search follows the divide and conquer approach in which the list is divided into two halves,
# and the item is compared with the middle element of the list.
# The data structure must be sorted.

def binarySearch(array,start_index,end_index,value):
    # print(array)
    # print(start_index)
    # print(end_index)
    if end_index>=start_index:

        mid_index=start_index+(end_index-start_index)//2
        # print("mid_index",mid_index)

        if array[mid_index]==value:
            return mid_index

        elif array[mid_index]>value:
            return binarySearch(array,start_index,mid_index-1,value)

        else:
            return binarySearch(array,mid_index+1,end_index,value)

    return -1
if __name__=="__main__":

    a=input("Enter elements: ")
    ls=list(a.split(","))
    # print(ls)
    # print(len(ls))
    array=[]
    for i in range(len(ls)):
        ls[i].isdigit()
        ls[i]=int(ls[i])
        array.append(ls[i])
    print("array",array)
    # print(">>>>",len(array))
    value=int(input("Enter Element to be Searched : "))
    result=binarySearch(array,0,len(array)-1,value)
    if result!=-1:
        print("Index of Element is : ",result)
    else:
        print("!!! Element Not Present !!!")