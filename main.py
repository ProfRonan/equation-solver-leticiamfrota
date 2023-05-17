grau = int(input()) 
if grau < 1 or grau > 2:
    print('Grau inválido')
if grau == 1:
    print('A equação é do primeiro grau')
    a = float(input())
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        x = -b/a
        print(f'{x:.2f}')
if grau == 2:
    print('A equação é do segundo grau')
    a = float(input())
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        c = float(input())
        delta = (b**2)-4*a*c
        if delta < 0:
            print('A equação não possui raízes reais')
        if delta == 0:
            print('A equação possui uma raiz real')
            x = (-b + (delta**0.5))/2*a
            print(f'{x:.2f}')
        if delta > 0:
            print('A equação possui duas raízes reais')
            x1 = (-b - (delta**0.5))/2*a
            x2 = (-b + (delta**0.5))/2*a
            print(f'{x1:.2f}', f'{x2:.2f}')

