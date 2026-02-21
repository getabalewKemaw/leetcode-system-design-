      
class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [None] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                # The core logic: Sum the two elements directly above
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)

        return triangle
