class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # list of buckets, each is a list (to handle collisions)

    def hash_function(self, value):
        #simple hash function:sum of character codes modulo the number of buckets
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        #add a value if its not already present
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        #check if a value exists in the set
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        #removes a value
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        #print all elements in the hash set
        print("Hash Set Contents: ")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

#creaating the hash set
hash_set = SimpleHashSet(size=10)

hash_set.add("Charolette")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:", hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))