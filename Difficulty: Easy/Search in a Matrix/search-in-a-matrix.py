#User function Template for python3

class Solution:
    
    def searchMatrix(self, matrix, x): 
        for row in matrix:
            for element in row:
                if element == x:
                    return True
        return False

