class Solution:
    def missingNum(self, arr):
        # code here
        return sum(i for i in range(len(arr)+2)) - sum(arr)