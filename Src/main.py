import time
import os 
from intro import introducao
from funções import texto_animado


#Função para menu
def menu():
    os.system('cls')  # Limpa a tela
    titulo = ("""                                                                           
      _____               _ _                             _        _                           
     |___  |  _ __   ___ (_) |_ ___  ___    _ __   __ _  | |_ __ _| |__   ___ _ __ _ __   __ _ 
        / /  | '_ \ / _ \| | __/ _ \/ __|  | '_ \ / _` | | __/ _` | '_ \ / _ \ '__| '_ \ / _` |
       / /   | | | | (_) | | ||  __/\__ \  | | | | (_| | | || (_| | |_) |  __/ |  | | | | (_| |
      /_/    |_| |_|\___/|_|\__\___||___/  |_| |_|\__,_|  \__\__,_|_.__/ \___|_|  |_| |_|\__,_|
      """)
    print(titulo)
    print('========='*11)  
    print('')  

    opcoes = ['[1] ➤  Iniciar jogo', '[2] ➤  Creditos', '[3] ➤  Sair']
    for linha in opcoes:
        print(linha.center(90))
    print('')     

#Função principal para escolha de opções
def main():
    while True:
     menu() 
     escolha = input('Escolha uma opcao: ')
     if escolha == '1':
        
        introducao() # Aqui chama a introdução do jogo
        break
     elif escolha == '2':
        creditos()
     elif escolha =='3':
        os.system('cls')
        texto_animado('saindo do jogo...') 
        time.sleep(4) 
        break
     else:
        print('Opção invalida, tente novamente')  
        time.sleep(2) 
   
#Função para créditos
def creditos():
    os.system('cls')
    print('''Créditos do jogo''')





if __name__ == '__main__':
   main()    