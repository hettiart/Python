class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        while l <= r:                       # This while loop implements the core logic of binary search. The loop continues as long as the left pointer l is less than or equal to the right pointer r

            mid = (l + r) // 2              # Inside the loop, mid is calculated as the middle index between l and r. The // operator performs integer division, ensuring mid is always an integer

            if target == nums[mid]:         # The code checks if the target value matches the element at the mid index. If they are equal, the function immediately returns mid as the insertion point.
                return mid

            if target > nums[mid]:          # If the target value is greater than the element at the mid index, it means the insertion point must be in the right half of the list
                l = mid+1                   # The left pointer l is updated to mid + 1, effectively excluding the left half of the list from further search
            else:                           # If the target value is less than the element at the mid index, the insertion point must be in the left half of the list.
                r = mid-1                   # The right pointer r is updated to mid - 1, effectively excluding the right half of the list from further search

        return l                            # If the loop completes without finding an exact match for the target value, the function returns l. This is because l will have been adjusted to point to the index where the target value should be inserted to maintain the sorted order.
    


    # this code uses binary search to efficiently determine the correct position to insert a target value into a sorted list nums. It handles cases where the target value already exists in the list or where it needs to be inserted at the beginning or end of the list.
    # https://www.youtube.com/watch?v=K-RYzDZkzCI