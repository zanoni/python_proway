A = int(input('Primeiro valor: '))
B = int(input('Segundo valor: '))
C = int(input('Terceiro valor: '))

val = [A, B, C]

val.sort()

if val[2] < (val[0] + val[1]):
    print('Os lados formam um triângulo')   
else :
    print('Os lados não formam um triângulo')   

