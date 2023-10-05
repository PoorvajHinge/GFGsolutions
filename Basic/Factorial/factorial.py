#User function Template for python3


class Solution:
    def factorial (self, N):
        # code here
        def fact(N):
            if N==0:
                return 1
            else:
                return N * fact(N-1)
                
        return fact(N)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends