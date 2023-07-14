# '''The Numbers Station VI'''
# def tns():
#     '''aera'''
#     num = int(input())
#     if 1 <= num <= 6:
#         def tns1():
#             '''aera'''
#             if num == 1:
#                 print("A")
#             elif num == 2:
#                 print("E")
#             elif num == 3:
#                 print("I")
#             elif num == 4:
#                 print("N")
#             elif num == 5:
#                 print("O")
#             elif num == 6:
#                 print("T")
#         tns1()
#     elif 70 <= num <= 79:
#         def tns2():
#             '''aera'''
#             if num == 70:
#                 print("B")
#             elif num == 71:
#                 print("C")
#             elif num == 72:
#                 print("D")
#             elif num == 73:
#                 print("F")
#             elif num == 74:
#                 print("G")
#             elif num == 75:
#                 print("H")
#             elif num == 76:
#                 print("J")
#             elif num == 77:
#                 print("K")
#             elif num == 78:
#                 print("L")
#             elif num == 79:
#                 print("M")
#         tns2()
#     elif 80 <= num <= 89:
#         def tns3():
#             '''aera'''
#             if num == 80:
#                 print("P")
#             elif num == 81:
#                 print("Q")
#             elif num == 82:
#                 print("R")
#             elif num == 83:
#                 print("S")
#             elif num == 84:
#                 print("U")
#             elif num == 85:
#                 print("V")
#             elif num == 86:
#                 print("W")
#             elif num == 87:
#                 print("X")
#             elif num == 88:
#                 print("Y")
#             elif num == 89:
#                 print("Z")
#         tns3()
#     elif num == 0 or 90 <= num <= 99:
#         print("Not an alphabet")
#     elif num < 0:
#         print("Negative numbers aren't allowed.")
#     else:
#         print("Unknown")
# tns()

# '''Kong_(Kongfa)_The Numbers Station VI'''
# def main():
#     '''Kong_(Kongfa)_The Numbers Station VI'''
#     num = int(input())
#     if num < 0:
#         print("Negative numbers aren't allowed.")
#     elif not (0 <= num <= 6 or 70 <= num <= 99):
#         print('Unknown')
#     elif 0 < num <= 6 or 70 <= num <= 89:
#         print(('A' * (num == 1)) + ('E' * (num == 2)) + ('I' * (num == 3)) + \
#         ('N' * (num == 4)) + ('O' * (num == 5)) + ('T' * (num == 6)) + ('B' * (num == 70)) + \
#         ('C' * (num == 71)) + ('D' * (num == 72)) + ('F' * (num == 73)) + ('G' * (num == 74)) + \
#         ('H' * (num == 75)) + ('J' * (num == 76)) + ('K' * (num == 77)) + ('L' * (num == 78)) + \
#         ('M' * (num == 79)) + ('P' * (num == 80)) + ('Q' * (num == 81)) + ('R' * (num == 82)) + \
#         ('S' * (num == 83)) + ('U' * (num == 84)) + ('V' * (num == 85)) + ('W' * (num == 86)) + \
#         ('X' * (num == 87)) + ('Y' * (num == 88)) + ('Z' * (num == 89)))
#     else:
#         print('Not an alphabet')
# main()

"""The Numbers Station VI"""
 
 
def print_alphabet(password):
    """if password is in a table and output is alphabet"""
    if password == 1:
        print("A")
    elif password == 2:
        print("E")
    elif password == 3:
        print("I")
    elif password == 4:
        print("N")
    elif password == 5:
        print("O")
    elif password == 6:
        print("T")
    elif password <= 72:
        print(chr(password - 4))
    elif password <= 75:
        print(chr(password - 3))
    elif password <= 79:
        print(chr(password - 2))
    elif password <= 83:
        print(chr(password))
    else:
        print(chr(password + 1))
 
 
def ct_table(password):
    """Output password"""
    if password < 0:
        print("Negative numbers aren't allowed.")
    elif password > 99:
        print("Unknown")
    elif password > 6 and password < 70:
        print("Unknown")
    elif password == 0 or password > 89:
        print("Not an alphabet")
    else:
        print_alphabet(password)
 
 
ct_table(int(input()))