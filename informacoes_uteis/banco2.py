menu = """
[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=>"""
account_balance = 500
limit = 500
extract =""
number_saques = 0
LIMIT_SAQUE= 3

while True:
    option = input(menu)

    if option =="a":
        value = float(input("Mostre o valor do depósito: "))
        
        if value > 0:
            account_balance += value
            extract += f"Depósito: R${value:.2f}\n"
            

        else:
            print("Operação falhou! O valor informado é inválido")

    elif option == "b":
         value1 = float(input("informe o valor do saque: "))
         execed_account_balance = value1 > account_balance
         exced_limit = value1 > limit
         execed_saque = number_saques >= LIMIT_SAQUE
    
         if execed_account_balance:
            print("Operação não terminada! Não há saldo suficiente ")
            if exced_limit:
                print("Operação não terminada ! O valor do saque excede o limite diário.")
            elif execed_saque:
                print("Operação não terminada ! Numero máximo de saques atendido por hoje.")
            elif value1 > 0:
                account_balance -= value1
                extract += f"Saque: R${value1:.2f}\n"
                number_saques += 1
            else:
                print("Operação não terminada ! O valor informado é inválido.,")
    elif option == "c":
        print("Extrato")
        print("Não foram realizados movimentações:" if not extract else extract)
        print(f"\n Saldo: R$:{account_balance:.2f}")
    

    elif option =="d":   
        break

    else:
        print("Esta opção não existe")
