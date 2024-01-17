#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        perms = [list(p) for p in permutations(arr)]
        new_list = [list(x) for x in set(tuple(x) for x in perms)]
        return sorted(new_list)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends