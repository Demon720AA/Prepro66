''' cosss '''
import math
def aey():
    '''function aera'''
    vector_x1 = float(input())
    vector_y1 = float(input())
    vector_x2 = float(input())
    vector_y2 = float(input())
    process1 = (vector_x1 * vector_x2) + (vector_y1 * vector_y2)
    process2 = (((vector_x1 ** 2)+(vector_y1**2)) ** 0.5)*(((vector_x2 ** 2)+(vector_y2**2)) ** 0.5)
    ps01 = process1/process2
    print(int(math.acos(ps01) * 180 // math.pi))#math.degrees
aey()
