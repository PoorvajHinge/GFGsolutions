#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		if N == 0 or N ==1:
		    return N
		unique = 1
		for i in range(1,N):
		    if A[i] !=A[i-1]:
		        A[unique] = A[i]
		        unique+=1
		return unique


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends