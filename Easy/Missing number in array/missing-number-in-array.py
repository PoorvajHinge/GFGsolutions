#User function Template for python3



class Solution:
    def missingNumber(self,array,n):
        # code here
        # sum_ser=(n*(n+1))//2
        # sum_arr=0
        # for i in array:
        #     sum_arr+=i
        # return sum_ser - sum_arr
        
        #sol2:
        n=len(array)+1
        return ((n*(n+1)//2)-sum(array))
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends