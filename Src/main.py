import time
import os 
from intro import introducao
from funções import texto_animado


#Função para menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    texto_animado('=== Bem-vindo a 7 noites na taberna ===')
    print('')
    print('1. Iniciar jogo')
    print('2. Creditos')
    texto_animado('3. Sair')

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
        texto_animado('saindo do jogo...') 
        time.sleep(2) 
        break
     else:
        print('Opção invalida, tente novamente')  
        time.sleep(2)
   

#Função para créditos
def creditos():
   texto_animado('=== Créditos ===')
   texto_animado('Criado por Larissa valeriano.')
   texto_animado('2025')
   texto_animado('Obrigado por jogar!')
   time.sleep(5)

if __name__ == '__main__':
   main()    