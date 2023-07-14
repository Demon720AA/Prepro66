'''Increasing Power'''
def inp():
    '''aera'''
    power = int(input())
    power_up = int(input())
    time = int(input())
    process = time * power_up
    power_max = power +process
    if power_up > 100000:
        print("I can FEEL it...")
    if power_max > 100000000:
        print("NOW I'M MAD!!!!")
    elif 0 <= power_max < 10000:
        print("Sorry... dad...")
    elif power_max < 0:
        print("Where am I..?")
    else:
        print(power_max)
inp()
