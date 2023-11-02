
class FenwickTree():
    def __init__(self,array):
        self.F = array[:]

        # this part is to contruct the fenwick tree
        k = 1
        while(pow(2,k-1)<= len(self.F)):
            for i in range(pow(2,k-1), len(self.F)):
                if i%pow(2,k) ==0:
                    self.F[i] += self.F[i-(pow(2,k-1))]
            k += 1
    
    # input a is a integer, base is 10, 
    # the output is the integer corresponding to the rightmost 1-bit in a
    # if a is 14, output is 2
    def rmb(self, a):                       # to get the right most bit
        return a&(~a+1)


    # no output, but you can see the changes from self.F
    def update(self, i, deta):
        array=[]                            # array is for storing the index(start with 1) that we need to modify
        array.append(i)
        a = i
        while a<len(self.F)-1:              # since we add one extra value at position 0
            b = a + self.rmb(a)
            array.append(b)
            a = b
        for i in array:                     # update the fenwick tree based on the indexes in array
            self.F[i] += deta
        
    
    # i is the integer, base 10
    def sumOperation(self, i):
        array=[]                            # for storing indexs that we need to add together
        array.append(i)
        a = i
        while a != 0:
            b = a - self.rmb(a)
            array.append(b)
            a = b
        val = 0
        for i in array:                     # get the sum based on the array
            val += self.F[i]
        return val

    def printArray(self):
        print(self.F)




array=[0,1,2,1,1,0,2,3,1,0,1,3,4,1,1,1,2]
FT = FenwickTree(array)                         # initial Fenwick Tree with a given array
FT.printArray()                                 # print the Fenwick Tree based on a given array
print(FT.sumOperation(14))                      # sum operation, output is the sum (array[1] to array[14])
FT.update(9,2)                                  # update operation, by print self.F, we could see the changes
FT.printArray()
