nome = "Isaque"
idade = 30
profissão = "DevSecOps"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Isaque", "idade": 30}

print("Nome: %s Idade: %s" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}")
