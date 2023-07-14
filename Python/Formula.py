'''ใส่สูตร(อย่าใส่เดี่ยวมากกว่า)'''
def aey():
    '''math'''
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    print("x1 : ", (-num_a * num_b + num_a) / (num_c * 2) + num_a ** 2, sep="")
    print("x2 : ", (num_a * num_b + num_a) / (num_c * 2) - num_a **2, sep="")
aey()
