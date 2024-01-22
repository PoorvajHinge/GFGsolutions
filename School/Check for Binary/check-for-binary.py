# Return true if str is binary, else false
def isBinary(str):
    #code here
    flag = False
    for i in str:
        if i=="1" or i =="0":
            flag = True
        else:
            flag = False
            return 0
            
    if flag ==True:
        return 1
    else:
        return 0


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends