'''Sleep Enough?'''
def sleep():
    '''aera'''
    sleep_h = int(input())
    sleep_m = int(input())
    weakup_h = int(input())
    weakup_m = int(input())
    process1 = (sleep_h * 60) + sleep_m#
    process2 = (weakup_h *60) + weakup_m
    if process2 < process1:
        process2 = process2 + 1440
    process3 = (process2 - process1) - 450
    weakup_h = (((process1 + 450))//60)%24#450=7.5H
    weakup_m = (process1 + 30)% 60
    if process3 >= 0:
        print("Sleep enough!")
    elif process3 < 0:
        print("P'Guy have to wake up at %02d:%02d" %(weakup_h, weakup_m))
sleep()

"""Sleep Enough?"""
 
 
# def sleep_time():
#     """Calculate sleep time"""
#     sleep_hour = int(input())
#     sleep_minute = int(input())
#     wake_up_hour = int(input())
#     wake_up_minute = int(input())
 
#     sleeping_minute = wake_up_minute - sleep_minute
#     sleeping_hour = (wake_up_hour - sleep_hour + sleeping_minute // 60) % 24
#     if sleeping_hour > 7 or (sleeping_hour == 7 and sleeping_minute % 60 >= 30):
#         print("Sleep enough!")
#     else:
#         should_wake_minute = sleep_minute + 30
#         should_wake_hour = (sleep_hour + 7 + should_wake_minute // 60) % 24
#         print("P'Guy have to wake up at %02d:%02d" %
#               (should_wake_hour, should_wake_minute % 60))
 
 
# sleep_time()