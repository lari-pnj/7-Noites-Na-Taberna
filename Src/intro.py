import time
from funções import texto_animado 
from cap1 import cap1
import textwrap
import os


def introducao():
    print('')
    texto_animado('          ☽✦☾ Iniciando....  ☽✦☾ '.center(50))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    time.sleep(2)
    print('')
    
    texto1 = """-Ora, Ora...um cavaleiro solitario, No alto da montanha, á essa hora?
    O que busca, coragem...ou Respostas?"""
    texto_animado(textwrap.fill(texto1))
    
    texto2 = """Mas já que chegou até aqui...Que tal um vinho fresco, Á luz das velas da taberna? venha entre. As noites são longas... e ás vezes, falam conosco."""
    texto_animado(textwrap.fill(texto2))
    print('')
    time.sleep(2)
    
    #Jogador faz uma escolha 
    print('[1]➤ sim,claro. Que mal faria?')
    print('[2]➤ não, obrigado. Prefiro observar as colinas...por enquanto.')
    escolha = input('Escolha uma opção: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Jogador escolhe entrar no jogo
    if escolha == '1':
        print("O jogador aceita o vinho.",end='\n\n')
        cap1()
    #Jogador escolhe esperar     
    else:
        time.sleep(2)
        print('')
        print("Som do vento,talvez um sino distante",end ='\n\n')
        
        texto3 = """-Ás vezes, o silêncio nos oferece respostas... mas há perguntas que só a noite pode responder. Então,cavaleiro...vai entrar agora?"""
        texto_animado(textwrap.fill(texto3))
        print('')
        time.sleep(2)
        
    #Opcao de entrar novamente
        print('[1]➤ Entrar na taberna!')
        print('')
        segunda_escolha=input('Escolha uma opção: ')
        if segunda_escolha == '1':
            print('Voce entrou na taberna!')
            cap1()
            
    
#-----------------------------------------------FIM DA INTRODUÇÃO-----------------------------------------------------         
  