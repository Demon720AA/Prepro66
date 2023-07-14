'''(Bonus) น้ำดื่มละอองดาว I'''
def doa():
    '''เพลียเพลี้ยเพลีย'''
    price_a = int(input()) #ราคาเต็ม
    bottle = int(input()) #จำนวนฝาที่นำมาแลก
    sell = int(input()) #ราคาที่ลด
    buy = int(input()) #จำนวนขวดที่ซื้อ
    full = price_a * buy #ราคาเต็มที่จ่าย
    if bottle > 0 and sell <= price_a and buy > 0:
        bot_sell = (buy-1) // bottle #จำวนขวดที่ลดราคา
        sell = (price_a-sell)*bot_sell #จำนวนที่ลด
    else:
        sell = 0
    # print(full, sell)
    print(full-sell)
doa()
