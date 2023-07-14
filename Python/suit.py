'''suit'''
def f_a(num):
    '''f(a)'''
    return (num**2 + 2)*7
def g_xy(num1, num2):
    '''g(x, y)'''
    return 3*(num1+num2)*2+4
def h_rza(num1, num2, num3):
    '''h(r, z, a)'''
    return ((num1+num2)/num3)+(num3/num2)
def i_abcd(num1, num2, num3, num4):
    '''i(a, b, c, d)'''
    return ((num1*num3+num4*num2)**2)/(num3**2 * num4**2 * 10)
def sui():
    '''aera'''
    a_num = float(input())
    b_num = float(input())
    c_num = float(input())
    print("x1 :", f_a(a_num))
    print("x2 :", g_xy(f_a(b_num), a_num))
    print("x3 :", h_rza(f_a(g_xy(a_num+b_num, c_num)), \
                g_xy(f_a(c_num+b_num), c_num), \
                f_a(b_num+c_num)))
    print("x4 :", i_abcd(g_xy(f_a(g_xy(a_num+b_num, c_num))\
    , h_rza(g_xy(b_num+c_num, f_a(g_xy(b_num, c_num+a_num))), \
    c_num, a_num+b_num)), g_xy(f_a(c_num+b_num), b_num*a_num), \
    f_a(c_num), g_xy(f_a(f_a(a_num)), c_num)))
sui()
