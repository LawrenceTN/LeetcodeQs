# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next= None
        
class LRUCache:
    def __init__(self, n):
        self.length = n
        self.cache = {} # hashmap for our cache to map keys to specific values (holds our nodes)
        
        # construct 2 nodes initially as reference/pointers
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

        # left side if the least recent
        # right side is the most recent

    def insert(self, node): # inserting a node at right position for most recently used, using self.right as reference for MRU. make sure to fill in missing links
        prev = self.right.prev
        nex = self.right

        prev.next = node
        nex.prev = node

        node.next = nex
        node.prev = prev

    def remove(self, node): # removing a node from the LL, make sure to re-connect prev and next nodes
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev


    def set(self, key, value):
        if key in self.cache: # if node exists in the list with same key/value, remove Node 
            self.remove(self.cache[key])
        # if not: create a new node and set to MRU
        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key])

        # check length of list exceeds capacity
        # if so, remove LRU (left) from cache/HM
        if len(self.cache) > self.length:
            lru = self.left.next # this will be the LRU, bc left = 0 as a reference (left mode Node)
            self.remove(lru) # remove/delete
            del self.cache[lru.key]

    
    def get(self, key):
        if key in self.cache:
            # when you get a value, delete it from its current position, and then update it to the most recent (right)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # get the Node at specific key if in cache
        return None