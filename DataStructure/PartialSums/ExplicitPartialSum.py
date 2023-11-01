
class PartialSums():
    def __init__(self,array):
        self.A = array[:]
        self.P = [0]*len(self.A)
        self.P[0] = self.A[0]
        for i in range(1, len(self.P)):
            self.P[i] = self.P[i-1] + self.A[i]


    def sumOperation(self,i):
        return self.P[i-1]

    def update(self, i, deta):
        for j in range(i-1,len(self.P)):
            self.P[j] += deta


array=[1,2,1,1,0,2,3,1,0,1,3,4,1,1,1,2]
partial_sum = PartialSums(array)

print(partial_sum.sumOperation(11))
print(partial_sum.A)
print(partial_sum.P)
partial_sum.update(13,5)
print(partial_sum.A)
print(partial_sum.P)