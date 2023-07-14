'''Peashooter'''
def shoot():
    '''เอ๊เห็นจำนวนข้อและเครียด'''
    num = int(input())
    text = ""
    if num > 20:
        print("Game Over")
    else:
        for num in range(num):
            text = text + " o"
        print("'O<" + text)
shoot()
