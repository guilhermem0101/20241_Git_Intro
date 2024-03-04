import calculadora

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 para Somar")
        print("0 para Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calculadora.somar(a, b))
            
        elif opcao == '0':
            print("Saindo...")
            break
