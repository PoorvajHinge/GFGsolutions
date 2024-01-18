#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        def loops(n):
            if n == 0:
                return 1
            else:
                print(n,end=" ")
                return n - loops(n-1)
                
        loops(n)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends