class Solution:
    def two_sum(self,input_array,target_sum):
       left_pointer,right_pointer = 0,len(input_array)-1
       while left_pointer < right_pointer:
          if(input_array[left_pointer]+input_array[right_pointer]<target):
             left_pointer+=1
          elif(input_array[left_pointer]+input_array[right_pointer]>target):
             right_pointer-=1
          else:
            return [left_pointer,right_pointer]

           

nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.two_sum(nums,target))