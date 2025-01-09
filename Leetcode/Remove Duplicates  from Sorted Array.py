class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        l = 1
        for r in range(1, len(nums)): # go through the elements in the sorted array one by one
            if nums[r] != nums[r-1]:  # if current element in the array is not equal to previous element 
                nums[l] = nums[r]     # move current element(r) to last pointer(l)
                l += 1                # now increment pointer number by one move to next available position in array
        return l                      # return the pointer where it ended last 
    

# https://www.youtube.com/watch?v=DEJAZBq0FDA