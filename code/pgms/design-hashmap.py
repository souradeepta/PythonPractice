class Bucket:
    
    def __init__(self):
        self.bucket = []
        
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
            
        return -1
    
    def update(self, key, value):
        found = False

        for i, value in enumerate(self.bucket):
            if value[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break
                
        if found == False:
            self.bucket.append((key, value))
            
    def remove(self, key):
        for i, value in enumerate(self.bucket):
            if value[0] == key:
                del self.bucket[i]
                
    def print(self):
        print(self.bucket)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record_count = 2069
        self.map = [Bucket() for i in range(self.record_count)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.record_count
        self.map[hash_key].update(key, value)
    

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.record_count
        self.map[hash_key].get(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.record_count
        self.map[hash_key].remove(key)
        
    def print(self):
        for value in self.map:
            if value is not None:
                value.print()
        
        
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
param_2 = obj.get(1)
obj.remove(1)
