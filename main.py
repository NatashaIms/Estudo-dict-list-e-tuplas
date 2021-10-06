import json


# lista é uma estrutura de dados composta por itens organizados de fomra linear acessados através
# de um índice. Serve para organizar mais de um valor

# lista em dicionario
a = ['Na', 'Vi', 'Da']
b = ['1', '2', '3']

resultado = dict(zip(a, b))
print(resultado)

# lista em tupla

minhalista = [1,2,3,4]
minhatupla = tuple(minhalista)

print(minhatupla)

# lista em json
minhalista = ["disney", "netflix", "prime"]
meujson = json.dumps(minhalista)

print(meujson)

# JSON formata listas, dicionarios e tuplas

# json em dicionario

jason = '{"maca": "1", "banana": "3", "uva": "5"}'

dicionario = json.loads(jason)

print(dicionario)

# json em lista


jason = '{"maca": "1", "banana": "3", "uva": "5"}'

listjson = json.loads(jason)

print(listjson)

# json em tupla

jason = '{"maca": "1", "banana": "3", "uva": "5"}'

tuplajson = tuple(jason)

print(tuplajson)


# é uma colecao ordena por chaves e valores
# difere do resto que é por posicoes

# dicionario em lista

a = {'banana': '2', 'uva': '3', 'maça': '5'}

listofkeys = a.keys()

lista = list(listofkeys)

print(lista)

# dicionario em tupla

a = {'banana': '2', 'uva': '3', 'maça': '5'}

listaTupla = a.items()

listaTupla = list(listaTupla)

print(listaTupla)

# dicionario em json

a = {'banana': '2', 'uva': '3', 'maca': '5'}
b = json.dumps(a)

load = json.loads(b)
print(b)

# tupla servem para associar (dar nome) a um valor dentro de uma lista
# podem conter lista dentro de tuplas
# sao imutaveis ao contrario das listas
# acumulam menos espaço na memoria

# tupla em dicionario

tupla = (('valor', 'chave'), ('6', 'numero'))

resultado = dict((a, b) for a,b in tupla)
print(type(resultado))

# tupla em json

# tupla em lista

minhatupla = (('valor', 'chave'), ('6', 'numero'))

listatupla = list(minhatupla)

print(type(listatupla))