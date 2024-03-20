#User function Template for python3

class Solution:
    def toLower (self , s : str)-> str :
        # code here 
        return s.lower()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.toLower(s))
# } Driver Code Ends