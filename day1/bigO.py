# this is O(n) linear time

nemo = ["nemo","dori","carl","thomas"]
worst_case=["dori","carl","thomas","nemo"]
best_case = ["nemo","dori","carl","thomas"]

#<--------------------------------------end------------------------------------>


def findNemo(array):
    for i in (array):
     if i == "nemo":
        print("found nemo")

print(findNemo(nemo))

#<--------------------------------------end------------------------------------>



#this is constant time O(1)

def findonce(array):
   print(array[0])

#<--------------------------------------end------------------------------------>


#considering worst case scenario always assume linear relationship
#use break statement to skip unnecessary computation
'''
for both case be it best case or worst case always consider O(n)
'''


def functionFindNemo(inp):
   for i in worst_case:
      if i == "nemo":
         print("Found Nemo")
   for i in best_case:
      if i == "nemo":
         print("found nemo")

#<--------------------------------------end------------------------------------>

#removing constants and insignificant values 
'''
O(n/2 + 100) can be considered as O(n)

'''


def compressbox(boxes):
   for i in boxes:
      print(i)
   for j in boxes:
      print(j)

# in  this example O(2n) can be considered O(n) 



#<--------------------------------------end------------------------------------>












