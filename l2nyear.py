def calen():
    a = int(input('Year:'))
    a_string = str(a)
    a_length = len(a_string)
    c = int(a_string[a_length - 2: a_length])
    return c