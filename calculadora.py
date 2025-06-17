def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    # Solicita os números ao usuário
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    # Realiza as operações matemáticas
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    
    # Tratamento para divisão por zero
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero"

    # Exibe os resultados das operações
    print("\nResultados das operações:")
    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
    print(f"Divisão: {num1} / {num2} = {divisao}")

    # Análise do primeiro número
    print(f"\nAnálise do primeiro número ({num1}):")
    print(f"É {'par' if num1 % 2 == 0 else 'ímpar'}")
    print(f"É {'primo' if eh_primo(num1) else 'não é primo'}")

    # Análise do segundo número
    print(f"\nAnálise do segundo número ({num2}):")
    print(f"É {'par' if num2 % 2 == 0 else 'ímpar'}")
    print(f"É {'primo' if eh_primo(num2) else 'não é primo'}")

if __name__ == "__main__":
    main() 