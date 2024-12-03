class HashTable:
    def __init__(self):
        self.size = 20
        self.data = [ [] for i in range(self.size) ]

    def __str__(self):
        return str(self.__dict__)
    
        
    def hash(self,key):
        return len(key) % self.size

    def set(self,key,value):
        hash_value = self.hash(key)
       
        current_reference = self.data[hash_value]
        for i in range(len(current_reference)):
            if current_reference[i][0] == key:
                current_reference[i][1] = value
                return None
        current_reference.append([key,value])
       
        return None
    def get(self,key):
        hash_value = self.hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return None
    
    def remove(self,key):
        hash_value = self.hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None
    
    def get_keys(self):
        keys_list = []
        for i in range(len(self.data)):
             if self.data[i]:
                 if len(self.data[i]) > 1:
                      for j in range(len(self.data[i])):
                          keys_list.append(self.data[i][j][0])
                 keys_list.append(self.data[i][0][0])
                          
                     
                
                     
        print(keys_list)
      
          
        
               
               
       

solution = HashTable()
solution.set("grapessss",1000)
solution.set("grapes",50)
solution.set("apples",100000)
solution.set("appl",2000)
solution.set("banana",3000)
solution.get_keys()



