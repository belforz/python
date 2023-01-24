#if ternario

# é um if simples de caráter validador
saldo = 2000
saque = 2000

status = "Sucesso" if saldo >+ saque else "Falha"

print(f"{status} ao realizar o saque")


# for SEMPRE COM (START,STOP,STEP(É OPCIONAL))

for numero in range(0,100,2):
    print(numero, end=" ")

#WHILE É usada para funções em que n prevenho quantos se usam no fim
opçao= -1

while opcao != 0:
  opcao=int(input("[1] Sacando .. \n [2] Extraindo \n [3] Sair \n: "))
  
  if opcao == 1:
    print("Sacando..")
    
    elif opcao >== 2:
    print("extraindo dinheiro...")

    else:
    print("Obrigado por sacar o dinheiro")








