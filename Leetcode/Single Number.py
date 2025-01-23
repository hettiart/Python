class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0

        for num in nums:

            result ^= num  

        return result
    
    '''

    Here's a detailed breakdown of the XOR operations with the example nums = [2, 2, 1]:

Step 1: result = 0

We start with result initialized to 0.
Step 2: result ^= 2 (result becomes 2)

Binary Representation:
result (0) in binary:  0000
2 in binary: 0010

XOR Operation:
0000 ^ 0010 = 0010

Decimal Conversion: 0010 in binary is equal to 2 in decimal. So, result becomes 2.
Step 3: result ^= 2 (result becomes 0)

Binary Representation:
result (2) in binary:  0010
2 in binary: 0010

XOR Operation:
0010 ^ 0010 = 0000

Decimal Conversion: 0000 in binary is equal to 0 in decimal. So, result becomes 0.
Step 4: result ^= 1 (result becomes 1)

Binary Representation:
result (0) in binary:  0000
1 in binary: 0001

XOR Operation:
0000 ^ 0001 = 0001

Decimal Conversion: 0001 in binary is equal to 1 in decimal. So, result becomes 1.

    '''
