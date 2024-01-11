#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        new_list = [int(x) for x in str(N) if int(x)!=0 and N %int(x)==0]
        return len(new_list)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends