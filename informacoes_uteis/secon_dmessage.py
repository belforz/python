
p = input('Primeiro valor:')
q = input('Segundo valor:')
r = input('Terceiro Valor:')

if p> q and p > r:
    print(' o maior número é {}'.format(p))
elif q > p and q > r:
    print('o maior numero é {}'.format(q))
else :
    print(' o maior numéro é {}'.format(r))

a = int(input('Digite uma nota'))
if a >= 10:
     a= int(input('Voce digitou errado, tente novamente: '))
b = int(input('Digite uma nota'))
if b >= 10:
    b= int(input('Voce digitou errado, tente novamente: '))
c = int(input('Digite uma nota'))
if c >= 10:
     c= int(input('Voce digitou errado, tente novamente: '))

media =int (a + b + c) / 4
print('Sua média no semestre foi: {}' .format(media))