#User function Template for python3

class Solution:
    def leftElement(self, arr, n):
    # Your code goes here  
            arr.sort()
            start = 0
            end = len(arr)-1
            while start<end:
                start+=1
                end-=1
            return arr[end]
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.leftElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends