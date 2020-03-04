def calen():
    x=input('month:')
    flag = False
    if x in ['01','02']:
        flag  = True
    if x == '01':
        return 0,flag
    elif x == '02':
        return 3,flag
    elif x == '03':
        return 3,flag
    elif x == '04':
        return 6,flag
    elif x == '05':
        return 1,flag
    elif x == '06':
        return 4,flag
    elif x == '07':
        return 6,flag
    elif x == '08':
        return 2,flag
    elif x == '09':
        return 5,flag
    elif x == '10':
        return 0,flag
    elif x == '11':
        return 3,flag
    elif x == '12':
        return 5,flag