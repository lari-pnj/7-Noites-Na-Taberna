import time
from funções import texto_animado
import textwrap
import os

def cap1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    print('Iniciando....', end="\n\n")
    time.sleep(2)
    
    #fala narrador
    os.system('cls' if os.name == 'nt' else 'clear')
    texto4 = """Você empurra a porta. Um aroma de vinho envelhecido,E ervas secas preenche o ar. 
    O calor do fogo estala na lareira. E apenas um velho sentado ao fundo. Parece te olhar...
    mesmo que nunca tenha o visto."""
    texto_animado(textwrap.fill(texto4))
    time.sleep(3)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    texto5 = """TABERNEIRO:-Bem vindo a ultima taberna antes do despertar.
    sete noites, sete Historias...E talvez,sete partes de você mesmo,quer beber..ou conversar primeiro?"""
    texto_animado(textwrap.fill(texto5))
    print('')
    
    #OPÇÕES:
    print("[1]➤ Me dê algo forte. Preciso esquecer")
    print("[2]➤ Prefiro conversar. Quem é aquele velho?")
    escolha3 = input("Escolha uma opção: ")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    
    if escolha3 == '1':
        print('taberneiro: coloca a taça sobre a mesa, sem pressa')
        texto6 = '-todos que chegam aqui querem esquecer...'
        texto_animado(textwrap.fill(texto6))
        texto7 = """-mas as vezes, o vinho só faz lembrar com mais nitidez."""
        texto_animado(textwrap.fill(texto7))
        texto8 = """Você bebe. O liquido é quente, amargo... e estranho. Um peso suave invade seu peito.\nO mundo parece ficar mais cento.
        O velho ao fundo continua te observando, não disse uma palavra. Mas você sente...
        ele sabe o que você quer esquecer."""
        texto_animado(textwrap.fill(texto8))
    else:
        texto9 = """TABERNEIRO:
        -Ele está aqui há mais tempo do que qualquer um se lembre.
        -nunca disse seu nome. Nunca pediu nada. Só espera.Toda noite.
         """
        texto_animado(textwrap.fill(texto9))
        print('Você sente que ja o viu..mas talvez tenha sido em um sonho...',end='\n\n')
        os.system('cls' if os.name == 'nt' else 'clear')

    print('===☽✦☾ NOITE 1-ARREPENDIMENTO ☽✦☾==='.center(50))

    texto10 = """Enquanto o vinho repousa no fundo da taça...algo muda no ar.
    Os ventos da montanha batem contra as janelas da taberna, por um instante,tudo parece suspenso
    então... A porta range.
    um novo visitante entra.
    """
    texto_animado(textwrap.fill(texto10))

    texto11 = """sua armadura está arranhada, suja, pesada. o som de metal arrastando ecoa no chão de madeira.
    Ele senta ao seu lado, pede algo com a mão e bebe. só então fala - voz rouca, pausada.
    SOLDADO:
    -lutei...
    -por algo que eu acreditei ser justo.
     """
    texto_animado(textwrap.fill(texto11))

    time.sleep(2)
    texto12 = """-E não era.
    -fiz coisas que...nem o tempo ousa tocar.
    -hoje...minha guerra é outra.carrego o peso.e caminho...tentando perdoar quem fui.
     """
    texto_animado(textwrap.fill(texto12))
    
    print('ele vira para o jogador,pela primeira vez,e olha fundo nos olhos.',end="\n\n")

    texto_animado("""E você...? - já fez algo que não da pra desfazer?""")
    print('')
    print("[1]➤ Sim.e penso nisso todos os dias.")
    print("[2]➤ Talvez..mas prefiro não lembrar.")
    print("[3]➤ Não.pelo menos,é o que eu gosto de acreditar.",end="\n\n")

    escolha3 = input('Escolha uma opção: ')
    if escolha3 == "1":
        print("""SOLDADO:olha para frente,em silêncio por alguns segundos:""")
        time.sleep(2)
        
        texto13 = """-então entende o que é carregar um peso sem alça.
              -a culpa...não desaparece.mas ás vezes,aprende a andar ao lado."""
        texto_animado(textwrap.fill(texto13))
        print("ele respira fundo.A mão treme levemente ao pegar o copo")
        time.sleep(2)
        
        texto14 = """-então entende o que é carregar um peso sem alça.
              -a culpa...não desaparece.mas ás vezes,aprende a andar ao lado."""
        texto_animado(textwrap.fill(texto14))
    elif escolha3 == "2":
        texto15 = """SOLDADO:Sem olhar para o Voce:
       -fugir da memoria é uma guerra que nunca acaba:
       -eu também tentei...por anos.
       -mas o passado tem jeito de reaparecer...mesmo no silêncio.
       """
        texto_animado(textwrap.fill(texto15))
    elif escolha3 == "3":
        texto16 = """SOLDADO: vira-se lentamente para voce,expressão dura:
       -cuidado.
       -ás vezes,a pior ilusão é a que criamos pra sobreviver.
       -mas a verdade...sempre encontra um jeito de falar com a gente."""
        texto_animado(textwrap.fill(texto16))
    else:
        print('resposta invalida') 

    texto17 = """O soldado se levanta,deixa a taça vazia sobre a mesa.
        soldado antes de sair:
       -perdão não é esquecer.
       -é lembrar...sem sangrar."""
    texto_animado(textwrap.fill(texto17))     
    
    print("ele caminha até a porta.não olha para trás. sai.o velho permanece em silêncio.",end='\n\n')

    texto18 = """O silêncio retorna.mas algo mudou dentro de voce,
    oque fazer com os erros que não podem ser corrigidos..?
    talvez a proxima noite traga mais pistas."""
    texto_animado(textwrap.fill(texto18))
    
    print('=========================FIM DA NOITE 1==================================',end='\n\n')