
from typing import List


class Solution:
    def isPerfect(self, n : int, arr : List[int]) -> bool:
        # code here
        new_arr = arr[::-1]
        if(new_arr == arr):
            return True
        else:
            return False
        



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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isPerfect(n, arr)
        
        if res:
            print("PERFECT")
        else:
            print('NOT PERFECT')
            

# } Driver Code Ends