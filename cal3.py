def dow(date, month, year):
    temp  = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
    year -= month < 3
    return (year + (year // 4) - (year // 100) + (year // 400) + temp[month - 1] + date) % 7

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


def create():
    look = []
    cnt = 0
    for yr in range(400):
        l = is_leap(yr)
        dw = dow(1, 2, yr)
        cnt += 1 if((l and dw == 6) or ((not l) and (dw == 0 or dw == 6))) else 0
        look.append(cnt)
    return look

look_up = create()

t = int(input())

for _ in range(t):

    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())

    count = 0
    if y1 == y2:
        if m1 <= 2 and m2 >= 2:
            l = is_leap(y1)
            dw = dow(1, 2, y1)
            count += 1 if((l and dw == 6) or ((not l) and (dw == 0 or dw == 6))) else 0
            print(count)
        else:
            print(0)
    else:
        if m1 <= 2:
            y1 -= 1
        if m2 < 2:
            y2 -= 1
        
        p1 = y1 % 400
        p2 = y2 % 400
        t1 = 101 * (y1 // 400)
        t2 = 101 * (y2 // 400)


        print((look_up[p2] + t2) - (look_up[p1] + t1))

