'''Pizza topping'''
def pizza():
    '''No pineapple'''
    lis = []
    contorl = False
    while contorl == False:
        text = input()
        lis.append(text)
        if text == "done":
            contorl = True
    if "sauce" and "cheese" in lis:
        if "pineapple" in lis:
            print("My Ancestor is crying")
        else:
            print("Nice pizza!")
    else:
        print("It's not complete")
pizza()
