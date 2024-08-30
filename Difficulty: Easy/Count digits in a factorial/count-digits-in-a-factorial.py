#User function Template for python3
from math import factorial
class Solution:
    def facDigits(self,N):
        #code here
        fact = factorial(N)
        nums=[x for x in str(fact)]
        return len(nums)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.facDigits(N))
# } Driver Code Ends