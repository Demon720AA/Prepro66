'''Time-Investment'''
# def sec(money, time, iq1):
#     '''เหนื่อย'''
#     money = money - 100
#     time = time + 1
#     if iq1 > 10:
#         iq1 = iq1 - 1
#     return
def tim():
    '''ข้อเมื่อกี้ผ่านได้ไง'''
    contorl = 0
    time = 0
    money = 2000
    iq1 = 15
    fun = 2
    mass = 0
    check = False
    while contorl == 0:
        work = input()
        if work == "Wake up":
            check = True
            continue
        elif work == "Collapse":
            break
        while check == True:
            if work == "Sleep":
                check = False
            elif work == "Work":
                money = money - 100
                time = time + 1
                money = money + 1000
                fun = fun - 0.8
            elif work == "Study":
                money = money - 100
                time = time + 1
                iq1 = iq1 + 1
                fun = fun - 0.5
            elif work == "Play":
                money = money - 100
                time = time + 1
                if fun < 50:
                    fun = fun + 2
                if mass > -10:
                    mass = mass - 0.5
            elif work == "Exercise":
                money = money - 100
                time = time + 1
                mass = mass + 0.6
            else:
                money = money - 100
                time = time + 1
                if iq1 > 10:
                    iq1 = iq1 - 1
            break
    print("Investment Result:")
    print("Time Invested: %d hours" %(time))
    print("End Money: %d Baht" %(money))
    print("End Knowledge: %d Unit" %(iq1))
    print("End Enjoyment: %.2f Unit" %(fun))
    print("End Muscle Mass: %.2f Unit" %(mass))
    print("Experiment Concluded")
tim()
