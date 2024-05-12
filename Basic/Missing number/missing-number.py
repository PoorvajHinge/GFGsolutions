
from typing import List


class Solution:
    def missingNumber(self, n : int, arr : List[int]) -> int:
        # code here
        sum1 = sum(arr)             #8
        sum2 = n*(n+1)//2           #10
        return sum2-sum1
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n-1)
        
        obj = Solution()
        res = obj.missingNumber(n, arr)
        
        print(res)
        

# } Driver Code Ends