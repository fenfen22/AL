class PartialSums():
    def __init__(self,array):
        self.A = array[:]
        
    def sumOperation(self, i):
        val = 0
        for j in range(0,i):
            val +=self.A[j]
        return val

    def update(self, i, deta):
        self.A[i-1] = self.A[i-1] + deta
        return self.A[i-1]
    
    def printArray(self):
        print(self.A)

array=[1,2,1,1,0,2,3,1,0,1,3,4,1,1,1,2]
partial_sum = PartialSums(array)
partial_sum.printArray()
print(partial_sum.sumOperation(5))
print(partial_sum.update(4,3))
partial_sum.printArray()