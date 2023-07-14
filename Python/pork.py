'''หมูเด้งได้'''
def pork():
    '''เหนื่อย'''
    check = "MH", "PH", "SH", "WH", "GH"
    mha = 0
    pha = 0
    sha = 0
    wha = 0
    gha = 0
    contorl = 0
    while contorl == 0:
        com = input()
        if com in check:
            if com == "MH":
                mha = mha + 1
            elif com == "PH":
                pha = pha + 1
            elif com == "SH":
                sha = sha + 1
            elif com == "WH":
                wha = wha + 1
            elif com == "GH":
                if mha > 0 and pha > 0 and sha > 0 and wha > 0:
                    gha = gha + 1
                    mha = 0
                    pha = 0
                    sha = 0
                    wha = 0
                # elif mha == 0 or pha == 0 or sha == 0 or wha == 0:
                #     mha = 0
                #     pha = 0
                #     sha = 0
                #     wha = 0
                #     print("ERROR")
        elif com == "END":
            break
        else:
            mha = 0
            pha = 0
            sha = 0
            wha = 0
            print("ERROR")
    print(gha)
pork()
