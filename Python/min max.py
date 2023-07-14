'''find("M\\M")'''
def fmm():
    '''main'''
    check = input()
    if check == "MAX":
        num1 = int(input())
        num = num1
        num2 = int(input())
        if num2 > num:
            num = num2
        num3 = int(input())
        if num3 > num:
            num = num3
        num4 = int(input())
        if num4 > num:
            num = num4
        num5 = int(input())
        if num5 > num:
            num = num5
    else:
        num1 = int(input())
        num = num1
        num2 = int(input())
        if num2 < num:
            num = num2
        num3 = int(input())
        if num3 < num:
            num = num3
        num4 = int(input())
        if num4 < num:
            num = num4
        num5 = int(input())
        if num5 < num:
            num = num5
    print(check, ":", num)
fmm()
