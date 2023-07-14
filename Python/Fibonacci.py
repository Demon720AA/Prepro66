'''Fibonacci'''
def process(fibo):
    ''';-;'''
    if fibo == 1:
        return 1
    elif fibo == 0:
        return 0
    else:
        return process(fibo-1)+process(fibo-2)
def fib():
    '''เอ๊ว่ายาก'''
    fibo = int(input())
    if fibo == 1 or fibo == 2:
        print(1)
    elif fibo == 0:
        print(0)
    else:
        print(process(fibo))
fib()
