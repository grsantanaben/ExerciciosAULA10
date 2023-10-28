#AULA10
#Exercício 1: Escreva uma função que calcule a soma dos números de 1 a N, onde N é um número inteiro dado.

def test(N):
  soma = 0
  for i in range (1, N+1):
    soma = soma + i
  print(soma)

test(5)

#Exercício 2: Escreva uma função que conte quantas vezes uma letra específica aparece em uma palavra.

def contar(palavra,letra):
  c = 0
  for char in palavra:
   if char == letra:
    c = c + 1
  print(c)
contar('Gabriel', 'a')

#Exercício 3: Escreva uma função que calcule o fatorial de um número inteiro não negativo N.
def fat(N):
  if N == 0:
     return 1
  result = 1
  for i in range(1, N + 1):
    result *=  i
  print(result)
fat(5)

#Exercício 4: Crie um Dicionário, adicione elementos ao dicionário e os mostre na tela. dicionario = {}

dict = {}
dict ['chave 1'] = 'valor1'
dict ['chave 2'] = 'valor2'
dict ['chave 3'] = 'valor3'
dict ['chave 4'] = 'valor4'
print (dict)

#Exercício 5: Utilizando Dicionários, que peça para o usuário inserir o nome de três produtos # de mercado e seus respectivos preços e os mostre na tela.

produtos = {}

for i in range(2):
 nome_produto = input('Qual o produto: ' ) 
 preco_produto = float(input('Preco do produto: ' ))
 produtos[nome_produto] = preco_produto
  
print('Lista de produtos')

for produtos, preco in produtos.items():
 print (f'{produtos}: R${preco}')
