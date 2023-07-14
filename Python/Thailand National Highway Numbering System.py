'''Thailand National Highway Numbering System'''
def tnhns():
    '''aera'''
    road_num = int(input())
    if road_num >= 1 and road_num <= 4:
        print("highway connecting Bangkok to outlying regions")
    elif road_num == 7 or road_num == 9:
        print("motorway")
    elif road_num == 11 or road_num == 12 or road_num >= 21 \
        and road_num <= 24 or road_num >= 31 and road_num <= 38 \
        or road_num >= 41 and road_num <= 44:
        print("principal highway")
    elif road_num >= 101 and road_num <= 131 or road_num >= 201 \
        and road_num <= 299 or road_num >= 301 and road_num <= 376 \
        or road_num >= 401 and road_num <= 425:
        print("regional secondary highway")
    elif road_num >= 1001 and road_num <= 1430 or road_num >= 2027 \
        and road_num <= 2425 or road_num >= 3001 and road_num <= 3902 \
        or road_num >= 4001 and road_num <= 4373:
        print("intra-province highway")
    else:
        print("Invalid Route")
tnhns()
