'''Simple Decryption'''
def sim(num, num2):
    '''aera'''
    if num > 0:
        text = input()
        if text == "a" or text == "f" or text == "k" or text == "p" or\
        text == "u" or text == "z":
            num1 = num2 + 20
            sim(num-1, num1)
        elif text == "b" or text == "g" or text == "l" or text == "q" or\
        text == "v":
            num1 = num2 + 21
            sim(num-1, num1)
        elif text == "c" or text == "h" or text == "m" or text == "r" or\
        text == "w":
            num1 = num2 + 22
            sim(num-1, num1)
        elif text == "d" or text == "i" or text == "n" or text == "s" or\
        text == "x":
            num1 = num2 + 23
            sim(num-1, num1)
        elif text == "e" or text == "j" or text == "o" or text == "t" or\
        text == "y":
            num1 = num2 + 24
            sim(num-1, num1)
    else:
        print(num2)
sim(5, 0)
