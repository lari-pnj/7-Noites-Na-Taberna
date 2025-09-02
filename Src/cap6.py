import os
from funções import texto_animado
import time
import textwrap


def cap6():
    os.system("cls" if os.name == "nt" else "clear")
    texto_animado('===☽✦☾ Noite 6- PACIÊNCIA ☽✦☾==='.center(50))
    time.sleep(2)
    print('')
    
    os.system("cls" if os.name == "nt" else "clear")
    texto="""Amanhece no lado de fora da taberna.O céu começa a clarear.
    o silêncio do mundo é interrompido apenas pelo som
    dos passaros e pelo vento passando entre as folhas. """
    texto_animado(textwrap.fill(texto))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto1="""Voce caminha lentamente pela estrada de terra que levava
    de voltá á sua casa.A taberna ainda estava viva em sua mente,
    as vozes,os rostos,os pensamentos...mas do lado de fora,o mundo era diferente.
    mais leve.mas real."""
    texto_animado(textwrap.fill(texto1))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto2="""enquanto seguia pelo campo umido de orvalho,algo lhe chamou atenção.
    À beira de uma arvore antiga,
    uma senhora estava sentada num banquinho de madeira,sozinha,com um pequeno vaso no colo.
    dentro dele,um broto verde e delicado.
    sem saber porque,o (jogador) parou.
    depois,sentou-se ao lado dela."""
    texto_animado(textwrap.fill(texto2))
    time.sleep(2)
    
    print("""VELHA:
    -sabe quanto tempo faz que eu plantei essa arvore?
    -quarenta anos.e ainda espero pelas flores.\n\n""")
    
    print("""ela não o olhou,ainda estava com os olhos fixos na arvore á frente.\n\n""")
    time.sleep(3)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    texto3="""-sabe,o mundo corre,grita,exige.Mas há coisas que não correm,não gritam.
    só crescem.
    A flor....ela só vem quando o tempo decide que sim."""
    texto_animado(textwrap.fill(texto3))
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""-Me diga....você tem pressa dequê?\n\n""")
    print("[1] ➤ ver o resultado nas minhas escolhas.    ".center(50))
    print("[2] ➤ Me curar logo de tudo oque sinto        ".center(50))
    print("[3] ➤ Ser alguém melhor o mais rápido possível".center(50))
    escolha = input('Escolha uma opção:')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"voce escolheu {escolha}")
    if escolha == "1":
        texto4="""-Ah...o solo precisa ser mexido antes da semente ser plantada.e mesmo depois,
        ainda há chuva,sombra,vento...tudo isso antes do broto romper a terra.
        só porque você não ve,não quer dizer que não esteja crescendo."""
        texto_animado(textwrap.fill(texto4))
        time.sleep(2)
    elif escolha == "2":
        texto5="""-A dor não tem botão.ela dissolve aos poucos,feito gelo no chá quente.
        tentar apressar isso é como pedir pro inverno ir embora com palavras."""
        texto_animado(textwrap.fill(texto5))
        time.sleep(2)
    elif escolha == "3":
        texto6="""-Já pensou se uma borboleta forrçasse seua asa a crescer antes da hora?
        ela não voaria.ser melhor exige tempo. e tempo exige...paciência."""
        texto_animado(textwrap.fill(texto6))
        time.sleep(2)
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        return cap6()
    print('')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('a velha sorri e se levanta com o vaso nos braços\n\n')
    
    texto7="""VELHA:
    -crescimento exige tempo.e tempo,exige fé.
    regue oque há em você,mesmo que os outros não vejam flores.
    elas virão."""
    texto_animado(textwrap.fill(texto7))
    time.sleep(2)

if __name__=="__main__":
    cap6()