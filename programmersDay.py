year=int(input())
nonleapfebDays=28
daysumWithoutFeb=215
programmersDay=256
if year<1918:
    if year%4==0:
        leapfeb=nonleapfebDays+1
        daysum=daysumWithoutFeb+leapfeb
        day=programmersDay-daysum
        print(f"{day}.09.{year}")
#31+31+30+31+30+31+31=215
    else:
        daysum = daysumWithoutFeb + nonleapfebDays
        day = programmersDay - daysum
        print(f"{day}.09.{year}")
else:
    if year==1918:
        nonleapfebDays = 15
        if year%4==0 and year%100!=0:
            leapfeb=nonleapfebDays+1
            daysum = daysumWithoutFeb + leapfeb
            day = programmersDay - daysum
            print(f"{day}.09.{year}")
        else:
            daysum = daysumWithoutFeb + nonleapfebDays
            day = programmersDay - daysum
            print(f"{day}.09.{year}")
    else:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    leapfeb = nonleapfebDays + 1
                    daysum = daysumWithoutFeb + leapfeb
                    day = programmersDay - daysum
                    print(f"{day}.09.{year}")
                else:
                    daysum = daysumWithoutFeb + nonleapfebDays
                    day = programmersDay - daysum
                    print(f"{day}.09.{year}")
            else:
                leapfeb = nonleapfebDays + 1
                daysum = daysumWithoutFeb + leapfeb
                day = programmersDay - daysum
                print(f"{day}.09.{year}")
        else:
            daysum = daysumWithoutFeb + nonleapfebDays
            day = programmersDay - daysum
            print(f"{day}.09.{year}")

