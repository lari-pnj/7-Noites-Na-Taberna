import time
import os 
from intro import introducao
from funções import texto_animado


#Função para menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print('~=~=~='*20)
    texto_animado('=~=~=~=~=~= ☽✦☾ Bem-vindo a 7 noites na taberna ☽✦☾~=~=~==~=~='.center(60))
    print('~=~=~='*20)
    print('[1] ➤ Iniciar jogo'.center(50))
    print('[2] ➤ Creditos    '.center(50))
    print('[3] ➤ Sair        '.center(50))
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
        texto_animado('saindo do jogo...') 
        time.sleep(2) 
        break
     else:
        print('Opção invalida, tente novamente')  
        time.sleep(2)
   

#Função para créditos
def creditos():
   os.system('cls' if os.name == 'nt' else 'clear')
   texto_animado('=== ☽✦☾  Créditos  ☽✦☾  ==='.center(50))
   print('')
   print("""Criado por:Larissa valeriano.""".center(50))
   print('            Contatos:             '.center(50))
   print('github:https://github.com/lari-pnj'.center(50))
   print('Email:Larissavaleriano36@gmail.com'.center(50))
   print('Obrigado por jogar!               '.center(50))
   time.sleep(15)

if __name__ == '__main__':
   main()    