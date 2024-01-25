#User function Template for python3

class Solution:
    def transform(self, s):
        # code here
        words = s.split(' ')
        words1 = [word.capitalize() for word in words]
        return (' '.join(words1))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends