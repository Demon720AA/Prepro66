'''card'''
def card():
    '''aera'''
    card1 = int(input())
    if card1 // 10 == 1:
        if card1 % 10 == 2:
            print("A")
        elif card1 % 10 == 3:
            print("B")
        else:
            print("B")
    if card1 // 10 == 2:
        if card1 % 10 == 1:
            print("A")
        elif card1 % 10 == 3:
            print("C")
        else:
            print("B")
    if card1 // 10 == 3:
        if card1 % 10 == 2:
            print("C")
        elif card1 % 10 == 1:
            print("B")
        else:
            print("B")
card()
