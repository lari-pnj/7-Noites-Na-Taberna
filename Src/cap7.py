import os
from funções import texto_animado
import time
import textwrap


def cap7():
    os.system('cls' if os.name =="nt" else "clear")
    texto_animado('===☽✦☾ Noite 7 - O VELHO ☽✦☾==='.center(50))
    time.sleep(2)
    print('')
    
    os.system('cls' if os.name =="nt" else "clear")
    texto="""A taberna,antes cheia de risos,conversas e reflexões,
    Agora estava quase vazia,as luzes estavam mais suaves,o ar mais denso.
    e ele (o jogador) sentiu isso assim que cruzou a porta."""
    texto_animado(textwrap.fill(texto))
    time.sleep(2)
    
    os.system('cls' if os.name =="nt" else "clear")
    texto1="""Lá no canto,onde todas as noites havia estado,estava o velho.
    O mesmo velho.
    Sempre ali,calado. com os olhos firmes,mas serenos.era como uma estatua viva
    Alguém que via tudo,mas nunca dizia nada.
    mas naquela noite....
    ele falou."""
    texto_animado(textwrap.fill(texto1))
    time.sleep(2)

    os.system('cls' if os.name =="nt" else "clear")
    print("""A voz era grave,mas não rude.Pausada.como se cada palavra fosse lapidada antes de sair.\n\n""")
    time.sleep(3)
    
    os.system('cls' if os.name =="nt" else "clear")
    texto2="""VELHO:
    -sente-se.
    -Eu estive aqui todas as noites cada vez que você duvidou de si.
    cada vez que fingiu ser forte.
    estive aqui...quando você quis desaparecer."""
    texto_animado(textwrap.fill(texto2))
    time.sleep(2)
    
    os.system('cls' if os.name =="nt" else "clear")
    texto3="""ele ergue lentamente os olhos.e o (jogador)vê algo familiar.
    muito familiar"""
    texto_animado(textwrap.fill(texto3))
    time.sleep(2)

    os.system('cls' if os.name =="nt" else "clear")
    texto4="""-Já percebeu....que todos aqueles que você conheceu aqui...
    eram só pedaços de você mesmo?"""
    texto_animado(textwrap.fill(texto4))
    time.sleep(2)

    os.system('cls' if os.name =="nt" else "clear")
    texto5="""ele faz uma pausa longa.
    depois pergunta,direto,simples,como um espelho:
    -me diga...
    voce se trata como trata quem ama?"""
    texto_animado(textwrap.fill(texto5))
    time.sleep(2)
    print('')

    print('[1] ➤ Como quem ama.   '.center(50))
    print('[2] ➤ Como quem odeia? '.center(50))
    print('[3] ➤ não sei responder'.center(50))
    print('')
    escolha =input('Escolha uma opção: ')
    print(f'voce escolheu {escolha}')
    time.sleep(2)
    if escolha == "1":
        texto6="""-O velho sorri,um sorriso sutil,quase imperceptivel.
        -Então continue.poque isso é raro.e preciso.
        só não se esqueça de ser paciente com suas sombras tambem.
        O amor verdadeiro não é exigente.ele é presente."""
        texto_animado(textwrap.fill(texto6))
        time.sleep(2)
        
    elif escolha == "2":
        texto7="""-O velho abaixa os olhos.não por decepção.por compaixão.
        -Então chegou a hora de mudar isso.
        você mora dentro de si.
        nâo pode viver num lugar onde só há desprezo."""
        texto_animado(textwrap.fill(texto7))
        time.sleep(2)

    elif escolha == "3":
        texto8="""-O velho inclina a cabeça,como se ponderasse.
        -Não saber é o primeiro passo para aprender.
        -E eu estarei aqui,sempre que precisar."""
        texto_animado(textwrap.fill(texto8))
        time.sleep(2)
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")  
        
    os.system('cls' if os.name == 'nt' else 'clear') 
    textoA=""" O velho se levanta.pela primeira vez em todas as noites.
    ele caminha até o centro da taberna.diante do (jogador) 
    e diz:"""
    texto_animado(textwrap.fill(textoA))
    time.sleep(3)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    textoA1="""-todos eles...A mulher do broto,o homem com medo.
    todos estavam em voce.mas eu....
    EU SOU VOCÊ..."""
    texto_animado(textwrap.fill(textoA1))
    time.sleep(4)

    os.system('cls' if os.name == 'nt' else 'clear')
    textoA2="""ele toca o ombro do (jogador)com leveza."""
    texto_animado(textwrap.fill(textoA2))
    time.sleep(3)
    print('')
    
    textoA3="""A taberna não era um lugar.era voce mesmo,por dentro.
    e aquela era a sétima noite.
    mas a primeira vez que se sentiu em casa.
                           FIM."""
    texto_animado(textwrap.fill(textoA3))
    time.sleep(3)
    




if __name__ == "__main__":
    cap7() 
    