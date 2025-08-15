import time
import sys

#Função para texto animado
def texto_animado(texto):
   for letra in texto:
      print(letra, end='')
      sys.stdout.flush()
      time.sleep(0.1)
   print()  

#Função para menu
def menu():
    texto_animado('=== Bem-vindo a 7 noites na taberna ===')
    print('1. Iniciar jogo')
    print('2. Creditos')
    print('3. Sair')

#Função principal para escolha de opções
def main():
    while True:
     menu() 
     escolha = input('Escolha uma opcao: ') 
     if escolha == '1':
        iniciar_jogo()
     elif escolha == '2':
        creditos()
     elif escolha =='3':
        texto_animado('saindo do jogo...') 
        time.sleep(2) 
        break
     else:
        print('Opção invalida,tente novamente')  
        time.sleep(2)

#Função para iniciar o jogo
def iniciar_jogo():
   print('Carregando jogo...')
   time.sleep(5)

#Função para créditos
def creditos():
   texto_animado('=== Créditos ===')
   texto_animado('Criado por Larissa valeriano.')
   texto_animado('2025')
   texto_animado('Obrigado por jogar!')
   time.sleep(5)

if __name__ == '__main__':
   main()    