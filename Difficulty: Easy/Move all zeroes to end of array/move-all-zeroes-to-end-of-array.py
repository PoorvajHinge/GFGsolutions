#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	zero = arr.count(0)
    	new1 = [x for x in arr if x!=0]
    	for i in range(zero):
    	    new1.append(0)
    	arr[:] = new1
    	return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends