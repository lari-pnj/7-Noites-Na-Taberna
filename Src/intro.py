import time
from main import texto_animado 


def introducao():
    texto_animado("""-Ora,Ora...um cavaleiro solitario,No alto da montanha,á essa hora?
 O que busca,coragem...ou Respostas?""")
    time.sleep(2)
    texto_animado("""Mas já que chegou até aqui...Que tal um vinho fresco,Á luz das velas da taberna? \nvenha entre.
  As noites são longas... e ás vezes,falam conosco.""")
    print('----'*20)
    time.sleep(2)
    
    #Jogador faz uma escolha 
    print('1-sim,claro.Que mal faria?')
    print('2-não,obrigado.prefiro observar as colinas...por enquanto.')
    escolha = input('Escolha uma opção: ')

     #funcao de iniciar o jogo
    def iniciar_jogo():
        print('Iniciando...')
        time.sleep(2)
        #fala narrador
        texto_animado("""Você empurra a porta.Um aroma de vinho envelhecido,madeira na lareira.E ervas secas preenche o ar.
        O calor do fogo estala na lareira.e apenas um velho sentado ao fundo.parece te olhar...
        mesmo que nunca tenha o visto.""")
        time.sleep(2)
        #fala taberneiro
        texto_animado("""TABERNEIRO:
        -Bem vindo a ultima taberna antes do despertar.
        sete noites,sete Historias...E talvez,sete partes de você mesmo,quer beber..ou conversar primeiro?""")

        #OPÇÕES:
        print("1-Me dê algo forte.Preciso esquecer")
        print("2-Prefiro conversar.Quem é aquele velho?")
        escolha3 = input("Escolha uma opção: ")
        if escolha3 == '1':
            print('taberneiro:coloca a taça sobre a mesa,sem pressa')
            texto_animado('-todos que chegam aqui querem esquecer...')
            texto_animado('-mas as vezes,o vinho só faz lembrar com mais nitidez.')
            texto_animado("""Você bebe.O liquido é quente,amargo...e estranho.um peso suave invade seu peito.\nO mundo parece ficar mais cento.
        O velho ao fundo continua te observando,não disse uma palavra.Mas você sente...
        ele sabe oque você quer esquecer.""")
        else:
            texto_animado("""TABERNEIRO:
            -Ele está aqui há mais tempo do que qualquer um se lembre.
            -nunca disse seu nome.Nunca pediu nada.Só espera.Toda noite.
            """)
            print('Você sente que ja o viu..mas talvez tenha sido em um sonho...')

    #Jogador escolhe entrar no jogo
    if escolha == '1':
        print("O jogador aceita o vinho.")
        iniciar_jogo()
    #Jogador escolhe esperar     
    else:
        time.sleep(2)
        print("som do vento,talvez um sino distante")
        texto_animado("""-Ás vezes, o silêncio nos oferece respostas... mas há perguntas que só a noite pode responder.
    Então,cavaleiro...vai entrar agora?""")
        print('----'*20)
        time.sleep(2)
     #Opcao de entrar novamente
        print('1-Entrar na taberna!')
        segunda_escolha=input('Escolha uma opção: ')
        if segunda_escolha == '1':
            print('Voce entrou na taberna!')
            iniciar_jogo()
#-----------------------------------------------FIM DA INTRODUÇÃO-----------------------------------------------------         

introducao()   