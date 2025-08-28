import textwrap
from funções import texto_animado
import time
import os




def cap3():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto_animado('===☽✦☾ Noite 3- LIBERDADE E ESCOLHAS ☽✦☾==='.center(50))
    time.sleep(2)
    print('')

    texto1 = """A noite está fria, Mas tranquila. Pela primeira vez, Você
    decide não entrar na taberna de imediato.
    Ele se encosta no muro de pedra, tira um cigarro do bolso e o acende.
    O som do vento é quebrado apenas pelo estalar do fumo queimando."""
    texto_animado(textwrap.fill(texto1))
    time.sleep(5)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    texto2 = """minutos depois,passos lentos se aproximam.
    um homem de aparencia pacifica se senta em uma pedra proxima
    seu olhar é sereno, mas carrega um cansaço antigo.
    algemas de ferro pendem frouxas de seus pulsos.
    ele tambem acende um cigarro."""
    texto_animado(textwrap.fill(texto2))
    time.sleep(2)
    print('')
    
    print('[1] ➤ Essas algemas...você fugiu de algum lugar?')
    print('')
    escolha = input('Escolha uma opção: ')
    print('')
    if escolha == '1':
        texto3 = """PRISIONEIRO(SORRINDO LENTAMENTE):
        - engraçado...não
        - As portas estavam abertas.eu só fui embora.
        - mas,mesmo fora,não me sinto exatamente livre"""
        texto_animado(textwrap.fill(texto3))
        time.sleep(2)
    else:
        texto4 = """Ele apenas dá de ombros, um sorriso triste se formando.
        - O silêncio também é uma resposta."""
        texto_animado(textwrap.fill(texto4))
        
    os.system('cls' if os.name == 'nt' else 'clear')
    texto5 = """ele sopra a fumaça para o céu,como quem manda um pensamento embora."""
    texto_animado(textwrap.fill(texto5))
    time.sleep(2)

    print('-Então porque ainda usa isso?')
    escolha2 = input('Escolha uma opção: ')
    if escolha2 == "1":
        texto6 = """-talvez ainda não tenha saido completamente...
        -ou talvez nunca estive preso de fato.
        -você ja teve a sensação de estar vivendo uma vida que não escolheu?
        -de seguir caminhos que outros colocarem sob seus pés...
         como se fossem seus?
        - me diga...você escolheu a vida que vive?"""
        texto_animado(textwrap.fill(texto6))
        time.sleep(2)
    else:
        texto7 = """-O silêncio também é uma resposta."""
        texto_animado(textwrap.fill(texto7))
        time.sleep(2)
        
    print("[1] ➤ sim.cada passo que dei foi por vontade propria.                ".center(50)) 
    print("[2] ➤ não sei,As vezes sinto que só fui levando pelos acontecimentos.".center(50)) 
    print("[3] ➤ não.mas ainda tenho tempo de escolher deferente.               ".center(50)) 
    print('')
    escolha3 = input('Escolha uma opção: ')  
    if escolha3 == "1":
        texto6 = """-Hm...talvez você seja mais livre do que a maioria.
        mas mesmo escolhas livres carregam consequencias.
        você estaria disposto a perder tudo pelo caminho que escolheu?"""
        texto_animado(textwrap.fill(texto6))
    elif escolha3 == "2":
        texto7 = """-muitos vivem assim...e morrem sem perceber.o conforto
        da corrente invisivel é que ela não aperta.
        só quando tentamos nos mover é que ela dói.""" 
        texto_animado(textwrap.fill(texto7)) 
    elif escolha3 == "3":
        texto8 = """-Então talvez haja esperança.A liberdade não começa com uma chave.
        começa com a consequencia de que estamos acorrentado""" 
        texto_animado(textwrap.fill(texto8))
        time.sleep(2)
    else:
        texto9 = """-O silêncio também é uma resposta."""
        texto_animado(textwrap.fill(texto9))
        time.sleep(2)
        
    texto01 = """NARRADOR:
    O cigarro do prisioneiro acaba.ele se levanta devagar.
    antes de ir embora,deixa algo cair no chão uma pequena chave.
    -ela não abre nenhuma porta.mas pode lembrar você de que pode tentar.
    Ao lado da porta da taberna,algo escrito
    "Liberdade sem conciencia é só uma cela com vista para o mar"""
    texto_animado(textwrap.fill(texto01))
    time.sleep(5)





  
  
if __name__ == "__main__":
    cap3()