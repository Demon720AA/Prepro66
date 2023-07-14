'''Treasure Hunter'''
def trh():
    '''aera'''
    temp = int(input())
    gravity = float(input())
    if temp > 100 and 0 < gravity < 2:
        print("Visited the Luminous Crystal Planet.")
    elif -50 <= temp <= 100 and gravity > 3:
        print("Visited the Majestic Gravity Well Planet.")
    elif -50 > temp and 0.5 <= gravity <= 1.5:
        print("Visited the Enigmatic Floating Island Planet.")
    else:
        print("Visited the Mystery Planet.")
trh()
