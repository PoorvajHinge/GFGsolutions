from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	counter = Counter(arr)
    	dups = [item for item, count in counter.items() if count>1]
    	return sorted(dups) if dups else [-1]


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends