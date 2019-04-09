# Author: 
# Assignment 2: Empty template
# Date: 
#
# Problem 1.5.1: With the extension to support
#   " ": 26  == 11010 #space is 26
#   ".": 27  == 11011
#   "!": 28  == 11100
#   ",": 29  == 11101
#   "?": 30  == 11110
#   ":": 31  == 11111

# b1, b2: single binary bits
def GF2_addbit(b1, b2):
    return "nothing"


# w1, w2: same length, list of bits
# returns the GF2_add result of w1 and w2
def GF2_addword(w1, w2):
    return "nothing"

# generates as a list of strings, all binrary number of given number of bits
# E.g.,
#   n_bit_list(1): returns ['0', '1']
#   n_bit_list(2): returns ['00', '01', '10', '11']
#   n_bit_list(3): returns ['000', '001', '010', '011', '100', '101', '110', '111']
#   ...
def n_bit_list(n):
    return "not implemented"
    # Note: n_bit_list(n): function is _NOT_ a required function for AS2
    #       just that I found it convenient to have this function
    #       for our test cases of 2, 3, and 5 bits

    
# Part A: Output all n-bit string addition results
def test_add(bit_list):
    print("GF2_WordAdd Test not implemented")

# try decode
book_codes = ['10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101', '00100', '11001', '11010']
print("Decoding coded message from the book:")
# You should call your function to print out all combinations using 5-bit code

# loop here to encode and decode until an empty string is entered      
print("Thanks for playing. Bye")

# Now finally, what is the message here?
my_coded_msg = ['10000', '00000', '00000', '01000', '11010', '00000', '01000', '10111', '00110', '11111', '01001', '01000', '11001', '11010', '11111', '10110', '10010', '00011', '01000', '10010', '11001', '10100', '10110', '10011', '00011', '10010', '01000', '10000', '10010', '11111', '01000', '10010', '11001', '00000', '11100', '01000', '10011', '10110', '01000', '10111', '00110', '11111', '01111', '01000', '00001', '10101', '11010', '00000', '01000', '10000', '11001', '10010', '00000', '00000', '01000', '11010', '00000', '01000', '10111', '00110', '11111', '01110', '01000']
print("What am I saying in this message?", my_coded_msg)

