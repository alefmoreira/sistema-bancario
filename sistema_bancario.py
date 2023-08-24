#Sistema bancario utilizando conhecimentos na Formação Python Devloper da plataforma Dio

saldo = 0
limite = 500 
extrato = ""
numeros_saques = 0  
LIMITE_SAQUES = 3

menu ="""
==========OPERAÇÃO BANCARIA==========
                          
Digite a opcao que voce deseja:                   
[1] DEPOSITO
[2] SAQUE  
[3]EXTRATO 
[0]SAIR 
            
=====================================

>>> """

while True:  
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = float(input("Digite o valor do deposito:"))
        
        if valor <=0:
            print("O valor dever ser maior do que R$ 0,00")
        
        else:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
                
    elif opcao == 2:
        valor = float(input("Digite o Valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        
        
        if excedeu_saldo:
            print(f"o valor é maior que o saldo disponivel, seu saldo é {saldo}")
        
        elif excedeu_limite:
            print(f"limite de saque excedido, tente novamente com um valor inferior à {limite}")    
        
        elif excedeu_saques:
            print("limites de saque excedido!")
        
        elif valor> 0:
            saldo += valor
            extrato += f"SAQUE: {valor:.2f}\n"
            numeros_saques += 1 
        else:
            print("VALOR INVALIDO!")    
    elif opcao == 3:
        print("===============EXTRATO===============")
        print("Nenhuma movimentação foi realizada" if not extrato else extrato)
        print(f"Seu saldo é de: R${saldo:.2f}\n")
        print("=====================================")
    elif opcao == 0: 
        print("Obrigado por ser noso cliente!")
        break
    else:
        print('Operação inválida, por favor digite uma opção válida.')



