class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        
        while left <= right:
            lr = nums[left] ** 2
            rl = nums[right] ** 2

            if lr > rl:
                result.append(lr)
                left += 1
            else:
                result.append(rl)
                right -= 1
                
        return result[::-1]