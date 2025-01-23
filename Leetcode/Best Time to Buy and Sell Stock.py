class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def get_elements_right_of_min(prices):
            min_value = min(prices)
            min_index = prices.index(min_value)
            right_elements = prices[min_index + 1:] 
            return right_elements, min_value  # Return both right_elements and min_value

        def get_max_from_right_array(right_elements):
            if right_elements:                # If the list right_elements is not empty
                return max(right_elements)
            else:
                return None  

        right_elements, min_value = get_elements_right_of_min(prices)
        max_value = get_max_from_right_array(right_elements)

        if max_value is not None:
            profit = max_value - min_value
            return profit  # Return the profit instead of printing
        else:
            return 0  # Return 0 instead of printing
