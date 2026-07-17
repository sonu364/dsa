class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        
        # Loop until the two pointers meet
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            # Compare and add the LARGER square to the back of our result list
            if left_square > right_square:
                result.append(left_square)
                left += 1
            else:
                result.append(right_square)
                right -= 1
                
        # Since we collected them from largest to smallest, reverse it at the end!
        return result[::-1]