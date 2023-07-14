'''Quadrant'''
def qua():
    '''aera'''
    num_x = float(input())
    num_y = float(input())
    if num_x == 0 or num_y == 0:
        print("on the axis")
    elif num_x > 0 and num_y > 0:
        print("1")
    elif num_x < 0 and num_y > 0:
        print("2")
    elif num_x < 0 and num_y < 0:
        print("3")
    elif num_x > 0 and num_y < 0:
        print("4")
qua()
