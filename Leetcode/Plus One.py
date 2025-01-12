class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1 # No carry needed
                return digits
            else:
                digits[i] = 0  # Set current digit to 0 and carry over to the next digit
        
        # If the loop completes, it means all digits were 9 (e.g., [9, 9, 9])
        # Add a leading 1 to handle the carry
        return [1] + digits