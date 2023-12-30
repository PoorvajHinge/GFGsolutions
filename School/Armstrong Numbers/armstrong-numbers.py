#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here
        temp = n
        sum = 0
        b = len(str(n))
        while n>0:
            dig = n%10
            sum = sum + dig**b
            n = n //10
        if(sum == temp):
            return "Yes"
        else:
            return "No"
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends