'''MA LA XIANG GUO (SPICY NUMBING STIR-FRY POT)'''
def mal():
    '''aera'''
    lis = []
    sprice = ""
    check = "celery stalks", "carrots", "potatoes", "mushrooms", "tofu"\
    , "lotus root", "cabbage", "instant noodles", "glass noodle", "wonton"\
    , "beef", "pork loin", "chicken", "fish balls", "cheese ball", \
    "octopus", "fish", "shrimp", "mussels", "stop", 1, 2, 3, 4
    contorl = False
    while contorl == False:
        text = input()
        if text.lower() == "stop":
            contorl == True
            break
        lis.append(text.lower())
        continue
    if lis == []:
        print("Huh? you didn't order anything!")
    else:
        if lis[-1] == "1":
            sprice = "Mild"
        if lis[-1] == "2":
            sprice = "Medium"
        if lis[-1] == "3":
            sprice = "Hot"
        if lis[-1] == "4":
            sprice = "Extra hot"
        if sprice == "":
            print("Please choose a spiciness level!")
        elif check in lis:
            print(sprice, "Mala xiang guo is here.")
        else:
            print("Get out!")
mal()
