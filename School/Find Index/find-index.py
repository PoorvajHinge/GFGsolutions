#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        lst=[]
        for i in range(0,len(a)):
            if key == a[i]:
                lst.append(i)
        if not lst:
            start_index = stop_index = -1
        elif len(lst) <2:
            start_index = lst[0]
            stop_index = start_index 
        else:
            start_index = lst[0]
            stop_index = lst[len(lst)-1]
        return start_index,stop_index
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends