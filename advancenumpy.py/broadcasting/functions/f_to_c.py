def f_to_c(f):
    return 5*(f-32)/9
f = int(input('enter the temp in f '))
c = f_to_c
print(f'{round(c,2)}c')