'''While_Sum'''
def main():
    '''aera'''
    contorl = 0
    plus = 0
    while contorl == 0:
        num = int(input())
        if num < 0:
            break
        else:
            plus = plus + num
    print(plus)
main()
