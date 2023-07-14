'''Alien Translator'''
def alien():
    ''':D'''
    check = 155, 69, 71, 47, 53, 210, 252
    text = input()
    plus = 0
    for i in text:
        i = ord(i)
        plus = plus + i
    # print(plus)
    if plus in check:
        print(((plus == 155)*'Hi!') + ((plus == 69) * 'Nice') + ((plus == 71) * 'Kill!') + \
        ((plus == 47)*'Spy!') + ((plus == 53)*'Food!') + ((plus == 210)*'Capture!') + \
        ((plus == 252)*'Not Found'))
    else:
        print("Unknown Word")
alien()
