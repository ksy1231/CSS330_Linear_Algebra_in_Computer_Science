# Author: Kelvin Sung
# Assignment 2: Solution
# Date: Sep 16, 2018
#
# Problem 1.5.1: With the extension to support
#   " ": 26  == 11010 #space is 26
#   ".": 27  == 11011
#   "!": 28  == 11100
#   ",": 29  == 11101
#   "?": 30  == 11110
#   ":": 31  == 11111

# b1, b2: single binary bits
def GF2_addbit(b1, b2): return '0' if b1 == b2 else '1'


# w1, w2: same length, string of bits
# returns the GF2_add result of w1 and w2, a bit string
def GF2_addword(w1, w2):
    r = ''
    for (b1, b2) in zip(w1, w2):
        r = r + GF2_addbit(b1, b2)
    return r

# alternative implementaiton of addword ...
def GF2_addword(w1, w2):
    r = ''
    for i in range(len(w1)):
        r += GF2_addbit(w1[i], w2[i])
    return r

# generates as a list of strings, all binrary number of given number of bits
def n_bit_list(n):
    if n == 1:
        return ['0', '1']
    else:
        l = n_bit_list(n-1)
        r = list()
        for b in l:
            r += [b+'0', b+'1']
        return r

####################################
# alternative-1 using loop iteration
def itob(num, digit):     # integer number to binary string
    b = ''
    lead_zero = digit
    while num > 0:
        b = str(num%2) + b  # modulo 
        num = num // 2      # integer division
        lead_zero = lead_zero - 1
    while (lead_zero > 0):
        b = '0' + b
        lead_zero = lead_zero - 1
    return b


def n_bit_list_using_iteration(n):
    l = list()
    for i in range((2**n)):
        l.append(itob(i, n))
    return l

##############################
# alternative-2 to creating n-bits:
#    Credit: https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python 
def n_bit_list_using_lib(n):
    return [ bin(i)[2:].zfill(n) for i in range(2**n)]

# Part C: Output all n-bit string addition results
def test_add(bit_list):
    l = len(bit_list)
    print("GF2_WordAdd Test for", len(bit_list[0]), "bits:")
    for i in range(l):
        print(bit_list[i], ":")
        for j in range(i, l):
            a = bit_list[i]
            b = bit_list[j]
            print("    ", a, "+", b, " = ", GF2_addword(a, b))
    print("===== done ====\n")


# list of 5-bit strings
five_bits_list = n_bit_list(5)
    # Alternative:
    #   r2 = range(2)
    #   [str(d0)+str(d1)+str(d2)+str(d3)+str(d4) for d0 in r2 for d1 in r2 for d2 in r2 for d3 in r2 for d4 in r2]

# Compute the list of alphabets + suppoted punctuations 
aOrd = ord('A')
alphabet_list = [chr(aOrd+r) for r in range(26)]
char_list = alphabet_list + [' ', '.', '!', ',', '?', ':']  # makes to 32 elements

# New build the forward code-to-char and backward char-to-code dictionaries
code_to_char = {a: b for (a, b) in zip(five_bits_list, char_list)}
    # NOTE: how to reverse a dictionary, there are MANY other ways, any will do
char_to_code = {code_to_char[x]: x for x in code_to_char}


# returns a decoded message with the given 5-bit code
def decode(coded_msg, my_key):
    r = []
    for code in coded_msg:
        wd = GF2_addword(code, my_key)
        r = r + [code_to_char[wd]]
    return r


# 
def check_msg(coded_msg):
    print("decoding ... ", coded_msg)
    for key in five_bits_list:
        m = decode(coded_msg, key)
        print('key=', key, '==>', ''.join(m))


def encode(msg, my_key):
    coded_msg = []
    for c in msg:
        coded_msg = coded_msg + [GF2_addword(char_to_code[c], my_key)]
    return coded_msg

# Now, output for the assignment ...
    
print("Output for Part-(C):")
print()
test_add(n_bit_list(2))
test_add(n_bit_list(3))
print("=================================================")
print("")

print("Output for Part-(D):")
print()
book_codes = ['10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101', '00100', '11001', '11010']
print("Decoding coded message from the book:")
check_msg(book_codes)
print("=================================================")
print("")

print("Output for Part-(E):")
print()
coded_msg = encode("THIS IS BORING! NOT FUN AT ALL.", '01010')
check_msg(coded_msg)
print("=================================================")
print("")


print("Output for Part-(F):")
print()

quit = False
while not quit:
    msg = input("Please enter your message: ")
    quit = msg == ""
    if not quit:
        code = input("Please enter your 5 bit code: ")
        coded_msg = encode(msg, code)
        print("This is the coded message: ", coded_msg)
        check_msg(coded_msg)
        
print("Thanks for playing. Bye")
print("=================================================")
print("")

my_coded_msg = ['10000', '00000', '00000', '01000', '11010', '00000', '01000', '10111', '00110', '11111', '01001', '01000', '11001', '11010', '11111', '10110', '10010', '00011', '01000', '10010', '11001', '10100', '10110', '10011', '00011', '10010', '01000', '10000', '10010', '11111', '01000', '10010', '11001', '00000', '11100', '01000', '10011', '10110', '01000', '10111', '00110', '11111', '01111', '01000', '00001', '10101', '11010', '00000', '01000', '10000', '11001', '10010', '00000', '00000', '01000', '11010', '00000', '01000', '10111', '00110', '11111', '01110', '01000']
print("What am I saying in this message?", my_coded_msg)
# check_msg(my_coded_msg)
