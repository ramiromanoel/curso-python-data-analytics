"""
# maiúscula, minúscula, e título
curso_1 = "pYtHon"

print(curso_1.upper())
print(curso_1.lower())
print(curso_1.title())

# eliminando espaços em branco
curso_2 = "    Python  "

print(curso_2.strip())
print(curso_2.lstrip())
print(curso_2.rstrip())

# junções e centralizações
curso_3 = "Python"

print(curso_3.center(10, "#")) # centraliza de acordo com a qtd de carateres definido e tbm pode receber um carectere para preencher estes espaços
print(".".join(curso_3)) # 

# interpolação de variáveis
nome = "Ramiro"
idade = 27
profissao = "Analista de dados"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Ramiro", "idade": 27}

print("Nome: %s, Idade: %s" % (nome, idade))
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {1}, Idade: {0}".format(idade, nome))
print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name}, Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome}, Idade: {idade}".format(**dados))
print(f"Nome: {nome}, Idade: {idade}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.2f}")

# fatiamento de strings ([start:stop:step])
nome = "Ramiro Manoel dos Santos Junior"

print(nome[0])
print(nome[-1])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1]) # espelhamento da string
"""
# string múltiplas linhas
# strings triplas
nome = "Ramiro"

mensagem = f"""
        Olá meu nome é {nome},
Eu estou aprendendo Python.
            Essa mensagem tem diferentes recuos.
"""

print(mensagem)

print("""
    ============== MENU ==============
    
      1 - Depositar
      2 - Sacar
      0 - Sair
    
    ==================================
      
    Obrigado por usar nosso sistema!
""")