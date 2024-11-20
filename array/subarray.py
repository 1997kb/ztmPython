# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#kadane's algorithm

class Solution:
    def sub_array(self,input_array):
       max_current = input_array[0]
       max_global = input_array[0]
       for i in range(1,len(input_array)):
           max_current = max(input_array[i],max_current + input_array[i])

           if max_global > max_current:
               max_global = max_current
       return max_global
       
       

          
            



input_array = []
solution = Solution()


