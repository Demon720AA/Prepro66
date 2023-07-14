'''Box V.1'''
def aey():
    '''def'''
    num = int(input())
    for row in range(num):
        for col in range(num):
            if col == 0 or col == num-1 or row == num-1 or row == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
aey()
