import sys
import time
import os


#Função para texto animado
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

def menu(opcoes):
    while True:
        limpar_tela()
        for i, opcao in enumerate(opcoes, start=1):
            print(f"[{i}] ➤ {opcao}")
        print("")
        
        escolha = input("Escolha uma opção: ").strip()
        
        # verifica se a escolha é um número válido
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return escolha  # retorna sempre como string
        else:
            print("Opção inválida, tente novamente.")
            time.sleep(2)