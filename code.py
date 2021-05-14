# Item 1 da Lista de exercícios - Você tem uma lista de número: [6,7,4,7,8,4,2,5,7, 'hum', 'dois']. 
#A ideia do exercício é tirar a média de todos os valores contidos na lista, porém para fazer o cálculo
#precisa remover as strings.


lista = [6, 7, 4, 7, 8, 4, 2, 5, 7, 'hum', 'dois']
lista.remove('hum')
lista.remove('dois')

soma_da_lista = 0
for lista in lista:
    soma_da_lista += lista  
media_da_lista = soma_da_lista / 11
print(media_da_lista)


#Item 2 da Lista de exercícios - crie um método que receba duas matrizes, some os valores total de cada matriz e
#depois multiple o resultado delas e retorne o valor.

def lista(primeiramatriz, segundamatriz):

  resultado1 = 0
  resultado2 = 0
  resultado3 = 0

  for linha in primeiramatriz: 
    for coluna in linha: 
      resultado1 = coluna + resultado1

  for linha2 in segundamatriz: 
    for coluna in linha2:
      resultado2 = coluna + resultado2

  print('exibir resultado da soma da primeiramatriz:', resultado1)
  print('exibir resultado da soma da segundamatriz:', resultado2)

  resultado3 = resultado1 * resultado2
  print('exibir resultado da multiplicação das duas matrizes:', resultado3)
    
  
  primeiramatriz = [[1,2,3],[1,2,3]]
  segundamatriz = [[1,2,3],[10,20,30]]

lista(primeiramatriz, segundamatriz)

#Criar uma matriz nxm (n = 5, m =7)




