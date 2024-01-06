#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        arr.sort()
        return arr[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends