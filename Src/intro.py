import time
from funções import texto_animado, limpar_tela
from cap1 import cap1
import textwrap
import os


    
#funcao exibe as opcoes de escolha na tela-------------------

def opcao():
    opcoes =['[1]➤ sim,claro. Que mal faria?', '[2]➤ não, obrigado. Prefiro observar as colinas...por enquanto.']
    for linha in opcoes:
        print(linha)
    print('')  
    
#funcao para a escolha do jogador-------------------------------

def escolha1():
    while True: 
     opcao()
     escolha = input('Escolha uma opção: ').strip()    
                    
     if escolha == '1':
        print("\nO jogador aceita o vinho.\n")
        cap1()   
        break
    
     elif escolha == '2':
        time.sleep(2)
        limpar_tela()
        texto_animado("Som do vento,talvez um sino distante\n")
        
        texto3 = """-Ás vezes, o silêncio nos oferece respostas... mas há perguntas que só a noite pode responder. Então, cavaleiro...vai entrar agora?"""
        texto_animado(textwrap.fill(texto3))
        print('')
        time.sleep(2)
        
     #loop para segunda opcao--------------------------
        while True:
         print('[1] ➤  Entrar na taberna!')
         print('')
         segunda_escolha=input('Escolha uma opção: ').strip()
         if segunda_escolha == '1':
            print('\nVoce entrou na taberna!\n')
            cap1() 
            return
         else:
            print('Opção invalida, tente novamente')  
            time.sleep(2)  
     else:
         print('opção invalida, tente novamente!')
         time.sleep(2)
        

#funcao principal para iniciar o jogo ----------------------------------------

def introducao():
    limpar_tela()
    texto_animado('☽✦☾ Iniciando....  ☽✦☾ '.center(90))
    limpar_tela()
    print('')
    texto1 = """-Ora, Ora...um cavaleiro solitario, No alto da montanha, á essa hora? O que busca, coragem...ou Respostas?"""
    for linha in texto1.splitlines():
        texto_animado(textwrap.fill(linha.center(90)))
    print('')
    time.sleep(3)    
    
    limpar_tela()
    texto2 = """Mas já que chegou até aqui...Que tal um vinho fresco, Á luz das velas da taberna? venha entre. As noites são longas... e ás vezes, falam conosco."""
    for linha in texto2.splitlines():
        texto_animado(textwrap.fill(linha.center(90)))
    print('')
    time.sleep(2)
    escolha1()
    

     
if __name__ == '__main__':
    introducao()            
            
    
#-----------------------------------------------FIM DA INTRODUÇÃO-----------------------------------------------------         
  