
def leapYear(daysumWithoutFeb,programmersDay):
    leapfebDays = 29
    daysum = daysumWithoutFeb + leapfebDays
    day = programmersDay - daysum
    return day
def nomalYear(nonleapfebDays,daysumWithoutFeb,programmersDay):
    daysum = daysumWithoutFeb + nonleapfebDays
    day = programmersDay - daysum
    return day
def printt(date,year):
    print(f"{date}.09.{year}")

def main():
    year = int(input())
    nonleapfebDays0 = 28
    daysumWithoutFeb = 215
    programmersDay = 256
    if year%4==0:

        if year>1918:
            if year%100==0:
                if year%400==0:
                    date=leapYear(daysumWithoutFeb,programmersDay)
                    printt(date,year)
                else:
                    date = nomalYear(nonleapfebDays0,daysumWithoutFeb,programmersDay)
                    printt(date,year)
            else:
                date = leapYear(daysumWithoutFeb, programmersDay)
                printt(date, year)
        else:

            print("test 1")
            date = leapYear(daysumWithoutFeb,programmersDay)
            printt(date,year)
    else:
        if year==1918:
            nonleapfebDays0=15
        date = nomalYear(nonleapfebDays0,daysumWithoutFeb,programmersDay)
        printt(date,year)
main()
