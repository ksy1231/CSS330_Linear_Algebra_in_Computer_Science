# Author: Soo Yun Kim
# Assignment 2
# Date: October 10, 2018
#
# Problem 1.5.1: With the extension to support
#   " ": 26 == 11010 # space is 26
#   ".": 27 == 11011
#   "!": 28 == 11100
#   ",": 29 == 11101
#   "?": 30 == 11110
#   ":": 31 == 11111

# b1, b2: single binary bits
def GF2_addbit(b1, b2):
    if(len(b1) == 1 and len(b2) == 1):
        if(b1 == b2):
            return '0'
        if(b1 != b2):
            return '1'

# w1, w2: same length, list of bits
# return the GF2_add result of w1 and w2
a = []
c = []
def GF2_addword(w1, w2):
        if(len(w1) == 2 and len(w2) == 2):
                for i in range(len(w1)):
                        a.append(GF2_addbit(w1[i], w2[i]))
                b = ''.join(a)
                return b
            
        if(len(w1) == 3 and len(w2) == 3):
                for i in range(len(w1)):
                        c.append(GF2_addbit(w1[i], w2[i]))
                d = ''.join(c)        
                return d
 
# generates as a list of strings, all binary number of given number of bits
# E.g.,
#   n_bit_list(1): returns ['0', '1']
#   n_bit_list(2): returns ['00', '01', '10', '11']
#   n_bit_list(3): returns ['000', '001', '01', '011', '100', '101', '110', '111']
#   ...
def bin_list(n):    
    if n == 0:
        return['']
    else:
        return ['0' + i for i in bin_list(n - 1)] + ['1' + i for i in bin_list(n - 1)]
    # Note: n_bit_list(n): function is _NOT_ a required function for AS2
    #       just that I found it convenient to have this function
    #       for our test cases of 2, 3, and 5 bits

# Part A: Output all n-bit string addition results
def test_add(bit_list):
    x = bin_list(bit_list)
    if bit_list == 2:
        
        for i in range(len(x)):
            for j in range(len(x)):
                if i <= j:
                    y = GF2_addword(x[i], x[j])
                    a = [y[i:i+2] for i in range(0, len(y), 2)]

        for k in range(len(a)):
                print(a[k])
    if bit_list == 3:
        for i in range(len(x)):
            for j in range(len(x)):
                if i <= j:
                    y = GF2_addword(x[i], x[j])
                    b = [y[i:i+3] for i in range(0, len(y), 3)]
        for k in range(len(b)):
            print(b[k])

test_add(2)
test_add(3)

# try decode
book_codes = ['10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101', '00100', '11001', '11010']
print("Decoding coded message from the book:")
# You shoud call your function to print out all combinations using 5-bit code

# loop here to encode and decode until an empty string is entered
print("Thanks for playing. Bye")

# Now finally, what is the message here?
my_coding_msg = ['10000', '00000', '00000', '010000', '11010', '00000', '01000', '10111', '00110', '11111', '01001', '01000', '11001', '11010', '11111', '10110', '10010', '00011', '01000', '10010', '11001', '10100', '10110', '10011', '00011', '10010', '01000', '10000', '10010', '11111', '01000', '10010', '11001', '00000', '11100', '01000', '10011', '10110', '01000', '10111', '00110', '11111', '01111', '01000', '00001', '10101', '11010', '00000', '01000', '10000', '11001', '10010', '00000', '00000', '01000', '11010', '00000', '01000', '10111', '00110', '11111', '01110', '01000']
print("What am I saying in this message?", my_coding_msg)
