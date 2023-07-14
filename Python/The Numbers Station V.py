'''The Numbers Station V'''
def tns():
    '''aera'''
    num = int(input())
    if num >= 1 and num <= 6:
        print("A E I N O T")
    elif num >= 70 and num <= 79:
        print("B C D F G H J K L")
    elif num >= 80 and num <= 89:
        print("P Q R S U V W X Y Z")
    elif num >= 90 and num <= 98:
        print(""". : ' ( ) + - =""")
    elif num == 99:
        print("Spacebar")
    else:
        if num < 0:
            print("Unknown")
            print("Negative numbers aren't allowed.")
        else:
            print("Unknown")
tns()
