class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.lru = None
        

    def get(self, key):
        if not self.head: return -1
        curr = self.head

        while curr is not None:
            if curr.key == key: return curr.val
            else: curr = curr.next
        
        return -1
        

    def put(self, key, value):
        if not self.head: 
            self.head = Node(key, value)
            self.lru = self.head
        else:
            prev = None
            curr = self.head
            count = 0
            
            while curr:
                count += 1
                if not curr.next:
                    curr.next = Node(key, value)
                    return
                else:
                    prev = curr
                    curr = curr.next
                

        

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2, 2)