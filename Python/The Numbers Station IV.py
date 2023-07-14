'''The Numbers Station IV'''
def tns():
    '''area'''
    inp01 = str((int(input()) + 6) % 10)
    inp02 = str((int(input()) + 6) % 10)
    inp03 = str((int(input()) + 6) % 10)
    inp04 = str((int(input()) + 8) % 10)
    inp05 = str((int(input()) + 3) % 10)
    print(inp01+inp02+inp03+inp04+inp05)
tns()
