#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        pos = txt.find(pat)
        lst = []
        while(pos >=0):
            lst.append(pos)
            pos = txt.find(pat,pos+1)
        new_list = [x+1 for x in lst]
        return new_list
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends