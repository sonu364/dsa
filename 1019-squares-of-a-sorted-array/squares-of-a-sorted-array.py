class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      sorted_list = []
      for num in nums:
        sorted_list.append(num ** 2)
      sorted_list.sort()
      return sorted_list
        