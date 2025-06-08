#User function Template for python3

class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        l1 = [i for i in arr if i<x]
        return len(l1)