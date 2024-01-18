#User function Template for python3

class Solution:
    def noOfDigits(self, N):
        # code here
        if N==0:
            return 0
        elif N ==1:
            return 1
        a,b = 0,1
        for i in range(2,N+1):
            a,b = b,(a+b)
            
        lst = [x for x in str(b)]
        return len(lst)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.noOfDigits(N))
# } Driver Code Ends