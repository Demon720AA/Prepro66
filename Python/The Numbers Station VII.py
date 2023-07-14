'''The Numbers Station VII'''
def main():
    '''The Numbers Station VII'''
    num = int(input())
    number = 1, 3, 5, 7, 2889, 2661, 2663, 2665, 2667, 2669, 2821, 2823, 2825, 2827, 2829, \
    2841, 41, 43, 45, 47, 49, 21, 23, 25, 27, 29, 2843, 2845, 2847, 2849, 2861, 9, 2865, 801, \
    803, 805, 807, 809, 821, 823, 825, 827, 829, 841, 843, 845, 847, 849, 861, 863, 865, 867, \
    869, 881, 883, 885, 887, 889, 421, 2867, 2869, 2881, 2883, 2885, 2887, 601, 603, 605, 607, \
    609, 621, 623, 625, 627, 629, 641, 643, 645, 647, 649, 661, 663, 665, 667, 669, 681, 683, \
    685, 687, 689, 423, 2681, 2683, 2685, 2687, 8881
    if num in number:
        print(((num == 1) * 'Space') + ((num == 3) * '!') + ((num == 5) * '"') + \
        ((num == 7) * '#') + ((num == 2889) * '$') + ((num == 2661) * '%') + \
        ((num == 2663) * '&') + ((num == 2665) * "'") + ((num == 2667) * '(') + \
        ((num == 2669) * ')') + ((num == 2821) * '*') + ((num == 2823) * '+') + \
        ((num == 2825) * ',') + ((num == 2827) * '-') + ((num == 2829) * '.') + \
        ((num == 2841) * '/') + ((num == 41) * '0') + ((num == 43) * '1') + \
        ((num == 45) * '2') + ((num == 47) * '3') + ((num == 49) * '4') + ((num == 21) * '5') + \
        ((num == 23) * '6') + ((num == 25) * '7') + ((num == 27) * '8') + ((num == 29) * '9') + \
        ((num == 2843) * ':') + ((num == 2845) * ';') + ((num == 2847) * '<') + \
        ((num == 2849) * '=') + ((num == 2861) * '>') + ((num == 9) * '?') + \
        ((num == 2865) * '@') + ((num == 801) * 'A') + ((num == 803) * 'B') + \
        ((num == 805) * 'C') + ((num == 807) * 'D') + ((num == 809) * 'E') + \
        ((num == 821) * 'F') + ((num == 823) * 'G') + ((num == 825) * 'H') + \
        ((num == 827) * 'I') + ((num == 829) * 'J') + ((num == 841) * 'K') + \
        ((num == 843) * 'L') + ((num == 845) * 'M') + ((num == 847) * 'N') + \
        ((num == 849) * 'O') + ((num == 861) * 'P') + ((num == 863) * 'Q') + \
        ((num == 865) * 'R') + ((num == 867) * 'S') + ((num == 869) * 'T') + \
        ((num == 881) * 'U') + ((num == 883) * 'V') + ((num == 885) * 'W') + \
        ((num == 887) * 'X') + ((num == 889) * 'Y') + ((num == 421) * 'Z') + \
        ((num == 2867) * '[') + ((num == 2869) * '\\') + ((num == 2881) * ']') + \
        ((num == 2883) * '^') + ((num == 2885) * '_') + ((num == 2887) * '`') + \
        ((num == 601) * 'a') + ((num == 603) * 'b') + ((num == 605) * 'c') + \
        ((num == 607) * 'd') + ((num == 609) * 'e') + ((num == 621) * 'f') + \
        ((num == 623) * 'g') + ((num == 625) * 'h') + ((num == 627) * 'i') + \
        ((num == 629) * 'j') + ((num == 641) * 'k') + ((num == 643) * 'l') + \
        ((num == 645) * 'm') + ((num == 647) * 'n') + ((num == 649) * 'o') + \
        ((num == 661) * 'p') + ((num == 663) * 'q') + ((num == 665) * 'r') + \
        ((num == 667) * 's') + ((num == 669) * 't') + ((num == 681) * 'u') + \
        ((num == 683) * 'v') + ((num == 685) * 'w') + ((num == 687) * 'x') + \
        ((num == 689) * 'y') + ((num == 423) * 'z') + ((num == 2681) * '{') + \
        ((num == 2683) * '|') + ((num == 2685) * '}') + ((num == 2687) * '~') + \
        ((num == 8881) * 'EOL'))
    else:
        print('Unknown')
