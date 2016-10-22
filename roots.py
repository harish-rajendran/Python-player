#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Admin
#
# Created:     24-06-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import cmath

    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0} and {1}'.format(sol1,sol2))
    list1=[1,2,3]
    list2=2*list1
    list3=list1 + list2
    print(max(list3))


if __name__ == '__main__':
    main()
