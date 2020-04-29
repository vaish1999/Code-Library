import datetime
# month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def overlap(month, year):
    # daydict = [[] for i in range(7)]
    sundays = []
    # fridays = []
    # lc = []
    # off = []

    if is_leap(year):
        days_in_month[1] = 29

    num_days = days_in_month[month-1]
    day_one = datetime.date(year, month, 1)
    start_day = day_one.isoweekday()

    start = start_day
    if start_day >= 7:
        start_day = 0
        start = 0
    # print(start)
    first_sun = 1 if start == 0 else 1 + (7 - start)
    first_fri = 7 if start == 6 else 1 + (5 - start)

    # lc.append(first_fri)
    # lc.append(first_fri + 10)

    lc = first_fri + 10

    for d in range(first_sun, num_days + 1, 7):
        sundays.append(d)

    off = sundays[-2]
    # for d in range(first_fri, num_days + 1, 7):
    #     fridays.append(d)

    # for day in range(1, num_days+1):
    #     daydict[start_day].append(day)
    #     start_day += 1
    #     if start_day >= 7:
    #         start_day = 0
    # print(daydict)

    # print(sundays)
    # print(fridays)

    # print(lc, off)
    if off < lc:
        return 1
    else:
        return 0

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


t = int(input())
for case in range(t):
    m1, y1 = list(map(int, input().split()))
    m2, y2 = list(map(int, input().split()))

    ov = 0

    # input_year = input()
    # year = int(input_year)
    # input_month = input()
    # month = int(input_month)
    if y2 == y1:
        for month in range(m1, m2 + 1):
            ov += overlap(month, y1)

    else:

        for month in range(m1, 13):
            # print(month, y1)
            ov += overlap(month, y1)

        for year in range(y1+1, y2):
            for month in range(1, 13):
                # print(month, year)
                ov += overlap(month, year)

        for month in  range(1, m2+1):
            ov += overlap(month, y2)
            # print(month, y2)
        
    print(ov)


