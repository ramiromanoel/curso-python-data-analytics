capacidade_atual, aumento_percentual = map(int, input().split())

# Calcule a nova capacidade do disco de Mithril
# Imprima a nova capacidade

# Calcula a nova capacidade total
nova_capacidade_total = capacidade_atual * (1 + aumento_percentual / 100)

# Exibe o resultado
print(int(nova_capacidade_total))
