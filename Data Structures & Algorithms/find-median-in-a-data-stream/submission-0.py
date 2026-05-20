class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:

        self.array.append(num)

    def findMedian(self) -> float:

        self.array.sort()

        l = len(self.array)

        if l % 2 == 0:
            num1 = (l//2) -1 
            num2 = (l//2)

            median = (self.array[num1] + self.array[num2])/2
        else:
            median = l // 2
            median = self.array[median]

        return median
        