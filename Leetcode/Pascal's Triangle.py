class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]                                  #  This line initializes a list named res to hold the rows of Pascal's Triangle. It starts with the first row, which is simply [1].

        for i in range(numRows - 1):                 #  This line starts a loop that iterates numRows - 1 times, where i represents the current row number (starting from 0). This loop is responsible for generating the remaining rows of the triangle.

            temp = [0] + res[-1] + [0]               #  temp = [0] + res[-1] + [0]: This line creates a temporary list called temp. It takes the last row in res (res[-1]) and adds a 0 at the beginning and end. This padding with zeros is crucial for the calculation of the next row.
            row = []                                 #  This line initializes an empty list called row, which will store the elements of the current row.

            for j in range(len(res[-1]) + 1):        #  This line starts an inner loop that iterates over the elements in the temp list. j represents the index of the element in temp. The loop runs for one extra iteration compared to the length of the previous row because of the padding zeros.
                row.append(temp[j] + temp[j + 1])    #  This line calculates the value of the current element in row by summing the corresponding element and its adjacent element in the temp list. This essentially combines the values from the previous row to generate the new row, following the principle of Pascal's Triangle.
            res.append(row)                          #  This line appends the newly calculated row (row) to the res list.

        return res                                   #  This line returns the res list, which now contains all the rows of Pascal's Triangle up to numRows.
    


    # https://www.youtube.com/watch?v=nPVEaB3AjUM