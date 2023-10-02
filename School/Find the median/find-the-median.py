#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		if(n%2!=0):
		    return v[n//2]
		else:
		    mid1=v[(n-1)//2]
		    mid2=v[n//2]
		    return (mid1+mid2)//2
		    
		
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends