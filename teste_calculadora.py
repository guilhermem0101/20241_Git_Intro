import calculadora 
def main():
    a = 2
    b = 3
    soma = calculadora.somar(a, b)
    print(f'(a) + (b) = (soma)')
    subtrair = calculadora.subtrair(a, b)
    print(f'(a) - (b) = (subtrair)')
    produto = calculadora.multiplicar(a, b)
    print(f' (a) * (b) = (produto)')
    quociente = calculadora.divisao(a, b)
    print(f' (a) / (b) = (produto)')
main()    