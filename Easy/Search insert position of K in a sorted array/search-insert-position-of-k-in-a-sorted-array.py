#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        low , high = 0,N-1
        while low<=high:
            mid = (low + high) //2
            if Arr[mid] == k:
                return mid
            elif(Arr[mid]<k):
                low = mid + 1
            else:
                high = mid -1
        return low

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends