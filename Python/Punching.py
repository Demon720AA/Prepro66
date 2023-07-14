'''Punching'''
def main():
    '''aera'''
    contorl = 0
    nub = 0
    punch = input()
    while contorl == 0:
        if punch == "(9*-*)9":
            punch = input()
            if punch == "(9*-*)--o":
                punch = input()
                if punch == "(>*)9-o":
                    nub = nub + 1
                elif punch == "done!":
                    break
                else:
                    punch = input()
                    continue
            elif punch == "done!":
                break
            else:
                continue
        elif punch == "done!":
            break
        else:
            punch = input()
            continue
    print(nub, "sets")
main()
