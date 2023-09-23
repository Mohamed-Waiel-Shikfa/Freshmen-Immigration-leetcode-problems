class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        i=0
        j=0
        while i!=m:
            if matrix[i][j] == target:
                return True
            if j == n-1:
                j=0
                i+=1
            else:
                j+=1
        return False