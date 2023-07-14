'''Triangle'''
def tri():
    '''aera'''
    line1 = int(input())
    line2 = int(input())
    line3 = int(input())
    if line1 == line2 == line3:
        print("Equilateral triangle")
    elif line1 != line2 and line1 != line3 and line2 != line3:
        print("Scalene triangle")
    elif line1 == line2 or line2 == line3 or line1 == line3:
        print("Isosceles triangle")
tri()
