#User function Template for python3

class Solution:
    def findMax(self, N):
        # code herenew1 
        new1 = [x for x in N]
        new1.sort(reverse =True)
        new2 = new1
        x = ''.join(new2)
        return int(x)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=input()
        
        ob = Solution()
        print(ob.findMax(N))
# } Driver Code Ends