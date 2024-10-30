strings = ['a','b','c','d']

print(strings[0]) #look up operation O(1) operation
strings.append('e') #push element O(1) operation
strings.pop() #remove O(1) no loop involved ...we only removed last item
strings.insert(0,'x')#insert operation in the beginning is O(n) as it shifts the indices
strings.insert(2,'y')#O(n)
