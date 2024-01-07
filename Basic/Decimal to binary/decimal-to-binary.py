#User function Template for python3
def toBinary(n):
    bin_num = bin(n)[2:]
    print(bin_num)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    for _ in range(int(input())):
        n=int(input())
        toBinary(n)

    
# } Driver Code Ends