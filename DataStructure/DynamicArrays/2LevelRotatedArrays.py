import math
from RotatedArray import RotatedArray



class TwoLevelRotatedArray():
    def __init__(self, array):
        self.g_n = 2 ** math.ceil(math.log2(len(array)))
        self.t_n = int(math.sqrt(self.g_n))
        self.Rs = []
        for i in range(self.t_n - 1):
            r = ['-' for j in range(self.t_n)]
            self.Rs.append(RotatedArray(r, self.t_n))
        r = ['-' for j in range(self.t_n)]
        self.Rs.append(RotatedArray(r,self.t_n-(self.g_n-len(array))))

        
        for i in range(len(array)):
            j = int(i / self.t_n)                       # index of Rs
            k = (i+self.Rs[j].offset) % self.t_n        # index of i in Rj
            self.Rs[j][k] = array[i]

    # i is the index from original array
    # compute 2-level rotated array Rj and index k corresponding to i, return Rj[k]
    def TwoLevel_access(self, i):
        j = int(i / self.t_n)                       # index of Rs
        k = (i+self.Rs[j].offset) % self.t_n        # index of i in Rj
        return self.Rs[j][k]


    """
    find Rj and k as in access
    rebuild Rj with new entry inserted
    propagate overflow to R(j+1) recursively
    """
    def TwoLevel_insert(self, i, x):
        j = int(i / self.t_n)                       
        k = i % self.t_n
        flag = self.Rs[j].pop(-1)
        self.Rs[j].insert(k,x)
        j += 1 
        while j < self.t_n:
            if self.Rs[j].n == self.t_n:          # Rj is full now, we need move the last element in Rj to R(j+1)
                pop_val = self.Rs[j].pop(-1)
                self.Rs[j].push(0, flag)
                flag = pop_val
                j += 1
            else:
                self.Rs[j].push(0, flag)
                j += 1
                break
            
    """
    find Rj and k as in Access
    rebuild Rj with entry i deleted
    propagate underflow to R(j+1) recursively
    """
    def TwoLevel_delete(self,i):
        j = int(i / self.t_n)                       
        k = i % self.t_n
        self.Rs[j].delete(k)
        j += 1
        while j<self.t_n:
            flag = self.Rs[j].pop(0)
            self.Rs[j-1].push(-1, flag)
            j += 1

    def print2LevelRoatedArray(self):
        for i in self.Rs:
            print("offset is:", i.offset)
            i.printRotatedArray()
            
        
    



if __name__ == '__main__':


    array = [1,2,1,1,0,2,3,1,0,1,3,4,1,1,1]         #  15 elements
    TwoLevelRA = TwoLevelRotatedArray(array)
    # TwoLevelRA.print2LevelRoatedArray()
    # print(TwoLevelRA.TwoLevel_access(4))
    TwoLevelRA.TwoLevel_insert(6,8)
    # TwoLevelRA.TwoLevel_delete(5)
    TwoLevelRA.print2LevelRoatedArray()
