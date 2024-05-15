#User function Template for python3

class Solution:
    def find_multiplication (self, arr, brr, n, m) : 
        #Complete the function
        max1 = max(arr)
        min1 = min(brr)
        return max1*min1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.find_multiplication(arr, brr, n, m)
    print(res)






# } Driver Code Ends