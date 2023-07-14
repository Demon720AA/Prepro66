'''Kangsom'''
def main():
    '''aera'''
    contorl = ""
    price = 0
    nub = 0
    while contorl == "":
        menu = input()
        if menu == "shrimp sour soup":
            price = price + 80
            nub = nub + 1
            continue
        elif menu == "mixed vegetables sour soup":
            price = price + 60
            nub = nub + 1
            continue
        elif menu == "papaya sour soup":
            price = price + 55
            nub = nub + 1
            continue
        elif menu == "snapper fish sour soup":
            price = price + 100
            nub = nub + 1
            continue
        elif menu == "cha om shrimp sour soup":
            price = price + 100
            nub = nub + 1
            continue
        elif menu == "stop":
            break
        else:
            continue
    if price >= 200 and nub >= 3:
        sale = 15
    else:
        sale = 0
    print("Original Price %d baht" %(price))
    print("Discount %d baht" %(price*(sale/100)))
    print("Total %d baht" %(price - (price*(sale/100))))
main()
