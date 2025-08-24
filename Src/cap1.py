import time
from funções import texto_animado

def cap1():
    
    print('Iniciando....')
    time.sleep(2)
    #fala narrador
    texto_animado("""
Você empurra a porta. Um aroma de vinho envelhecido, madeira na lareira. E ervas secas preenche o ar. 
O calor do fogo estala na lareira. E apenas um velho sentado ao fundo. Parece te olhar...
mesmo que nunca tenha o visto.""")
    
    time.sleep(2)
    #fala taberneiro
    texto_animado("""TABERNEIRO:
-Bem vindo a ultima taberna antes do despertar.
 sete noites, sete Historias...E talvez,sete partes de você mesmo,quer beber..ou conversar primeiro?""",end='\n\n')
    print('===='*20)
    #OPÇÕES:
    print("1-Me dê algo forte. Preciso esquecer")
    print("2-Prefiro conversar. Quem é aquele velho?")
    escolha3 = input("Escolha uma opção: ")
    if escolha3 == '1':
        print("-",end='\n\n')
        print('taberneiro: coloca a taça sobre a mesa, sem pressa')
        texto_animado('-todos que chegam aqui querem esquecer...')
        texto_animado('-mas as vezes, o vinho só faz lembrar com mais nitidez.')
        texto_animado("""Você bebe. O liquido é quente, amargo... e estranho. Um peso suave invade seu peito.\nO mundo parece ficar mais cento.
        O velho ao fundo continua te observando, não disse uma palavra. Mas você sente...
        ele sabe o que você quer esquecer.""")
    else:
        texto_animado("""TABERNEIRO:
            -Ele está aqui há mais tempo do que qualquer um se lembre.
            -nunca disse seu nome. Nunca pediu nada. Só espera.Toda noite.
            """)
        print('Você sente que ja o viu..mas talvez tenha sido em um sonho...',end='\n\n')  
    
    print('====================NOITE 1-ARREPENDIMENTO==================================',end='\n\n')

    texto_animado(""" Enquanto o vinho repousa no fundo da taça...algo muda no ar.
    Os ventos da montanha batem contra as janelas da taberna, por um instante,tudo parece suspenso
    então... A porta range.
    um novo visitante entra.
    """)
    texto_animado("""sua armadura está arranhada, suja, pesada.
    o som de metal arrastando ecoa no chão de madeira.
    Ele senta ao seu lado, pede algo com a mão e bebe.
    só então fala - voz rouca, pausada.
    SOLDADO:
    -lutei...
    -por algo que eu acreditei ser justo.
     """)
    time.sleep(2)
    texto_animado("""-E não era.
    -fiz coisas que...nem o tempo ousa tocar.
    -hoje...minha guerra é outra.carrego o peso.e caminho...tentando perdoar quem fui.
     """)
    print('ele vira para o jogador,pela primeira vez,e olha fundo nos olhos.',end="\n\n")
    texto_animado("""========-E você...?-já fez algo que não da pra desfazer?=======""",end="\n\n")

    print("1-Sim.e penso nisso todos os dias.")
    print("2-Talvez..mas prefiro não lembrar.")
    print('3-Não.pelo menos,é o que eu gosto de acreditar.',end="\n\n")
    escolha3 = input('Escolha uma opção: ')
    if escolha3 == "1":
        print("""SOLDADO:olha para frente,em silêncio por alguns segundos:""")
        time.sleep(2)
        texto_animado("""-então entende o que é carregar um peso sem alça.
              -a culpa...não desaparece.mas ás vezes,aprende a andar ao lado.""")
        print("ele respira fundo.A mão treme levemente ao pegar o copo")
    elif escolha3 == "2":
        texto_animado("""SOLDADO:Sem olhar para o Voce:
       -fugir da memoria é uma guerra que nunca acaba:
       -eu também tentei...por anos.
       -mas o passado tem jeito de reaparecer...mesmo no silêncio.
       """)    
    elif escolha3 == "3":
        texto_animado("""SOLDADO-vira-se lentamente para voce,expressão dura:
       -cuidado.
       -ás vezes,a pior ilusão é a que criamos pra sobreviver.
       -mas a verdade...sempre encontra um jeito de falar com a gente.
       """)    
    else:
        print('resposta invalida') 

    texto_animado("""O soldado se levanta,deixa a taça vazia sobre a mesa.
        soldado antes de sair:
       -perdão não é esquecer.
       -é lembrar...sem sangrar.
    """,end="\n\n")       
    print("ele caminha até a porta.não olha para trás. sai.o velho permanece em silêncio.",end='\n\n')

    print("""O silêncio retorna.mas algo mudou dentro de voce),
    oque fazer com os erros que não podem ser corrigidos..?
    talvez a proxima noite traga mais pistas.""")
    
#===========================================fim 2 cap ===========================================================