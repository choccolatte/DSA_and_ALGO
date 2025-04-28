class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # a list of buckets, each is a list (to handle collissions.)


    def hash_function(self, key):
        #sum only the numerical values of the key, ignoring the non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10 #perform modulo 10 on the sum

    def put(self, key, value):
        #add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # update the existing key
                return
        bucket.append((key, value)) #add new key, value pair if not found

    def get(self, key):
        #retrive a value by key
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None #key not found

    def remove(self, key):
        #remove a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] # remove the key-value pair
                return

    def print_map(self):
        #print all key-value pairs in the hash map
        print("Hash Map Contents: ")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index} : {bucket}")
            
#creating the hash map from the example
hash_map = SimpleHashMap(size = 10)

#adding the entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

#demonstrating retrieval
print("\nName associated with '123-4570': ", hash_map.get("123-4570"))

print("Updating the name for '123-4567' to 'Charizard'")
hash_map.put("123-4567", "Charizard")

#checking if Peter is still there
print("Name associated with '123-4570': ", hash_map.get("123-4570"))

print(hash_map.get("123-4567"))