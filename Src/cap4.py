import os
from funções import texto_animado
import time
import textwrap


def cap4():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto_animado('===☽✦☾ Noite 4- FÉ/INTUIÇÃO/DESTINO ☽✦☾==='.center(50))
    time.sleep(2)
    print('')
    
    texto1 ="""O sol se pôs há pouco. Você retorna á taberna. Após a noite anterior, ele não entrou
    preferiu o silêncio de casa. mas hoje,algo o atraiu de volta.
    A taberna está mais calma que o habitual.O taberneiro limpa alguns copos distraido.pouco depois a porta se abre.
    Entra uma mulher de véu branco,olhos leitosos e cajado de madeira. ela caminha,e em sua mão,uma cesta coberta com um pano bordado..."""
    texto_animado(textwrap.fill(texto1))
    time.sleep(5)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    texto_animado('-como será enxergar o mundo sem os olhos?')
    print('')
    
    texto2= """ANDARILHA(ANTES MESMO DELE FALAR):\n\n
    -Mais leve,ás vezes.
    quando deixamos de ver o que distrai,começamos a notar oque importa.
    ela sorri e se senta perto do fogo. o taberneiro agradece os pães doces que ela trouxe.
    ela não parece surpresa com sua presença."""
    texto_animado(textwrap.fill(texto2))
    print('')
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    texto3= """-quando perdi a visão,ainda era criança.No começo,chorei por tudo que não veria mais.
    mas então...comecei a ver oque os olhos escondem.
    -as palavras mudam de cor conforme o tom.os passos contam segredos.
    o silêncio...grita,quando escutamos com o coração.
    -Me diga,cavaleiro...quando escuta o mundo,oque ouve primeiro?"""
    texto_animado(textwrap.fill(texto3))
    print('')
    
    print("[1] ➤ O que grita mais alto.sempre fui guiado pelo que é forte.".center(50))
    print('[2] ➤ Às vezes ouço algo no fundo...mas é dificil confiar.     '.center(50))
    print('[3] ➤ Eu tento silenciar tudo...para ouvir oque vem de dentro. '.center(50))
    print('')
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        print('-O mundo grita porque tem medo de ser ignorado.mas oque é verdadeiro...quase sempre fala baixo')
    elif escolha == '2':
        print("""-A intuição é como um fio de luz na neblina.não é clara...mas é certa.
        quem aprende a seguir,raramente se perde.""")
    elif escolha == '3':
       print('''-Então você ja conheceu o sussuro do destino.ele não exige...apenas convida.''')
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
    
    os.system('cls' if os.name == 'nt' else 'clear')    
    texto4="""A andarilha se levanta,e antes de ir,toca o seu ombro com o cajado.-fé não é certeza
    fé é confiar...mesmo sem ver.
    ela entrega a ele uma pequena fita de pano branco.
    -guarde.quando tudo parecer escuro...lembre-se de que você
    tem mais olhos do que pensa.
    A intuição não grita.mas quando falamos com ela...responde"""  
    texto_animado(textwrap.fill(texto4))
    time.sleep(5)
    
    
    
    
    
if __name__ == "__main__":
    cap4()