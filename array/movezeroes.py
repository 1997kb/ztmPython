# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:
  def movezero(self,nums):
    non_zero_index_tracker = 0
    for i in range(len(nums)):
      if nums[i] != 0 :
        nums[i],nums[non_zero_index_tracker] = nums[non_zero_index_tracker],nums[i]
        non_zero_index_tracker +=1
    return nums
    
  


solution = Solution()
print(solution.movezero([0,1,0,3,12]))


