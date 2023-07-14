'''Again Please'''
def aga():
    '''กิมจิอร่อย'''
    main_text = input()
    limite = int(input())
    while (limite+1) > 0:
        text_back = input()
        if text_back == main_text:
            print("Yes")
            break
        elif limite == 0 and text_back != main_text:
            print("OMG!")
            break
        else:
            limite = limite - 1
            print(main_text)
aga()