main()

# '''Hehehe WHo need 200 line to do this'''
# def main():
#     '''https://rb.gy/u32mg'''
#     number = int(input())
#     res = "Unknown"
#     if number in range(1, 10, 2):
#         res = "?" if number == 9\
#             else chr(32+range(1, 8, 2).index(number)).replace(" ", "Space")
#     elif number in range(2661, 2670, 2):
#         res = chr(37+range(2661, 2670, 2).index(number))
#     elif number in range(41, 50, 2):
#         res = chr(48+range(41, 50, 2).index(number))
#     elif number in range(21, 30, 2):
#         res = chr(53+range(21, 30, 2).index(number))
#     elif number in range(2841, 2850, 2):
#         res = "/" if number == 2841\
#             else chr(58 + range(2841, 2850, 2).index(number)-1)
#     elif number in range(2861, 2870, 2):
#         res = ">" if number == 2861\
#             else "@" if number == 2865\
#             else chr(91+range(2867, 2870, 2).index(number))
#     elif number in range(801, 810, 2):
#         res = chr(65+range(801, 810, 2).index(number))
#     elif number in range(821, 830, 2):
#         res = chr(70+range(821, 830, 2).index(number))
#     elif number in range(841, 850, 2):
#         res = chr(75+range(841, 850, 2).index(number))
#     elif number in range(861, 870, 2):
#         res = chr(80+range(861, 870, 2).index(number))
#     if res == "Unknown":
#         return page2(number)
#     return res


# def page2(number):
#     """Why the fuck?"""
#     res = "Unknown"
#     if number in range(881, 890, 2):
#         res = chr(85+range(881, 890, 2).index(number))
#     elif number in range(2881, 2890, 2):
#         res = "$" if number == 2889 else chr(93+range(2881, 2888, 2).index(number))
#     elif number in range(601, 610, 2):
#         res = chr(97+range(601, 610, 2).index(number))
#     elif number in range(621, 630, 2):
#         res = chr(102+range(621, 630, 2).index(number))
#     elif number in range(641, 650, 2):
#         res = chr(107+range(641, 650, 2).index(number))
#     elif number in range(661, 670, 2):
#         res = chr(112+range(661, 670, 2).index(number))
#     elif number in range(681, 690, 2):
#         res = chr(117+range(681, 690, 2).index(number))
#     elif number in range(2681, 2688, 2):
#         res = chr(123+range(2681, 2688, 2).index(number))
#     elif number in range(2821, 2830, 2):
#         res = chr(42+range(2821, 2830, 2).index(number))
#     res = "Z" if number == 421\
#         else "z" if number == 423 else "EOL" if number == 8881 else res
#     return res


print((main()))

# '''The Numbers Station VII'''
# def tns12(num):
#     '''aera'''
#     if num == 2681:
#         print("""{""")
#     elif num == 2683:
#         print("""|""")
#     elif num == 2685:
#         print("""}""")
#     elif num == 2687:
#         print("""~""")
#     elif num == 2865:
#         print("""@""")
#     elif num == 2861:
#         print(""">""")
#     else:
#         print("Unknown")
#         return

# def tns11(num):
#     '''aera'''
#     if num == 2849:
#         print("""=""")
#     elif num == 2843:
#         print(""":""")
#     elif num == 2845:
#         print(""";""")
#     elif num == 2847:
#         print("""<""")
#     elif num == 2849:
#         print("""=""")
#     elif num == 2867:
#         print("""[""")
#     elif num == 2869:
#         print("""\\""")
#     elif num == 2881:
#         print("""]""")
#     elif num == 2883:
#         print("^")
#     elif num == 2885:
#         print("_")
#     elif num == 2887:
#         print("`")
#     else:
#         tns12(num)

# def tns10(num):
#     '''aera'''
#     if num == 2661:
#         print("""%""")
#     elif num == 2663:
#         print("""&""")
#     elif num == 2665:
#         print("""'""")
#     elif num == 2667:
#         print("""(""")
#     elif num == 2669:
#         print(""")""")
#     elif num == 2821:
#         print("""*""")
#     elif num == 2823:
#         print("""+""")
#     elif num == 2825:
#         print(""",""")
#     elif num == 2827:
#         print("-")
#     elif num == 2829:
#         print(".")
#     else:
#         tns11(num)

