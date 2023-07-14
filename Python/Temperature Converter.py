'''Temperature Converter'''
def c_f(temp):
    '''Celsius to Fahrenheit'''
    return temp*(9/5)+32
def c_k(temp):
    '''Celsius to Kelvin'''
    return temp + 273.15
def c_r(temp):
    '''Celsius to Rankine'''
    return (temp + 273.15)*(9/5)
def f_c(temp):
    '''Fahrenheir to Celsius'''
    return (temp-32)*(5/9)
def f_k(temp):
    '''Fahrenheir to Kelvin'''
    return (temp+459.67)*(5/9)
def f_r(temp):
    '''Fahrenheir to Rankine'''
    return temp+459.67
def k_c(temp):
    '''Kwlvin to Celsius'''
    return temp-273.15
def k_f(temp):
    '''Kwlvin to Fahrenheir'''
    return temp*(9/5)-459.67
def k_r(temp):
    '''Kwlvin to Ranking'''
    return temp*(9/5)
def r_c(temp):
    '''Rankine to Celsius'''
    return (temp-49.67)*(5/9)
def r_f(temp):
    '''Rankine to Fahrenheir'''
    return temp-459.67
def r_k(temp):
    '''Rankine to Kelvin'''
    return temp*(5/9)
def unit_c(unit2, unit, temp):
    '''Celsius'''
    if unit2 == "F":
        temp = c_f(temp)
        unit = "Fahrenheit"
    elif unit2 == "K":
        temp = c_k(temp)
        unit = "Kelvin"
    elif unit2 == "R":
        temp = c_r(temp)
        unit = "Rankine"
    return unit2, unit, temp
def unit_f(unit2, unit, temp):
    '''Celsius'''
    if unit2 == "C":
        temp = f_c(temp)
        unit = "Celsius"
    elif unit2 == "K":
        temp = f_k(temp)
        unit = "Kelvin"
    elif unit2 == "R":
        temp = f_r(temp)
        unit = "Rankine"
    return unit2, unit, temp
def tem():
    '''main'''
    temp = float(input())
    unit = input()
    unit1 = unit[:-2]# หา unit ตัวหลัง
    unit2 = unit[-1]# หา unit ตัวหน้า
    if unit1 == "C":
        unit = "Celsius"
        unit2, unit, temp = unit_c(unit2, unit, temp)
        # if unit2 == "F":
        #     temp = c_f(temp)
        #     unit = "Fahrenheit"
        # elif unit2 == "K":
        #     temp = c_k(temp)
        #     unit = "Kelvin"
        # elif unit2 == "R":
        #     temp = c_r(temp)
        #     unit = "Rankine"
    elif unit1 == "F":
        unit = "Fahrenheit"
        unit2, unit, temp = unit_f(unit2, unit, temp)
        # if unit2 == "C":
        #     temp = f_c(temp)
        #     unit = "Celsius"
        # elif unit2 == "K":
        #     temp = f_k(temp)
        #     unit = "Kelvin"
        # elif unit2 == "R":
        #     temp = f_r(temp)
        #     unit = "Rankine"
    elif unit1 == "K":
        unit = "Kelvin"
        if unit2 == "C":
            temp = k_c(temp)
            unit = "Celsius"
        elif unit2 == "F":
            temp = k_f(temp)
            unit = "Fahrenheit"
        elif unit2 == "R":
            temp = k_r(temp)
            unit = "Rankine"
    elif unit1 == "R":
        unit = "Rankine"
        if unit2 == "c":
            temp = r_c(temp)
            unit = "Celsius"
        elif unit2 == "F":
            temp = r_f(temp)
            unit = "Fahrenheit"
        elif unit2 == "K":
            temp = r_k(temp)
            unit = "Kelvin"
    print(unit, "= %.2f" %temp)
tem()
