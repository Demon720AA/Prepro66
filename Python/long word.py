'''Long word'''
def lgw():
    '''aera'''
    word1 = input()
    word2 = input()
    word3 = input()
    c_word1 = len(word1)
    c_word2 = len(word2)
    c_word3 = len(word3)
    if c_word1 < c_word2 < c_word3:
        print(word1.capitalize())
        print(word2.capitalize())
        print(word3.capitalize())
    elif c_word1 < c_word3 < c_word2:
        print(word1.capitalize())
        print(word3.capitalize())
        print(word2.capitalize())
    elif c_word2 < c_word1 < c_word3:
        print(word2.capitalize())
        print(word1.capitalize())
        print(word3.capitalize())
    elif c_word2 < c_word3 < c_word1:
        print(word2.capitalize())
        print(word3.capitalize())
        print(word1.capitalize())
    elif c_word3 < c_word2 < c_word1:
        print(word3.capitalize())
        print(word2.capitalize())
        print(word1.capitalize())
    elif c_word3 < c_word1 < c_word2:
        print(word3.capitalize())
        print(word1.capitalize())
        print(word2.capitalize())
lgw()
