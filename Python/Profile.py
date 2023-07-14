# '''Profile'''
# def pro():
#     '''aera'''
#     sex = input()
#     sex = sex[0:-4]
#     sex = bool(sex)
#     id1 = input()
#     id1 = id1[0:6]
#     name = input()
#     surname = input()
#     age = input()
#     occupation = input()
#     print("======")
#     print("ID :", id1)
#     print("Name : Mr"+ ("s"*sex) + ".", name.capitalize(), surname.capitalize())
#     print("Age :", age, "years old")
#     print("Occupation :", occupation.upper())
#     print("======")
# pro()

"""prepro66"""
 
 
def main():
    """prepro66"""
    gender = (input()).capitalize()
    rahad = (input())
    name = (input())
    surname = (input())
    age = (input())
    work = (input())
    print("======")
    print ("ID :",rahad[0:6] )
    print("Name :", "Mr." * (gender == "Male") + "Mr.s" * (gender == "Female"), name.capitalize(), surname.capitalize())
    print("Age :", age, "year old")
    print("Occupation :", work.upper())
    print("======")
 
 
main()