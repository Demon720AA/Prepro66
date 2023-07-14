'''The Axiom 01'''
def axi():
    '''aera'''
    years = int(input())
    people = int(input())
    process = (((1400/1914)*360*years)*people)
    if (process % 1) > 0:
        process = process + 1
    print("To prepare for %d years in space" %years)
    print("AutoPilot will need %d cups of Cupcake-In-A-Cups" %(process))
    print("The Axiom will need %d trees on board" %(people*8))
axi()
