#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        new1 = ''.join([str(x) for x in arr])
        new1 = int(new1) + 1
        new2 = [x for x in str(new1)]
        return new2
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends