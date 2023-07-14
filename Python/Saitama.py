'''Saitama'''
def main():
    '''aera'''
    contorl = 0
    while contorl == 0:
        word = input()
        aword = word.count(" ")+1
        if aword > 20:
            print("Shorten it down to 20 words!!!")
            continue
        elif aword <= 20:
            print("I understand what you're saying.")
            break
main()
