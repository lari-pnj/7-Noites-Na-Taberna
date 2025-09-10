import time
from funções import texto_animado , limpar_tela , mostrar_opcoes , perguntar_opcao , pausa
import os


#funcao chama as opcoes da primeira escollha
def primeira_escolha():
    escolha1= ["[1]➤ Me dê algo forte. Preciso esquecer","[2]➤ Prefiro conversar. Quem é aquele velho?"]
    for linha in escolha1:
        print(linha)
    print('') 
    
#funcao de opcoes para segunda escolha
def segunda_escolha():
    escolha2=["[1]➤ Sim.e penso nisso todos os dias,","[2]➤ Talvez..mas prefiro não lembrar" ,"[3]➤ Não.pelo menos,é o que eu gosto de acreditar."]
    for linha in escolha2:
     print(linha)
     print('')    


#introducao capitulo 1    
def cap1():
    limpar_tela()
    print('\nIniciando....\n')
    pausa()
    
    #fala narrador
    limpar_tela()
    texto_animado ("""Você empurra a porta. Um aroma de vinho envelhecido, E ervas secas preenche o ar.\nO calor do fogo estala na lareira. E apenas um velho sentado ao fundo. Parece te olhar...\nmesmo que nunca tenha o visto.""")
    pausa()
    
    limpar_tela()
    texto_animado("""TABERNEIRO: - Bem vindo a ultima taberna antes do despertar.\nsete noites, sete Historias...E talvez,\nsete partes de você mesmo, quer beber..ou conversar primeiro?""")
    print('')
  
    while True:
        primeira_escolha()
        escolha1 = input('Escolha uma opção: ').strip()  
        if escolha1 == '1':
            limpar_tela()
            texto_animado ='''taberneiro: coloca a taça sobre a mesa, sem pressa\n-todos que chegam aqui querem esquecer...\n-mas as vezes, o vinho só faz lembrar com mais nitidez.'''
            for linha in texto_animado:
                print((linha))
            pausa()     
            limpar_tela()  
               
            texto_animado("""Você bebe. O liquido é quente, amargo... e estranho. Um peso suave invade seu peito.\nO mundo parece ficar mais cento.
            O velho ao fundo continua te observando, não disse uma palavra. Mas você sente...
            ele sabe o que você quer esquecer.""")
            break
        
        elif escolha1 == '2':
            limpar_tela()
            texto_animado("""TABERNEIRO:
            -Ele está aqui há mais tempo do que qualquer um se lembre.\n-nunca disse seu nome. Nunca pediu nada. Só espera.Toda noite.""")
            pausa()
            limpar_tela()
            print('Você sente que ja o viu..mas talvez tenha sido em um sonho...\n')
            pausa()
            limpar_tela()
            break
        
        else: 
         print('opcao invalida, tente novamente! ') 
         
    inicio_noite1()      
    
     
#inicio da primeira noite
def inicio_noite1():
    print('===☽✦☾ NOITE 1-ARREPENDIMENTO ☽✦☾==='.center(50))
    pausa()
    limpar_tela()

    texto_animado("""Enquanto o vinho repousa no fundo da taça...algo muda no ar.\nOs ventos da montanha batem contra as janelas da taberna, por um instante,tudo parece suspenso
    então... A porta range.\num novo visitante entra.""")
    pausa()
    limpar_tela()
    texto_animado("""sua armadura está arranhada, suja, pesada. o som de metal arrastando ecoa no chão de madeira.\nEle senta ao seu lado, pede algo com a mão e bebe. só então fala - voz rouca, pausada.
    SOLDADO:\n-lutei...\n-por algo que eu acreditei ser justo.""")
    pausa()
    limpar_tela()
    texto_animado("""-E não era.\n-fiz coisas que...nem o tempo ousa tocar.\n-hoje...minha guerra é outra.carrego o peso.e caminho...tentando perdoar quem fui.""")
    pausa()
    limpar_tela()
    print('ele vira para o jogador,pela primeira vez,e olha fundo nos olhos.\n')
    pausa()
    texto_animado("""E você...? - já fez algo que não da pra desfazer?""")
    
    while True:
        segunda_escolha()
        escolha2 = input('Escolha uma opção: ').strip()
        if escolha2 == "1":
            print("""SOLDADO: Olha para frente, em silêncio por alguns segundos:""")
            pausa()
            limpar_tela()
            texto_animado("""-Então entende o que é carregar um peso sem alça.\n-a culpa...não desaparece. mas ás vezes,aprende a andar ao lado.\n""")
            pausa()
            limpar_tela()
            print("ele respira fundo. A mão treme levemente ao pegar o copo")
            pausa()
            limpar_tela()
            texto_animado("""-então entende o que é carregar um peso sem alça.\n-a culpa...não desaparece. mas ás vezes,aprende a andar ao lado.""")
            break
        
        elif escolha2 == "2":
            texto_animado("""SOLDADO: Sem olhar para Voce:\n-fugir da memoria é uma guerra que nunca acaba:\n-eu também tentei...por anos.\n-mas o passado tem jeito de reaparecer...mesmo no silêncio.""")
            break
        
        elif escolha2 == "3":
            texto_animado("""SOLDADO: vira-se lentamente para voce, expressão dura:\n-cuidado.\n-ás vezes,a pior ilusão é a que criamos pra sobreviver.\n-mas a verdade...sempre encontra um jeito de falar com a gente.""")
            break
        else:
            print('resposta invalida')

    texto_animado("""O soldado se levanta, deixa a taça vazia sobre a mesa.\nsoldado antes de sair:\n-perdão não é esquecer.\n-é lembrar...sem sangrar.""")  
    pausa()
    limpar_tela()  

    print("ele caminha até a porta. não olha para trás. sai. o velho permanece em silêncio.\n")
    pausa()
    limpar_tela()

    texto_animado("""O silêncio retorna. mas algo mudou dentro de voce,\noque fazer com os erros que não podem ser corrigidos..?\ntalvez a proxima noite traga mais pistas.""")
    
    print('=========================FIM DA NOITE 1==================================\n')     
            
    
if __name__ == '__main__':
    cap1()    