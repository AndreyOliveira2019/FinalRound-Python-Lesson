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



#ITEM 3 Criar uma matriz nxm (n = 5, m =7)

import numpy as np

a = np.array([(2, 2, 3, 3, 4, 4, 5),(2, 2, 3, 3, 4, 4, 5),(2, 2, 3, 3, 4, 4, 5),(2, 2, 3, 3, 4, 4, 5),(2, 2, 3, 3, 4, 4, 5)]) 
print(a)



#ITEM 3a Faça a Matriz Transposta desta matriz:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 

a.transpose()



#ITEM 3b - Somar toda a matriz:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 


a.sum()


#ITEM 3c - Somar todas as colunas:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 


a.sum(axis=0)



#ITEM 3d - Somar todas as linhas:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 


a.sum(axis=1)

#ITEM 3e - Retorne o maior valor:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 


a.max()

#ITEM 3f - Retorne o menor valor:

import numpy as np

a = np.array([(1, 2, 3, 4, 5, 6, 7),(8, 9, 10, 11, 12, 13, 14),(15, 16, 17, 18, 19, 20, 21),(22, 23, 24, 25, 26, 27, 28),(29, 30, 31, 32, 33, 34, 35)]) 


a.min()


#ITEM 4 - Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.

#ENGRAÇADÃO HEIN PROFESSOR KKKKK (Eu puto depois de duas horas procurando como somar :( )


#ITEM 5 - crie um array de números que vai de 0 a 1000:
a = np.arange(1001)
print(a)


#ITEM 6 - crie uma matriz só de zeros:
a = np.array([(0, 0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0, 0)])
print(a)




