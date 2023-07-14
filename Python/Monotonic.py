'''Monotonic'''
def main(tell2, check):
    '''main'''
    contorl = 1
    while contorl == 1:
        tell = input()
        if tell == "end":
            return (tell2, check)
        else:
            tell = int(tell)
            if tell2 > tell:
                check = False
                tell2 = tell
                return (tell2, check)
            else:
                tell2 = tell
                continue
def mon():
    '''aera'''
    check = bool(True)
    contorl = 0
    tell1 = int(input())
    while contorl == 0:
        tell2 = input()
        if tell2 != "end":
            tell2 = int(tell2)
            if tell1 > tell2:
                contorl = 0
            elif tell1 < tell2:
                tell2, check = main(tell2, check)
                contorl = 1
        elif tell1 == tell2:
            continue
        elif tell2 == "end":
            contorl = 1
        while contorl == 0:
            tell = input()
            if tell == "end":
                break
            else:
                tell = int(tell)
                if tell2 < tell:
                    check = False
                    tell2 = tell
                else:
                    tell2 = tell
                    continue
        break
    print(check)
mon()
