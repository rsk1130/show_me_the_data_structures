"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache.
If the cache is full and we want to add a new entry to the cache,
we use some criteria to remove an element.
After removing an element, we use the put() operation to insert the new element.
The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry
when the cache memory reaches its limit.
For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element.
If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""


class LRU_Cache(object):
    def __init__(self, capacity):
        self.contents = [None for i in range(capacity)]
        self.size = len(self.contents)
        self.last_in = None
        self.last_in_index = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        key = key - 1
        if key > self.size:
            return -1
        elif self.contents[key] is not None:
            return self.contents[key]
        else:
            return -1

    def set(self, key, value):
        key = key - 1
        if key >= self.size:
            key = key % self.size
        print(key)
        if self.contents[key] is None:
            self.contents[key] = value
            self.last_in = value
            self.last_in_index = key
        else:
            self.contents[self.last_in_index] = value
            self.last_in = value
            self.last_in_index = key


our_cache = LRU_Cache(5)

our_cache.set(3, 3);
print(our_cache.contents)
our_cache.set(4, 4);
print(our_cache.contents)
our_cache.set(1, 1);
print(our_cache.contents)
our_cache.set(2, 2);
print(our_cache.contents)



print(our_cache.get(1))      # returns 1
print(our_cache.get(2))    # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache


our_cache.set(6, 6)
print(our_cache.contents)

print(our_cache.get(3))
