def calen():
    x=int(input('year:'))
    leap = False
    if x % 100 == 0 and x % 400 == 0:
        leap = True
    elif x % 100 != 0 and x % 4 == 0:
        leap = True

    if x>=1600 and x<=1699:
        return 6,leap
    elif x>=1700 and x<=1799 :
        return 4,leap
    elif x>=1800 and x<=1899:
        return 2,leap
    elif x>=1900 and x<=1999:
        return 0,leap
    elif x>=2000 and x<=2099:
        return 6,leap