#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        back = 1
        ini = 1
        lst = []
        for i in range(n):
            temp = ini
            lst.append(back)
            ini +=back
            back = temp
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends