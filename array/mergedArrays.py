class Solution:
    def mergeArray(self,input_array_1,input_array_2):
        merged_array = []
        i,j = 0,0
        while i < len(input_array_1) and j < len(input_array_2):
            if input_array_1[i] < input_array_2[j]:
                merged_array.append(input_array_1[i])
                i+=1
            else:
                merged_array.append(input_array_2[j])
                j+=1
        #if any remaining elements remain un merged and the input arrays are already sorted
        while i < len(input_array_1):
            merged_array.append(input_array_1[i])
            i+=1
        while j < len(input_array_2):
            merged_array.append(input_array_2[j])
            j+=1
        
        return merged_array
        
        





input_array_1 = [1,2,3,4]
input_array_2 = [2,5,6]
solution = Solution()
print(solution.mergeArray(input_array_1,input_array_2))
