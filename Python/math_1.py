'''หารร่วมมาก'''
def process(num1, num2):
    '''ลืมdocstring;-;'''
    if num2 == 0:
        print("Number is", num1)
        return
    return process(num2, num1%num2)
def math():
    '''math'''
    num1 = int(input())
    num2 = int(input())
    process(num1, num2)
math()
