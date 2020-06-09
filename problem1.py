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

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def print_linked_list(self):
        output_list = []
        current_node = self.head
        while current_node is not None:
            output_list.append(current_node.value)
            current_node = current_node.next
        print(output_list)


class LRU_Cache(object):
    def __init__(self, capacity):
        self.bucket_array = [None for i in range(capacity)]
        self.capacity = capacity
        self.key_list = DoublyLinkedList()
        self.num_entries = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        key = key - 1
        if key > self.num_entries:
            return -1
        elif self.bucket_array[key] is not None:

            temporary = self.key_list.head
            self.key_list.head = self.key_list.head.next
            self.key_list.tail.next = temporary
            self.key_list.tail = self.key_list.tail.next

            return self.bucket_array[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        key = key - 1
        if key >= self.capacity:
            key = key % self.capacity
        if self.bucket_array[key] is None:
            self.bucket_array[key] = value
            self.num_entries += 1
            if self.key_list.head is None:
                self.key_list.head = DoubleNode(key)
                self.key_list.tail = self.key_list.head
            else:
                self.key_list.append(key)
        else:
            if self.num_entries == self.capacity:
                key_to_remove = self.key_list.head.value
                self.bucket_array[key_to_remove] = None
                self.num_entries -= 1
            else:
                print("That key is filled, but others are open. Take a look!")
        print("Fill level is now at {}".format(self.num_entries))


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
print("This is the current bucket array: {}".format(our_cache.bucket_array))
our_cache.key_list.print_linked_list()
our_cache.set(2, 2)
print("This is the current bucket array: {}".format(our_cache.bucket_array))
our_cache.key_list.print_linked_list()
our_cache.set(3, 3)
print("This is the current bucket array: {}".format(our_cache.bucket_array))
our_cache.key_list.print_linked_list()
our_cache.set(4, 4)
print("This is the current bucket array: {}".format(our_cache.bucket_array))
our_cache.key_list.print_linked_list()


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
print(our_cache.bucket_array)
our_cache.set(6, 6)
print(our_cache.bucket_array)

print(our_cache.get(3))   # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
