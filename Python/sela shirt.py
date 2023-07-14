'''sela shirt'''
def sls():
    '''aera'''
    price = 12800
    employment = input()
    if employment == "Magician":
        guild = input()
    else:
        guild = ""
    armor = int(input())
    if guild == "Fairy Tail":
        print("Total %d Jewel" %((price*armor)*0.8))
    elif guild == "Sabertooth" and armor > 5:
        print("Total %d Jewel" %((price*armor)*0.85))
    elif guild == "Lamia Scale" and 3 <= armor:
        print("Total %d Jewel" %((price*armor)*0.9))
    elif guild == "Blue Pegasus" and armor > 10:
        print("Total %d Jewel" %((price*armor)*0.95))
    else:
        print("Total %d Jewel" %((price*armor)))
sls()
