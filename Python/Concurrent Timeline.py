# '''Concurrent Timeline'''
# def aey():
#     '''aera'''
#     time = int(input())
#     second = time % 60
#     mstom = time // 60
#     minute = mstom % 60
#     mtoh = mstom // 60
#     hour = mtoh % 24
#     htod = mtoh // 24
#     print("%02d" % htod, ":", "%02d" % hour, ":", "%02d" % minute, ":", "%02d" % second, sep="")
# aey()

'''Concurrent Timeline.2'''
def aey():
    '''main'''
    time = int(input())
    second = time % 60
    minute = (time/60)%60
    hour = (time/3600)%24
    day = time//86400
    print("%02d:%02d:%02d:%02d" % (day, hour, minute, second))
aey()

# """Concurrent Timeline.3"""
# def aey():
#     """Bruh"""
#     sid = 86400
#     sih = 3600
#     sim = 60
#     second = int(input())
#     print("%02d:%02d:%02d:%02d" % \
#           (second//sid, (second%sid)//sih, \
#            ((second%sid)%sih)//sim, (((second%sid)%sih)%sim)))
# aey()
