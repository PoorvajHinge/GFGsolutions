#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a = set(a)
        b = set(b)
        return b.issubset(a)
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends