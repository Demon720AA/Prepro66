'''Box V.3'''
def box():
    '''งื่มๆๆๆ'''
    num = int(input())
    for row in range(num):
        for col in range(num):
            if col == 0 or col == num-1 or row == num-1 \
            or row == 0 or row == num//2 or col == num//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # print((num/2)-0.5)
box()
