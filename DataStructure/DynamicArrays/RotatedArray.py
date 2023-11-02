import random


class RotatedArray():
    def __init__(self, array, n):
        self.n = n                                                                  # the number of values in array, except '-', which represents empty position
        # offset = random.randint(0,len(array)-1)                                   # randomly select a offset position, offset is to mark start of the array
        self.offset = 10
        self.rotatedArray = ['-' for i in range(len(array))]                        # initial the rotated array
        for i in range(len(array)):
            self.rotatedArray[(self.offset + i)% len(array)] = array[i]             # construct the rotated array based on the given array and offset generated
        

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
            self.offset -= 1
            self.rotatedArray[self.offset] = x
        elif i == self.n:
            end = (end + 1)%len(self.rotatedArray)
            self.rotatedArray[end] = x
        else:
            if (i+self.offset)%len(self.rotatedArray) > start:
                self.offset -= 1
                self.rotatedArray[self.offset] = self.rotatedArray[start]
                start -= 1
                for j in range(start, i+self.offset):
                    self.rotatedArray[j] = self.rotatedArray[j+1]
                self.rotatedArray[i+self.offset] = x
                
            elif (i+self.offset)%len(self.rotatedArray) < end:
                for j in range(end,(i+self.offset) % len(self.rotatedArray),-1):
                    self.rotatedArray[j+1] = self.rotatedArray[j]
                self.rotatedArray[(i+self.offset) % len(self.rotatedArray)] = x
        self.n += 1

    

    def delete(self,i):
        if self.n<=0:
            raise ValueError("can't remove element from a empty array")

        start = self.offset                                         # points to the begaining value
        end = ((self.offset+self.n)-1) % len(self.rotatedArray)       # points to the ending value
        
        if i == 0:
            self.rotatedArray[self.offset] = '-'
            self.offset += 1
        elif i == self.n:
            self.rotatedArray[end] = '-'
            end = (end - 1) % len(self.rotatedArray)
        else:
            if (i+self.offset) % len(self.rotatedArray) > start:
                for j in range((i+self.offset), self.offset, -1):
                    self.rotatedArray[j] = self.rotatedArray[j-1]
                self.rotatedArray[self.offset] = '-'
                self.offset = (self.offset + 1) % len(self.rotatedArray)
                start = (start + 1) % len(self.rotatedArray)
                
            elif (i+self.offset) % len(self.rotatedArray) < end:
                for j in range((i+self.offset) % len(self.rotatedArray),end):
                    self.rotatedArray[j] = self.rotatedArray[j+1]
                self.rotatedArray[end] = '-'
                end = (end - 1) % len(self.rotatedArray)
        self.n -= 1

array = [1,2,1,1,0,2,3,1,0,1,3,4,1,'-','-']         # '-' means empty position
rotated_array = RotatedArray(array,13)                 # initial a rotated array
print(rotated_array.rotatedArray)
# print(rotated_array.access(1))                      # for ouput array[1] in this example
# rotated_array.insert(0,10)                            # insert a value at begaining
# rotated_array.insert(0,20)  
rotated_array.delete(0)                               # delete at begaining
# rotated_array.insert(13,100)                          # insert a value at ending (the position will be changed every time)
# rotated_array.insert(rotated_array.n,200) 
# rotated_array.delete(13)                              # delete at the end

# rotated_array.insert(4,22)
# rotated_array.delete(4)
rotated_array.delete(5)                                 # every time, we delete a value, the index changed!!!
# print(rotated_array.rotatedArray)
# rotated_array.insert(7,88)
print(rotated_array.rotatedArray)

