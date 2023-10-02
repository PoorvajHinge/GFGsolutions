#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        mul=1
        for i in arr:
            mul=mul*i
        return mul
            
    


#{ 
 # Driver Code Starts.
    

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()





# } Driver Code Ends