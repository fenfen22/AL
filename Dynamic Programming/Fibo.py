"""
Fibonacci numbers:
Fn = 0, if n = 0;
Fn = 1, if n = 1;
Fn = Fn-1 + Fn-2, otheriwse

"""

"""
This function is recursively call itself, it takes exponential time since there are a lot of recomputations
"""
def Fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib1(n-1) + Fib1(n-2)


"""
Memoized fibonacci numbers: we remember already computed values to avoid recomputations

In the main function, we need define a list F[] to store each value for Fib(n). Then in the function Mem_Fib2, we can just use 
this list to return value or store the value that we calculated.

So if we calculate Fib(5), we first check if F[5] is empty. If it's empty, we recursively call the function Mem_Fib2 to get what 
we want, and store the value in the list. so next time, we don't need to calculate it again.

The time complexit is O(n), n is the largest number you want to calculate.
Space is O(n)
"""
def Mem_Fib2(n,F):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if F[n] == False:
            F[n] = Mem_Fib2(n-1,F) + Mem_Fib2(n-2,F)            # remember the value we calculated in the list F[], so for each value, we only calculate once
        return F[n]                                         # if F[n] is empty, we calculat it, otherwise, we just output the value stored.
    

def Iter_Fib3(n,F):

    """
    we calculate these values from beginning, while we use a list to store all of them.

    Time complexity is O(n), and the space compelxity is O(n)
    """
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
    

def Fib4(n):
    """
    we calculate these values from begining, and only use three parameters to store them, since we only need to remember last two
    computed values. 
    
    In this algorithm, the time complexity is O(n), and the space is O(1) since we only need store 3 values.
    """
    previous = 0
    current = 1
    for i in range(2,n+1):                                   # index of i goes like [2,n]  ---> this line can be changed to range(1,n)
        nextOne = previous + current
        previous = current
        current = nextOne
    return current


if __name__ == '__main__':
    print("result of Fib1:", Fib1(8))                        # this is for Fib1()
    print("result of Fib4:", Fib4(8))                                 # this is for the last function


    """This four lines are for check the Memoized one and the bottom up one, 
    since these two both need a list to store the values that have been calculated before 
    """

    n = 8
    F = [False]* (n+1)
    print("result:", Mem_Fib2(n,F))
    print("result:", Iter_Fib3(8,F))                          # this is the bottom up


    



