def add_everything_up(a, b):
    try:
        c = a + b
    except:
        return str(a) + str(b)
    else:
        if isinstance(c, int) or isinstance(c, float):
            c = round(c, 3)
        return c


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))