# def tns9(num):
#     '''aera'''
#     if num == 681:
#         print("u")
#     elif num == 683:
#         print("v")
#     elif num == 685:
#         print("w")
#     elif num == 687:
#         print("x")
#     elif num == 689:
#         print("y")
#     elif num == 2889:
#         print("$")
#     elif num == 2841:
#         print("/")
#     else:
#         tns10(num)

# def tns8(num):
#     '''aera'''
#     if num == 641:
#         print("k")
#     elif num == 643:
#         print("l")
#     elif num == 645:
#         print("m")
#     elif num == 647:
#         print("n")
#     elif num == 649:
#         print("o")
#     elif num == 661:
#         print("p")
#     elif num == 663:
#         print("q")
#     elif num == 665:
#         print("r")
#     elif num == 667:
#         print("s")
#     elif num == 669:
#         print("t")
#     else:
#         tns9(num)

# def tns7(num):
#     '''aera'''
#     if num == 601:
#         print("a")
#     elif num == 603:
#         print("b")
#     elif num == 605:
#         print("c")
#     elif num == 607:
#         print("d")
#     elif num == 609:
#         print("e")
#     elif num == 621:
#         print("f")
#     elif num == 623:
#         print("g")
#     elif num == 625:
#         print("h")
#     elif num == 627:
#         print("i")
#     elif num == 629:
#         print("j")
#     else:
#         tns8(num)

# def tns6(num):
#     '''aera'''
#     if num == 881:
#         print("U")
#     elif num == 883:
#         print("V")
#     elif num == 885:
#         print("W")
#     elif num == 887:
#         print("X")
#     elif num == 889:
#         print("Y")
#     else:
#         tns7(num)

# def tns5(num):
#     '''aera'''
#     if num == 841:
#         print("K")
#     elif num == 843:
#         print("L")
#     elif num == 845:
#         print("M")
#     elif num == 847:
#         print("N")
#     elif num == 849:
#         print("O")
#     elif num == 861:
#         print("P")
#     elif num == 863:
#         print("Q")
#     elif num == 865:
#         print("R")
#     elif num == 867:
#         print("S")
#     elif num == 869:
#         print("T")
#     else:
#         tns6(num)
# def tns4(num):
#     '''aera'''
#     if num == 801:
#         print("A")
#     elif num == 803:
#         print("B")
#     elif num == 805:
#         print("C")
#     elif num == 807:
#         print("D")
#     elif num == 809:
#         print("E")
#     elif num == 821:
#         print("F")
#     elif num == 823:
#         print("G")
#     elif num == 825:
#         print("H")
#     elif num == 827:
#         print("I")
#     elif num == 829:
#         print("J")
#     else:
#         tns5(num)

# def tns3(num):
#     '''aera'''
#     if num == 1:
#         print("Space")
#     elif num == 3:
#         print("!")
#     elif num == 5:
#         print("\"")
#     elif num == 7:
#         print("#")
#     elif num == 9:
#         print("?")
#     elif num == 21:
#         print("5")
#     elif num == 23:
#         print("6")
#     elif num == 25:
#         print("7")
#     elif num == 27:
#         print("8")
#     elif num == 29:
#         print("9")
#     else:
#         tns4(num)

# def tns2(num):
#     '''aera'''
#     if num == 41:
#         print("0")
#     elif num == 43:
#         print("1")
#     elif num == 45:
#         print("2")
#     elif num == 47:
#         print("3")
#     elif num == 49:
#         print("4")
#     elif num == 421:
#         print("Z")
#     elif num == 423:
#         print("z")
#     elif num == 8881:
#         print("EOL")
#     else:
#         tns3(num)

# def tns1(num):
#     '''aera'''
#     if num == 1:
#         print("Space")
#     elif num == 3:
#         print("!")
#     elif num == 5:
#         print("\"")
#     elif num == 7:
#         print("#")
#     elif num == 9:
#         print("?")
#     elif num == 21:
#         print("5")
#     elif num == 23:
#         print("6")
#     elif num == 25:
#         print("7")
#     elif num == 27:
#         print("8")
#     elif num == 29:
#         print("9")
#     else:
#         tns2(num)

# tns1(int(input()))
