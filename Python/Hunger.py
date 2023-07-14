'''Hunger'''
def pera():
    '''Lobster'''
    rows = int(input())
    for i in range(rows):
        for j in range(rows):
            if i >= j:
                print("* ", end="")
            else:
                print(" ", end="")
        print()

    # text = input()
    # num = len(text)
    # k = 0
    # for row in text:
    #     for col in range(num):
    #         if row == 0:                
    #             print(row, end=" ")
    #         else:
    #             print(end=" ")
    #     print()
pera()
