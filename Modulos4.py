import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float (input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa equivale á {h:.2f}')
