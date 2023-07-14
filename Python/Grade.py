'''Grade'''
def grade():
    '''aera'''
    point = float(input())
    if 100 >= point >= 80:
        print("Grade : A")
        print("Yahoo!")
    elif 80 > point >= 75:
        print("Grade : B+")
        print("Yahoo!")
    elif 75 > point >= 70:
        print("Grade : B")
        print("Yahoo!")
    elif 70 > point >= 65:
        print("Grade : C+")
        print("Yahoo!")
    elif 65 > point >= 60:
        print("Grade : C")
        print("Try again!")
    elif 60 > point >= 50:
        print("Grade : D+")
        print("Try again!")
    elif 0 <= point < 50:
        print("Grade : F")
        print("So sad!")
    else:
        print("Grade : N/A")
        print("I'm confused")
grade()
