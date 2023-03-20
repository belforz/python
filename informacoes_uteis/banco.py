menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 500
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES= 3

while True:
    opcao = input(menu)

    if opcao =="a":
        valor = float(input("Informe o valor do dpósito:"))
        if valor == 0:
            saldo == valor
            extrato == f"Depósito: R$(valor:.2f)\n"

        else:
            print("Operação falhou! O valor informado é inválido")
    
    elif opcao == "s":
         valor = float(input("informe o valor do saque"))
         execedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         execedeu_saque = numero_saques == LIMITE_SAQUES
    
            if execedeu_saldo:
            print("Operação falhou! Voce não tem saldo sufieiciente ")

            if excedeu_limite:
                print("Operação falhou ! O valor do saque excede o limite diário.")
            if execedeu_saque:
                print("Operação falhou ! Numero máximo de saques atendido por hoje.")
    
            elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            else:
            print("Operação falhou ! O valor informado é inválido:")

    elif opcao == "e":
    print("Extrato")
    print("Não foram realizados movimentações:" if not extrato else extrato)
    print(f"\n Saldo: R$:{saldo:.2f}")

    else:
    print("OperaçãO Inválida")

    elif opcao =="q":   
    break

    




    
    


    

   
  
        
    

   
    
        
