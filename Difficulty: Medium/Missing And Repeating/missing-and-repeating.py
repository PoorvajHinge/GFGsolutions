#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        # code here
        count1 = Counter(arr)
        newl = [x for x , count in count1.items() if count>1]
        #2nd proceesssssszz
        
        new1 = (set(range(1,len(arr)+1)))
        new2 = set(arr)
        x = list(new1.symmetric_difference(new2))
        
        return newl[0],x[0]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends