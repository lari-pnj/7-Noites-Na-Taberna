import os
from funções import texto_animado
import time
import textwrap


def cap2():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto_animado('===☽✦☾ Noite 2- Medo e Coragem ☽✦☾==='.center(50))
    print('')
    time.sleep(2)

    texto1 = """A lareira queima mais forte. Um trovão distante. A madeira do teto range.O taberneiro serve outra taça, mas não fala nada."""
    texto_animado(textwrap.fill(texto1))
    print('')
    texto2 ="""NARRADOR: O medo sussurra. A coragem...se esconde. E ás vezes, o mais dificil não é lutar é se levantar."""
    texto_animado(textwrap.fill(texto2))
    time.sleep(2)
    print('')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    texto3 = """A porta se abre com força. um vento gélido entra. o novo visitante surge:um jovem de capa pesada,encharcado de suor mesmo com o frio.
    Ele se ajeita,como se quisesse parecer mais confiante. Ele olha em volta,seus olhos meio arregalados.Ele se senta ao seu lado"""
    texto_animado(textwrap.fill(texto3))
    print('')

    texto4 = """JOVEM: -Tá...tá tudo bém aqui né?ninguém vai...começar nada do nada certo? ele ri de si mesmo.nervoso."""
    texto_animado(textwrap.fill(texto4))
    print('')

    texto5 = """GUERREIRO:-Porque eu...não to aqui pra brigar,se for isso que ta pensando.-é só...sei lá.Curiosidade.Ele olha pro jogador.vê a espada em sua propria cintura.bate na bainha."""
    texto_animado(textwrap.fill(texto5))
    time.sleep(2)
    print('')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    texto5 ="""-eu carrego isso faz anos,acredita? nunca usei.nunca precisei. E espero continuar assim. Ou talvez eu só esteja enrolado mesmo."""
    texto_animado(textwrap.fill(texto5))
    print('')
    print('ele desvia o olhar.toma um gole de algo que o taberneiro colocou sem perguntar')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    
    texto6= """GUERREIRO: - Dizem que um dia todo guerreiro encontra sua grande batalha.
    mas...e se eu..e se eu travar na hora? e se eu fracassar?"""
    texto_animado(textwrap.fill(texto6))
    print('')
    
    #escolha do jogador
    print('[1] ➤ se você tem tanto medo porque continua carregando essa espada?'.center(50))
    print('[2] ➤ já pensou que talvez você esteja pronto e nem saiba?          '.center(50))
    print('[3] ➤ Todo mundo trava. A diferença é o que você faz depois.        '.center(50))
    escolha = input('Escolha uma opção: ')
    
    if escolha == "1":
        print('')
        escolha1 = """GUERREIRO:-Porque...sei lá. Vai que um dia eu preciso. E também....
        porque todo mundo espera que eu tenha uma. imagina um guerreiro...sem espada? eu ia virar piada.já fui,na real"""
        texto_animado(textwrap.fill(escolha1))
    elif escolha == "2":
        escolhas2 = """GUERREIRO: pronto?  pronto é quem não acordo suando frio só de ouvir a palavra "confronto"
        mas...vai ver é isso mesmo.A gente nunca sabe que tá pronto."""  
        texto_animado(textwrap.fill(escolhas2))
    elif escolha == "3":
        escolha3 = """É,isso é meio reconfortante.
        mas...se eu travar e correr?
        ai faço oque depois?
        desculpa.tô pensando alto demais,né?é que todos parecem prontos.
        e eu ainda tremo por dentro. seilá...as vezes é mais facil imaginar a derrota
        do que arriscar ser derrotado de verdade.

        ele olha pra você e tenta um sorriso.

        -boa sorte com as suas batalhas.
        -se descobrir o segredo...me conta."""
        texto_animado(textwrap.fill(escolha3))
    else:
        texto_animado("Escolha inválida. Por favor, selecione 1, 2 ou 3.")
        time.sleep(2)
        print('')
        
    texto7 = """NARRADOR: O medo é barulhento.mas as vezes,a coragem...
    é só dar um passo.mesmo que você não saiba pra onde."""
    texto_animado(textwrap.fill(texto7))
    time.sleep(5)

    print('Fim do capítulo 2')



cap2()
