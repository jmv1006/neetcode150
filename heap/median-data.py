import heapq

class MedianFinder:
    def __init__(self):
        self.arr = []

        

    def addNum(self, num):
        self.arr.append(num)
        heapq.heapify(self.arr)
        

    def findMedian(self):
        length = len(self.arr) % 2
        print(self.arr)

        if length == 0:
            ##even number
            copy = self.arr
            list_length = len(self.arr) // 2

            while len(copy) > list_length:
                heapq.heappop(copy)
            
            print(copy)
            num1, num2 = copy[0], copy[1]

            median = (num1 + num2) / 2
          
        else:
            pass
 

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(6)
obj.addNum(5)
obj.addNum(4)
obj.addNum(3)
obj.addNum(2)
obj.addNum(1)
obj.findMedian()

nums = [1,2,3,7,4,6]
heapq.heappop(nums)
heapq.heappop(nums)
heapq.heappop(nums)

# param_2 = obj.findMedian()