#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        count = N 
        for i in range(1,N+1):
            for j in range(count,0,-1):
                print("*",end=" ")
            count = count -1
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends