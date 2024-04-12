# identação e blocos
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa")

    print("obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo = valor


sacar(1000)

# estruturas condicionais (permitem o desvio de fluxo de controle, quando deteminadas expressões lógicas são atendidas)
# if / elif / else
# exemplo caixa banco
opcao = int(input(
    "****Caixa Banco**** SA\n    [1] Sacar\n    [2] Extrato\nDigite uma das opções acima:"))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
elif opcao == 2:
    print("Exibindo o extrato... ")
else:
    sys.exit("Opção inválida")

# exemplo com idade
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")

# exemplo conta
conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente.")

# if ternário (usado em verificações simples)
saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao relizar o saque!")

# estruturas de repetição
# for (usado quando tem um número fixo de vezes em que será executado)

# exemplo usando um iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper in VOGAIS:
        print(letra, end="")
else:
    print()

# exemplo usando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")

# comando while (usado quando NÃO tem um número fixo de vezes em que será executado)
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, tenha um bom dia!")

# comando break
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):

    if numero == 10:
        break

    print(numero, end=" ")

# continue é usado para pular a execução
for numero in range(100):

    if numero == 12:
        continue

    print(numero, end=" ")

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
