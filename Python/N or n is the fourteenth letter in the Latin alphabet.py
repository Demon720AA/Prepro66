'''N, or n, is the fourteenth letter in the Latin alphabet'''
def non():
    ''':('''
    num = int(input())
    for  i in range(num):
        for row in range(num):
            if row == 0 or (i == row and (row > 0 and row < num)) or row == num-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
non()
