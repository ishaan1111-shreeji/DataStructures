# def getLeaders(array,length):
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            curr = arr[i]
            arr[i] = curr_max
            if curr>curr_max:
                curr_max = curr
        return arr
if __name__=="__main__":
    ls=[17,18,5,4,6,1]
    solution_1 =Solution()
    array=solution_1.replaceElements(ls)
    print(array)

