'''Certificate'''
def cer():
    '''aera'''
    name = input()
    surname = input()
    name2 = name.capitalize()
    surname2 = surname.capitalize()
    alpha1 = name.isalpha()
    alpha2 = surname.isalpha()
    if name == name2 and surname == surname2 and \
        alpha1 == True and alpha2 == True:
        print("Print certificate success.")
        print(name + "-" + surname)
    else:
        print("Cannot print certificate.")
cer()
