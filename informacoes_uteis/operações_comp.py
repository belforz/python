# AND em comparações boolianas retorna um atributo como falso por mais que um seja somente verdadeiro, entre comparações
# OR em comparaçoes boolianas retorna um atributo como verdadeiro por mais que seja exista falsos, entre comparações

limite = 100
saque = 150
conta_especial = True

x = not (limite>=saque and conta_especial >=saque)
print(x)

limite = 1250
saque = 1000
conta_especial = True
cheque_especial = 1500

y = (limite<= saque and saque<=cheque_especial) or (conta_especial==True)
print(y)

x1 = "Take this as a communication to your future"
x2 =  "ake" not in x1
print(x2)
        