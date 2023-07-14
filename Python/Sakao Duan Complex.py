'''Sakao Duan Complex'''
def sdc():
    '''aera'''
    month = int(input())
    keycard_1 = str.lower(input())
    keycard_2 = str.lower(input())
    damage = int(input())
    price = int(0)
    if month < 12:
        price = price + 15000
    if keycard_1 == "yes":
        price = price + 1000
    if keycard_2 == "yes":
        price = price + 500
    price = price + (damage * 300)
    if month >= 12 and keycard_1 == "no" and keycard_2 == "no"\
    and damage == 0:
        print("You got lucky!")
    else:
        print("Your payment is due, %d Baht" %price)
sdc()
