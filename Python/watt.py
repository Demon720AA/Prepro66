'''ค่าไฟนั้นแพง'''
def atv(watt):
    '''tv'''
    return ((watt*3)/1000)*30
def bmicro(watt):
    '''microwave'''
    return ((watt*1)/1000)*30
def cdai(watt):
    '''ไดร์เป่าผม**มี4เครื่อง'''
    return (((watt*0.5)/1000))*30
def dlight(watt):
    '''หลอดไฟ'''
    return ((watt*5)/1000*4)*30
def ecool(watt):
    '''ตู้เย็น'''
    return ((watt*24)/1000)*30
def wat():
    '''aera'''
    a_tv = int(input())
    b_microwave = int(input())
    c_dri = int(input())
    d_light = int(input())
    e_cool = int(input())
    print("TV %d Watt 1 ea for 3 hours" %(a_tv))
    print("%.2f unit." %(atv(a_tv)))
    print("Microwave %d Watt 1 ea for 1 hours" %(b_microwave))
    print("%.2f unit." %(bmicro(b_microwave)))
    print("Hair dryer %d Watt 1 ea for 0.5 hours" %(c_dri))
    print("%.2f unit." %(cdai(c_dri)))
    print("light bulb %d Watt 4 ea for 5 hours" %(d_light))
    print("%.2f unit." %(dlight(d_light)))
    print("Refrigerator %d Watt 1 ea for 24 hours" %(e_cool))
    print("%.2f unit." %(ecool(e_cool)))
wat()
