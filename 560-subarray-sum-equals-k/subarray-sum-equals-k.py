class Solution:
    def subarraySum(self, nums, k):
        my_dict = {0: 1}   # prefix sum : how many times it appeared

        total = 0
        answer = 0

        for num in nums:
            total += num

            if total - k in my_dict:
                answer += my_dict[total - k]

            if total in my_dict:
                my_dict[total] += 1
            else:
                my_dict[total] = 1

        return answer
 ##class Solution:
   ## def subarraySum(self, nums, k):
     ##   count = 0
       ## n = len(nums)

        ##for i in range(n):
          #  for j in range(i, n):
             ##   if sum(nums[i:j + 1]) == k:
                   ## count += 1

        #return count##