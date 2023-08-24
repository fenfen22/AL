"""
Integer Multiplication

Divide-and-conquer : divide the n-bit integers into two

Let's take two base2 values as an example: 
x = 10001101; y = 11100001
After we divided them into two parts, respectively. We get:
x_h = 1000; x_l = 1101
y_h = 1110; y_l = 0001

x*y = (2^(n/2) * x_h + x_l) * (2^(n/2) * y_h + y_l) 
    = 2^n * x_h * y_h + 2^(n/2) * (x_h * y_l + x_l * y_h) + x_l * y_l

Thus, we only recursively compute 3 products of n/2-bit integers: 
x_h * y_h      ------> represented as z2 in code below
(x_h * y_l + x_l * y_h)          ------> represented as z1 in code below
x_l * y_l               ------> represented as z0 in code below

This code use numbers represented in based 10. For binary representation of integers, it suffices to replace
everywhere 10 by 2.

Time complexity: O(n^(lg3))

"""

# split_at function specifies the number of digits to extract from the right
# for example split_at(12345,3) will extract the 3 final digits, giving high = 12, low = 345
# since we use "int" to convert str to int, we should be very careful about the string! int(" ") would report error!
def split_at(num,position):
    string = str(num)
    high = int(string[:-position])
    low = int(string[-position:])
    return high, low

# calculate the length of this num
def size_base(num):
    return len(str(num))


def karatsuba(num1, num2):
    if(num1 < 10 or num2 < 10):
        return num1 * num2          # fall back to traditional multiplication
    
    m = max(size_base10(num1), size_base10(num2))
    m2 = m // 2   # divide it into two parts

    high1, low1 = split_at(num1, m2)
    high2, low2 = split_at(num2, m2)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return(z2*10**(m2*2) + ((z1-z2-z0)*10**m2)) + z0


if __name__ == '__main__':
    num1 = 234
    num2 = 12345
    print("234 * 12345 = ", karatsuba(num1, num2))
