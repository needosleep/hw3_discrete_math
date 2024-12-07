
# def invert_number(number):
#     inverted = bin(number).replace('1', '2').replace('0', '1').replace('2', '0')[2:]
#     return(int(inverted, 2))



# from itertools import product

# def printFormula(formula):
#     print("  a b c f")
#     i = 1
#     for p in product([0, 1], repeat=3):
#         a, b, c = p
#         f = eval(formula)
#         print(i, a, b, c, int(f))
#         i += 1

from itertools import product

def nand(a, b):
    return not (a and b)

def binary_to_gray(b):
    b4, b3, b2, b1 = b

    g3 = b4
    n1 = nand(b3, b3)
    n2 = nand(b4, b4)
    g2 = nand(nand(b4, n1), nand(n2, b3))

    n3 = nand(b2, b2)
    g1 = nand(nand(b3, n3), nand(n1, b2))

    n4 = nand(b1, b1)
    g0 = nand(nand(b2, n4), nand(n3, b1))

    return [int(g3), int(g2), int(g1), int(g0)]

for p in product([0, 1], repeat=4):
    a, b, c, d = p
    binary_input = [int(a), int(b), int(c), int(d)]
    gray_output = binary_to_gray(binary_input)
    print("Binary:", binary_input)
    print("Gray Code:", gray_output)
    print()
