# Function should return an integer value
def convertFive(n):
    # Code here
    n = str(n)
    x = n.replace('0','5')
    return x


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends