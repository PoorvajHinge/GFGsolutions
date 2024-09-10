#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        # pos = [x for x in arr if x>0]
        # negs = [x for x in arr if x<0]
        # arr[:] = pos + negs
        # return arr
        pos = []
        neg = []
        for num in arr:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)
        arr[:] = pos + neg
        return arr
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
