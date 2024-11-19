class Solution:
    def reverse(self,input_string):
        return input_string[-1:-(len(input_string)+1):-1]


input_string = 'Hi My name is Andrei'
soln = Solution()
print(soln.reverse(input_string))