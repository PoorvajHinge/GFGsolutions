#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def immediateSmaller(self,arr):
		# code here
		res =[]
		for i in range(len(arr)-1):
		    if arr[i]> arr[i+1]:
		        res.append(arr[i+1])
		    else:
		        res.append(-1)
		res.append(-1)
		return res

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.immediateSmaller(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends