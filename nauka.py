import math

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


while True:
    a = input('enter value a: ')
    b = input('enter value b: ')
    c = input('enter value c: ')

    if a.isdecimal() and b.isdecimal() and c.isdecimal():
        a_int = int(a)
        b_int = int(b)
        c_int = int(c)

        if a_int == 0:
            print('error value')
            break
        elif a_int !=0:
            delta = (b_int**2)-(4*a_int*c_int)
            print('delta result: %d ' %(delta))

            if delta < 0:
                print('this equation has not solution')
                break
            elif delta > 0:
                x1 = (-b_int - math.sqrt(delta) / 2*a_int)
                x2 = (-b_int + math.sqrt(delta) / 2*a_int)
                print('x1 result: %d' %(x1))
                print('x2 result: %d' % (x2))
                break
            elif delta == 0:
                x1 = (-b_int - math.sqrt(delta) / 2 * a_int)
                print('x1 result: %d' % (x1))
                break
    else:
        print('every value must be an number')
        continue