# operadores aritméticos
produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = 10 / 2 + 25 * 2 - 2 ** 2
print(x)
print(y)

# operadores de comparação
saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

# operadores de atribuição
saldo = 500
print(saldo)

saldo = 200
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo //= 2        #retorna um número do tipo float usando as duas barras
print(saldo)

saldo /= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

saldo **= 4
print(saldo)

# operadores lógicos
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# operadores de identidade (testa se os objetos ocupam o mesmo espaço na memória)
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

# operadores de associação (usado para verificar se algo está em uma determinada sequencia)
frutas = ["limao", "uva"]
curso = "Curso de Python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Python" in curso)
