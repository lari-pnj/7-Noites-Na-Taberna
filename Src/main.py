import time
import os 
from intro import introducao
from funções import texto_animado



#função par limpar a tela do terminal
def limpar_tela():
   os.system('cls' if os.name == 'nt' else 'clear')


#Função para menu
def menu():
    limpar_tela()
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
        limpar_tela()
        texto_animado('saindo do jogo...') 
        time.sleep(4) 
        break
     else:
        print('Opção invalida, tente novamente')  
        time.sleep(2) 
   
#Função para créditos
def creditos():
   limpar_tela()
   titulo_creditos = '''' 
      __  ____     ___  ___    ____  ______   ___   _____
     /  ]|    \   /  _]|   \  |    ||      | /   \ / ___/
    /  / |  D  ) /  [_ |    \  |  | |      ||     (   \_ 
   /  /  |    / |    _]|  D  | |  | |_|  |_||  O  |\__  |
  /   \_ |    \ |   [_ |     | |  |   |  |  |     |/  \ |
  \     ||  .  \|     ||     | |  |   |  |  |     |\    |
   \____||__|\_||_____||_____||____|  |__|   \___/  \___|
                                                            '''
   for linha in titulo_creditos.splitlines():
       print(linha.center(90))
   print('')
   
   creditos = [
    '- Desenvolvedor: Larissa Valleriano',
    '- Música: ****',
    '- Imagens: *****',
    '- Contatos: ',
    '- Github: https://github.com/lari-pnj',
    '- Email: Larissavaleriano36@gmail.com'
   ]
   for i in creditos:
       print(i.center(90))
   print('')    
   input('Pressione Enter para voltar ao menu principal...')

if __name__ == '__main__':
   main()    