# Item 1 da Lista de exercícios - Você tem uma lista de número: [6,7,4,7,8,4,2,5,7, 'hum', 'dois']. 
#A ideia do exercício é tirar a média de todos os valores contidos na lista, porém para fazer o cálculo
#precisa remover as strings.


lista = [6, 7, 4, 7, 8, 4, 2, 5, 7, 'hum', 'dois']
lista.remove('hum')
lista.remove('dois')

soma_da_lista = 0
for lista in lista:
    soma_da_lista += lista  
media_da_lista = soma_da_lista / 9
print(media_da_lista)


#Item 2 da Lista de exercícios - crie um método que receba duas matrizes, some os valores total de cada matriz e
#depois multiple o resultado delas e retorne o valor.


