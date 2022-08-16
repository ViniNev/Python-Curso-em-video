import math
ang = float(input('Digite o angulo para saber o seno, cosseno e tangente: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Com o angulo de {:.2f}º, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, seno, cose, tang))