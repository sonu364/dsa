##class Solution:
   ## def longestConsecutive(self, nums: List[int]) -> int:
        ##numSet = set(nums)
       ## longest = 0

    ##    for n in nums:
            # check if its the start of a sequence
  ##          if (n - 1) not in numSet:
       ##         length = 0
##
     ##           while (n + length) in numSet:
   ##                 length += 1

 ##               longest = max(length, longest)
3
        ##return longest ##
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for num in s:

            if num - 1 not in s:      # Start of sequence
                count = 1

                while num + 1 in s:
                    num += 1
                    count += 1

                longest = max(longest, count)

        return longest