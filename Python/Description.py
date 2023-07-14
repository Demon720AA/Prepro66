'''Description'''
def des():
    '''aera'''
    money = float(input())
    if money >= 50:
        print("Taxi")
        print("no walking")
    elif money >= 40:
        print("BTS")
        print("walking")
    elif money >= 25:
        print("Motorcycle")
        print("no walking")
    elif money >= 8:
        print("Song Thaeo")
        print("walking")
    else:
        print("not going anywhere")
des()
