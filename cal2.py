array=[]
def isLeapYear(year):
    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
        return 1
    else:
        return 0

def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)

def initialize():
    global array
    count=0
    for i in range(400):
        year=i
        if isLeapYear(year):
            if dayofweek(1,2,year)==6:
                count+=1
        else:
            if dayofweek(1,2,year)==0 or dayofweek(1,2,year)==6 :
                count+=1
   
        array.append(count)



t = int(input())
initialize()

for __ in range(t):
    m1,y1 = map(int,input().split(' '))
    m2,y2 = map(int,input().split(' '))
   

    count=0
    if y1==y2:
        if m1<=2 and m2>=2:
            if isLeapYear(y1):
                if dayofweek(1,2,y1)==6:
                    count+=1
            else:
                if dayofweek(1,2,y1)==0 or dayofweek(1,2,y1)==6 :
                    count+=1
            print(count)
        else:
            print("0")
    else:
        if m1<=2:
            y1-=1
        if m2<2:
            y2-=1
        res1=y1%400
        temp1=101*int(y1/400)
        res2=y2%400
        temp2=101*int(y2/400)


        print((array[res2]+temp2)-(array[res1]+temp1))