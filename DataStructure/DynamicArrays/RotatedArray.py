import random


class RotatedArray():
    
    def __init__(self, array, n):
        self.n = n                                                                  # the number of values in array, except '-', which represents empty position
        self.offset = random.randint(0,len(array)-1)                                   # randomly select a offset position, offset is to mark start of the array
        # self.offset = 10
        self.rotatedArray = ['-' for i in range(len(array))]                        # initial the rotated array
        for i in range(len(array)):
            self.rotatedArray[(self.offset + i)% len(array)] = array[i]             # construct the rotated array based on the given array and offset generated
    
    def __setitem__(self, index, value):                                            # RotatedArray' object support item assignment
        self.rotatedArray[index] = value
    
    def __getitem__(self, index):
        return self.rotatedArray[index]                                             # allows you to access elements based on index
        

    # given position i(start with 0), return A[i] based on rotated array
    # query the value stored in position i of original array
    def access(self, i):
        position = (self.offset + i)% len(self.rotatedArray)
        return self.rotatedArray[position]

    # if we insert element in endpoint, we could just shift the offset
    def insert(self, i, x):
        if self.n>=len(self.rotatedArray):
            raise ValueError("can't add element into a full array")

        start = self.offset                                         # points to the begaining value
        end = ((self.offset+self.n)-1)%len(self.rotatedArray)       # points to the ending value
        
        if i == 0:
            self.offset =(self.offset-1 + len(self.rotatedArray)) % len(self.rotatedArray)
            self.rotatedArray[self.offset] = x
        elif i == end+1:
            end = (end + 1)%len(self.rotatedArray)
            self.rotatedArray[end] = x
        else:
            v = (i + self.offset) % len(self.rotatedArray)
            if abs(v-start)< abs(v-end):
                self.offset =(self.offset-1 + len(self.rotatedArray)) % len(self.rotatedArray)
                for j in range(self.offset, v):
                    self.rotatedArray[j] = self.rotatedArray[j+1]
                self.rotatedArray[v] = x
            else:
                for i in range(end+1, v, -1):
                    self.rotatedArray[j] = self.rotatedArray[j-1]
                self.rotatedArray[v] = x
        self.n += 1

    
    def pop(self, x):
        if self.n<=0:
            raise ValueError("can't pop element from a empty array")
        if x == 0:
            res = self.rotatedArray[self.offset]
            self.delete(self.offset)
        elif x == -1:
            end = ((self.offset+self.n)-1) % len(self.rotatedArray)
            res = self.rotatedArray[end] 
            self.delete(self.n-1)
        return res
    
    
    def push(self, x,val):
        if self.n>=len(self.rotatedArray):
            raise ValueError("can't push a element into a full array")
        position = 0
        if x == -1:                                                             # push a value at the end
            end =  ((self.offset+self.n)-1)%len(self.rotatedArray)
            position = end + 1
        elif x == 0:                                                            # push a value at begaining
            position = 0
        self.insert(position,val)
        
    def delete(self,i):
        if self.n<=0:
            raise ValueError("can't remove element from a empty array")

        start = self.offset                                         # points to the begaining value
        end = ((self.offset+self.n)-1) % len(self.rotatedArray)       # points to the ending value
        
        if i == 0:
            self.rotatedArray[self.offset] = '-'
            self.offset += 1
        elif i == self.n-1:
            self.rotatedArray[end] = '-'
            end = (end - 1) % len(self.rotatedArray)
        else:
            v = (i + self.offset) % len(self.rotatedArray)
            if abs(v-start)< abs(v-end):
            # if (i+self.offset) % len(self.rotatedArray) > start:
                for j in range(v, self.offset, -1):
                    self.rotatedArray[j] = self.rotatedArray[j-1]
                self.rotatedArray[self.offset] = '-'
                self.offset = (self.offset + 1) % len(self.rotatedArray)
                start = (start + 1) % len(self.rotatedArray)
            else:
                for j in range(v, end):
                    self.rotatedArray[j] = self.rotatedArray[j+1]
                self.rotatedArray[end] = '-'
                end = (end - 1) % len(self.rotatedArray)
        self.n -= 1
    
    def printRotatedArray(self):
        print(self.rotatedArray)



if __name__ == '__main__':

    array = [1,2,1,1,0,2,3,1,0,1,3,4,1,'-','-']         # '-' means empty position
    rotated_array = RotatedArray(array,13)                 # initial a rotated array
    print("offset is : ", rotated_array.offset)
    print(rotated_array.rotatedArray)
# print(rotated_array.access(1))                      # for ouput array[1] in this example
    rotated_array.insert(1,200)                            # insert a value at begaining
    # rotated_array.insert(0,20)  
    rotated_array.delete(0)                               # delete at begaining
# rotated_array.insert(13,100)                          # insert a value at ending (the position will be changed every time)
# rotated_array.insert(rotated_array.n,200) 
    # rotated_array.delete(rotated_array.n-1)                              # delete at the end

# rotated_array.insert(4,22)
# rotated_array.delete(4)
    rotated_array.delete(5)                                 # every time, we delete a value, the index changed!!!
# print(rotated_array.rotatedArray)
# rotated_array.insert(7,88)
    # print(rotated_array.rotatedArray)
    # rotated_array.push(55)
    # b = rotated_array.pop()
    # print(b)
    print(rotated_array.rotatedArray)

