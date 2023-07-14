'''Fast server'''
def fast():
    '''aera'''
    speed_a = int(input())
    time_a = input()
    speed_b = int(input())
    time_b = input()
    if time_a == "Millisecond":
        speed_a = speed_a / 1000
    elif time_a == "Microsecond":
        speed_a = speed_a / 1000000
    elif time_a == "Nanosecond":
        speed_a = speed_a / 1000000000
    elif time_a == "Picosecond":
        speed_a = speed_a / 1000000000000
    if time_b == "Millisecond":
        speed_b = speed_b / 1000
    elif time_b == "Microsecond":
        speed_b = speed_b / 1000000
    elif time_b == "Nanosecond":
        speed_b = speed_b / 1000000000
    elif time_b == "Picosecond":
        speed_b = speed_b / 1000000000000
    if speed_a > speed_b:
        print("Server B, %.6f second" % speed_b)
        print("Faster than server A , %.0f times" %(speed_a // speed_b))
    elif speed_b > speed_a:
        print("Server A, %.6f second" % speed_a)
        print("Faster than server B , %.0f times" %(speed_b // speed_a))
    elif speed_a == speed_b:
        print("equal")
fast()
