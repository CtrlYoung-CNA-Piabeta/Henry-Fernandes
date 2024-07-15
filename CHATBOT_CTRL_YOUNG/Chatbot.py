import random

def saudacao(nome):
    frases = [
        'Fala aí, CNPJoto! Aqui é o ' + nome + '.',
        'Fala aí, borboleto! Aqui é o ' + nome + '.',
        'Olá! Me chamo' + nome + '. Em que posso ajudar?'
    ]
    return(frases[random.randint(0,2)])

def recebe_mensagem():
    msg = "Cliente: " + input("Cliente: ")
    proibidoes = ['vasco', 'bocó', 'bobão']
    for palavra in proibidoes:
        if palavra in msg:
            print("Tô namoral contigo! Me respeita!")
            return recebe_mensagem()
    return msg

def busca_mensagem(nome, mensagem):
    with open('base.txt', 'a+', encoding='utf-8') as base_conhecimento:
        base_conhecimento.seek(0)
        while True:
            linha = base_conhecimento.readline()
            print(linha)
            if linha != "":
                if  mensagem.replace("Cliente: ", "") == "Tchau":
                    print(nome + base_conhecimento.readline())
                    return 'Fim'
                # string.strip -> Ex: Felipe, nos poupe
                # string.strip -> Ex: Felipe,nospoupe
                elif linha.strip() == mensagem.strip():
                    proxima_linha = base_conhecimento.readline()
                    if "Chatbot: " in proxima_linha:
                        return proxima_linha
            else:
                print('Chatbot: Sei disso não, mermão.')
                base_conhecimento.write('/n' + mensagem)
                resposta_esperada = input('O que tu esperavas?')
                base_conhecimento.write('\nChatbot: ' + resposta_esperada)
                return 'Hum...'
            
def exibe_resposta(resposta, nome):
    print(resposta.replace('Chatbot', nome))
    if resposta == 'Fim':
        return resposta
    return 'Continue'

        