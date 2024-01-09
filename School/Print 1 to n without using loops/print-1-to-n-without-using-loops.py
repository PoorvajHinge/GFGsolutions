#User function Template for python3

class Solution:
    def printTillN(self, N):
    	#code here 
    	def prin(N):
    	    if N == 0:
    	        return                  #base case
    	    prin(N-1)
    	    print(N,end=" ")
        prin(N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends