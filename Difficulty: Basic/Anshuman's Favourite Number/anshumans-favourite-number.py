#User function Template for python3
class Solution:
    def isValid (self,N):
        # code here 
        if (N % 10 ==5 or N % 10 ==0):
            return "YES"
        else:
            return "NO"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
    

        ob = Solution()
        print(ob.isValid(N))
# } Driver Code Ends