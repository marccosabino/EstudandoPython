#AJUSTANDO NOME DE PRODUTOS
produto = input("Digite o nome do produto: ")  
produto_padronizado = produto.strip().lower()
print(produto_padronizado)

#FORMATANDO UMA SAUDAÇÃO
nome_cliente = input('Digite o nome do cliente: ')
cidade_cliente = input('Digite a cidade do cliente: ')
print(f'Olá, {nome_cliente}! Bem-vindo(a) ao sistema da cidade de {cidade_cliente}!')

#DECIFRANDO PISTAS COM PALAVRAS-CHAVE
texto = input("Digite a palavra-chave: ")  
primeiras = texto[:3]
ultimas = texto[-3:]
print(f"Primeiras: {primeiras}")
print(f"Últimas: {ultimas}")

#VERIFICANDO O INÍCIO E O DIM DE UMA STRING
url = input("Digite a URL para validação: ") 
if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")

#ENCONTRANDO NÚMEROS EM UM TEXTO
import re

texto = input("Digite a descrição da receita: ")  
numero = re.findall(r'\d+', texto)[0]  
print(f"O número da receita é: {numero}")

#SUBSTITUINDO PALAVRAS ESPECÍFICAS
import re

texto = input('Diigte o texto a ser revisado: ')
palavra_substituir = input('Qual palavra deseja substituir? ')
palavra_nova = input('Digite a nova palavra: ')
re.sub(r'\d', 'texto')

#VALIDANDO NOMES COM REGEX
import re

nome = input("Digite o nome do cliente para validação: ")  
if re.fullmatch(r'[A-Z][a-z]*', nome):
    print("Nome válido!")
else:
    print("Nome inválido!")

#VERIFICANDO O FORMATO DE UM CPF
import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")


