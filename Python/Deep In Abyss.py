'''Deep In Abyss'''
def human1():
    '''main'''
    name = input()
    fall = int(input())
    if 0 <= fall <= 1350:
        layer_num = "1st"
        layer = "Edge of the Abyss"
    elif 1351 <= fall <= 2600:
        layer_num = "2nd"
        layer = "Forest of Temptation"
    elif 2601 <= fall <= 7000:
        layer_num = "3rd"
        layer = "Great Fault"
    elif 7001 <= fall <= 12000:
        layer_num = "4th"
        layer = "The Goblets of Giants"
    elif 12001 <= fall <= 13000:
        layer_num = "5th"
        layer = "Sea of Corpses"
    elif 13001 <= fall <= 15500:
        layer_num = "6th"
        layer = "The Capital of the Unreturned"
    elif 15501 <= fall:
        layer_num = "7th"
        layer = "The Final Maelstrom"
    print("Name :", name)
    print(layer_num, "Layer :", layer)
    print("Curse :", human2(layer_num))
def human2(layer_num):
    '''เช็คคำสาป'''
    up_or_down = input()
    curse = "-"
    if layer_num == "1st" and up_or_down == "UP":
        curse = "Light dizziness and nausea."
    elif layer_num == "2nd" and up_or_down == "UP":
        curse = "Intense nausea, headaches, and numbness of limbs."
    elif layer_num == "3rd" and up_or_down == "UP":
        curse = "Vertigo combined with visual and auditory hallucinations."
    elif layer_num == "4th" and up_or_down == "UP":
        curse = "Intense pain throughout the body and bleeding from every orifice."
    elif layer_num == "5th" and up_or_down == "UP":
        curse = "Complete sensory deprivation, confusion and self-harming behavior."
    elif layer_num == "6th" and up_or_down == "UP":
        curse = "Loss of humanity or death, or under specific conditions, the Blessing."
    elif layer_num == "7th" and up_or_down == "UP":
        curse = "Certain death."
    return curse
def main():
    '''main'''
    human1()
    print("---")
    human1()
    print("---")
    human1()
main()
