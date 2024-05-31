#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        A = set(A)
        B = set(B)
        final = sorted(A.symmetric_difference(B))
        return ''.join(final) if final else -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends