'''Sensitivity Finder'''
def ssf():
    '''aera'''
    pep = 0
    nub = 0
    prn = 100
    print("%.2f?" %(prn))
    speed = input()
    nub = nub + 1
    if speed == "S":
        while speed == "S":
            prn = prn * 2
            print("%.2f?" %(prn))
            speed = input()
    if speed == "F":
        prn = prn - (50/nub)
        nub = nub + 1
        print("%.2f?" %(prn))
    elif speed == "D":
        pep = pep + 1
    while pep == 0:
        speed = input()
        if speed == "F":
            prn = prn-(50/nub)
            print("%.2f?" %(prn))
        elif speed == "S":
            prn = prn+(50/nub)
            print("%.2f?" %(prn))
        elif speed == "D":
            pep = pep + 1
            break
        nub = nub * 2
    print("Your sensitivity is %.2f." %(prn))
ssf()
