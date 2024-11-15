strings = ['a','b','c','d']

# print(strings[0]) #look up operation O(1) operation
strings.append('e') #push element O(1) operation
strings.pop() #remove O(1) no loop involved ...we only removed last item
strings.insert(0,'x')#insert operation in the beginning is O(n) as it shifts the indices
strings.insert(2,'y')#O(n)



#<-------------------------------END------------------------------->



class Solution:
    def __init__(self):
        self.data = {}
        self.length = 0
    
    def get(self,index):
       return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length +=1

    def pop(self):
        del self.data[self.length-1]
        self.length -=1
        return self.data

    def shiftIndex(self,index):
        for i in range(index,self.length-1):
           self.data[i] = self.data[i+1]
        

    def delete(self,index):
       
        self.shiftIndex(index)
        del self.data[self.length-1]
        return self.data
    
    
        




newArr = Solution()
newArr.push("Hello")
newArr.push("how")
newArr.push("are")
newArr.push("you")
print(newArr.delete(2))


