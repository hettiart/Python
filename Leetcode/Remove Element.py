class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0                                   # setting pointer to initial element on zero position
        for r in range(len(nums)):              # for each element in the length of array
            if nums[r] != val:                  # if each element is not equal to val integer
                nums[l] = nums[r]               # add that not equal r value to l pointer position
                l += 1                          # then move the l pointer from current position to the next position
        return l                                # return the last position of l