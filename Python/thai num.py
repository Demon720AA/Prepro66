'''Thai num'''
def thai():
    '''aera'''
    price = 0
    national_ceck = 1
    sela_per = 1
    sela_per2 = 1
    u_thai = input()
    if u_thai == "N":
        national = input()
        national_ceck = national_ceck * 5
        if national == "Vietnam" or national == "Singapore"\
            or national == "India":
            sela_per = sela_per * (50/100)
    old = int(input())
    if 20 >= old > 10:
        price = price + 20
    elif 60 >= old > 20:
        price = price + 40
    sela = input()
    if sela == "Y":
        sela_per2 = sela_per2 *(1- (int(input())/100))
    print("%.2f" %(price * national_ceck * (sela_per) * sela_per2))
thai()
