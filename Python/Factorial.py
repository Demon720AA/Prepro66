'''Factorial'''
def fac():
    '''~_~'''
    num = int(input())
    num1 = num
    ans = num
    if num < 0:
        print("Please enter a positive integer.")
    elif num == 0:
        print(1)
    else:
        for _ in range(num-1):
            num1 = num1 - 1
            ans = ans * (num1)
        print(ans)
fac()
