#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		n1 = S.split()
		n2 = [x[0] for x in n1]
		return ''.join(n2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet(S)

        print(answer)
        print("~")

# } Driver Code Ends