#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		ls1=[]
		for i in range(n):
		    if arr[i] ==i+1:
		        ls1.append(arr[i])
        return ls1
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends