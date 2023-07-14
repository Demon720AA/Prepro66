# '''icescream'''
# def aey():
#     '''aera'''
#     import math
#     height = float(input())
#     radius = float(input())
#     process = math.pi * radius * height + math.pi * radius ** 2
#     print("Cone area is %.4f" % process)
# aey()

"""
calculate the total amount
"""
import math
 
 
def main():
    """
    input and calculate and print the result function
    """
    numberx = float(input())
    numbery = float(input())
    l = math.sqrt(numberx**2+numbery**2)
    roundx = (math.pi*numbery**2)
    side = (math.pi*numbery*l)
    answer = side+roundx
    print("Cone area is", '%.4f' % (answer))
 
 
main()