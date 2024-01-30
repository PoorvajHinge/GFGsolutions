#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min_i = i
            for j in range(i+1,n):
                if arr[j] < arr[min_i]:
                    min_i = j
            arr[i],arr[min_i] = arr[min_i],arr[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends