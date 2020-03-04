import l2nyear
import month
import year
date=int(input('Date is:'))
month,flag=month.calen()
year,leap=year.calen()
num=l2nyear.calen()
y=date+month+year+num+num//4
# print(leap,flag)
if leap and flag:
    y -= 1
x = y % 7
def calen():

    if x == 0:
        return 'Sunday'
    elif x == 1:
        return 'Monday'
    elif x == 2:
        return 'Tuesday'
    elif x == 3:
        return 'Wednesday'
    elif x == 4:
        return 'Thrusday'
    elif x == 5:
        return 'Friday'
    elif x == 6:
        return 'Saturday'
calen()
print(calen())
