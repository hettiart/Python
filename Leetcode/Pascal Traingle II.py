class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1]                               # This line initializes a list named res with the value [1].  This represents the first row of Pascal's Triangle, which is always just [1].

        for i in range(rowIndex):               #  This line starts a loop that iterates rowIndex times, where i represents the current row number (starting from 0). The loop will run until it reaches the specified rowIndex, building up the rows of the triangle.
            next_row = [0] * (len(res) + 1)     # This line creates a new list called next_row, which will store the elements of the next row of the triangle. It's initialized with a length one greater than the current row (res) and filled with zeros.
            for j in range(len(res)):           # This line starts an inner loop that iterates through the elements of the current row (res), where j represents the index of the element in the current row.
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row                      # This line updates the res list to be equal to the next_row list. This effectively moves to the next row in the triangle.
        return res                              # This line returns the res list, which now contains the elements of the specified row in Pascal's Triangle.