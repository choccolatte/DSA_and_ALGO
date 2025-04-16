class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] # a list of buckets, each is a list (to handle collisions)

    def hash_function(self, value):
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
        #remove a value
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        #prints all elements in the hash set
        print('Hash Set Contains: ')
        for index, bucket in enumerate(self.buckets):
            print(f'Bucket {index}: {bucket}')