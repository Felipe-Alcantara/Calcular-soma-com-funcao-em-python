mensagem = 'olá mundo'
print(mensagem)


def calcular_soma(a, b):
    soma = a + b
    return soma


while True:
    try:
        numero1 = float(input('Digite um número: '))
        break  # Se a conversão para inteiro for bem-sucedida, sai do loop
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

while True:
    try:
        numero2 = float(input('Digite outro número: '))
        break  # Se a conversão para inteiro for bem-sucedida, sai do loop
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

print('"', calcular_soma(numero1, numero2), '"')

resultado = calcular_soma(numero1, numero2)
print('A soma destes dois números é: ', resultado)
print('Obrigado')
print('By: Felixo')
