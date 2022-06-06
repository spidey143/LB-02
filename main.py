from math import*


if __name__ == '__main__':
    print('Для решения уравнения ax^2+bx+c=0')
    a=float(input('введите коэффицинет a: '))
    b=float(input('введите коэффицинет b: '))
    c=float(input('введите коэффицинет c: '))
    D=b**2-4*a*c
    print('D=',D,sep='')
    if D>0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        print('X1=',x1,'\nX2=',x2,sep='')
    elif D==0:
        x=(-b) / (2 * a)
        print('X=',x,sep='')
    else:
        print('корней нет')
