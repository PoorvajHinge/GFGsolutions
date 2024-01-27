#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        # swapped = False
        # for i in range(n-1):
        #     for j in range(n-i-1):
        #         if arr[j] > arr[j+1]:
        #             arr[j],arr[j+1] = arr[j+1],arr[j]
        #             swapped = True
        # if swapped == False:
        #     return 1
        # else:
        #     return 0
        new_arr = sorted(arr)
        if new_arr == arr:
            return 1
        else:
            return 0 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends