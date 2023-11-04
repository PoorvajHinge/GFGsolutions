#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        array.sort()
        missing=int(n*(n+1)/2-sum(array))
        return missing


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends