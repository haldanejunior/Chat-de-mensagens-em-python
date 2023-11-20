# biblioteca importada para utilizar funcionalidades do sistema
# nesse caso para ter acesso ao teminal
import os

#armazenar mensagens
menssagens = []

# armazena nome do usuário
nome =input("Nome: ")

# laço para repertir armazenamento e mostrar mensagens
while True:

    # limpando terminal
    os.system('cls')

    # verifica se exite mensagem armazenada
    if len(menssagens) > 0:
        for m in menssagens:
            print(m['nome'], "-", m['texto'])
    
    print("________________")

    #obtendo texto
    texto = input("mensagem:  ")
    if texto == "fim":
        break 

    # adicionando mensagem na lista

    menssagens.append({
        "nome": nome,
        "texto": texto
    })