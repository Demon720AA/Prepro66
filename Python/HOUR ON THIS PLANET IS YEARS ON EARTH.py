'''HOUR ON THIS PLANET IS YEARS ON EARTH'''
def htp():
    '''aera'''
    time = int(input())
    process = round((time/60)*84) #84 = 7 * 12 7มาจาก1ชม=7ปี 12มาจาก1ปีมี12เดือน
    month = process % 12
    year = process // 12
    if time > 1:
        time1 = "%d Minutes" %time
    else:
        time1 = "1 Minute"
    if month > 1:
        month1 = "%d Months" %month
    else:
        month1 = "1 Month"
    if year > 1:
        year1 = "%d Years" %year
    else:
        year1 = "1 Year"
    if month == 0:
        print("%s here is %s on Earth." \
        % (time1, year1))
    elif year == 0:
        print("%s here is %s on Earth." \
        % (time1, month1))
    else:
        print("%s here is %s and %s on Earth." \
        % (time1, year1, month1))
htp()
