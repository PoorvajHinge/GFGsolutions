#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        N = str(N)
        s = [int(x) for x in N]
        y = sum(s)
        y = str(y)
        if y ==y[::-1]:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends