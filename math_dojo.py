class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
        
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
