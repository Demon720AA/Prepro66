'''Basic List'''
def basic():
    '''aera'''
    num = int(input())
    lis = []
    for _ in range(num):
        lis.append(input())
    print(lis)
    if lis == []:
        print("Empty!!!")
    else:
        for j in range(num):
            print(lis[j])
            j = j+1
basic()
