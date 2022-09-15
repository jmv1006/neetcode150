import heapq
from typing import Counter

def leastInterval(tasks, n):
    count = Counter(tasks)
    maxHeap = [-s for s in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    queue = []

    
    while queue or maxHeap:
        time += 1
        current_value = heapq.heappop(maxHeap)

        


        

        



tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
leastInterval(tasks, n)