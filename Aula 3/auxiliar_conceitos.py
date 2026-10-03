#Como criar listas
nomes = ['Ana', 'Joana', 'Guilheme']
#Pegar itens da lista
#Os itens começam a contar a partir de 0
primeiro = nomes[0] #Pegamos um item a partir do índice
print(primeiro)
#Adicionar itens
nomes.append('Rafael') #Adiciona no final
print(nomes)

#Dicionários
#Ótimo para pegar vários tipos de informações
pessoa = {'nome': 'Eliana', 'idade': '22', 'cidade': 'Açailândia'} #'chave': 'valor'
idade = pessoa['idade']
print(idade)

#Como usar
lista_mensagem = []
mensagem1 = {'role':'user', 'content':'mensagem do usuario'} #role - quem enviou, content - conteudo
mensagem2 = {'role':'assistant', 'content':'mensagem da ia'}

lista_mensagem.append(mensagem1)
lista_mensagem.append(mensagem2)
