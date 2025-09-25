import sys
import time
import os

#função para texto animado
def texto_animado(texto):
   for letra in texto:
      print(letra, end='')
      sys.stdout.flush()
      time.sleep(0.1)
   print()
   
# funcao para limpar a tela
def limpar_tela():
   os.system('cls' if os.name == 'nt' else 'clear')   
   
#funcao menu de opções   

def mostrar_opcoes(opcoes):
    for opcao in opcoes:
     print(opcao)
    print('')
    
#Função respostas    
def perguntar_opcao(pergunta, opcoes_validas):
    while True:
        escolha = input(pergunta).strip()  
        if escolha in opcoes_validas:
            return escolha
        print('Opção invalida, Tente novamente!')
      
        
#Função de pausa
def pausa(segundos=2):
    time.sleep(segundos)       
         