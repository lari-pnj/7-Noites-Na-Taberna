import os
from funções import texto_animado
import time
import textwrap

def cap5():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto_animado('===☽✦☾ Noite 5- AMOR PERDIDO/SAUDADE/PERDA ☽✦☾==='.center(50))
    time.sleep(2)
    print('')
    
    texto1= """A noite desce lenta como uma saudade antiga.
    Você entra na taberna, cansado, não de caminhar, mas de sentir.
    O taberneiro limpa o balcão, imerso em seu próprio silêncio.
    de repente,a porta se abre com um rangido conhecido.
    cambaleando,entra um homem com a camisa aberta,um caderno
    amassado sob o braço,e o olhar perdido num lugar que só ele encherga.
    ele se joga em uma cadeira proxima ao fogo."""
    texto_animado(textwrap.fill(texto1))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto2="""POETA:
    -O de sempre,companheiro.Que hoje...o coração pesa mais que ontem.
     O taberneiro serve sem dizer nada.
     O poeta levanta o copo,olha para o cavaleiro,e ergue um brinde no ar.
     -Aos que ainda esperam...mesmo sem saber pelo que"""
    texto_animado(textwrap.fill(texto2))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto3 ="""toma um gole lento.depois outro.fica um tempo em silêncio,olhando o fogo.então,sem virar o rosto"""
    texto_animado(textwrap.fill(texto3))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto4 = """-sabe,rapaz...tem dores que a gente aprende a esconder tão bém
    que um dia até esquece onde guardou...mas elas continuam lá.
    quietinha,esperando um cheiro,uma música...um nome."""
    texto_animado(textwrap.fill(texto4))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto5 = """ele abre o caderno com as mãos tremulas.A foha esta suja de vinho.
    começa a ler um poema,mas para na metade.suspira."""
    texto_animado(textwrap.fill(texto5))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto6 = """-Eu escrevo sobre ela quase toda semana mas nunca termino.
     talvez porque...no fundo,eu nunca quis terminar essa historia."""
    texto_animado(textwrap.fill(texto6))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    texto7 = """Ele vira para voce, olhos marejados,mas com um sorriso torto:"""
    texto_animado(textwrap.fill(texto7))
    
    print("-E você? Ja aprendeu a dizer Adeus...pra quem nunca saiu de dentro?")
    print('')
    print("[1] ➤ sim.mas a saudade ainda acorda comigo.".center(50))
    print("[2] ➤ não.e talvez nunca consiga.           ".center(50))
    print("[3] ➤ Acho que ainda to aprendendo          ".center(50))
    escolha = input('Escolha uma opção: ')
    if escolha == "1":
        texto8="""-Ah...então você entende. A saudade não bate á porta,ela mora na casa toda"""
        texto_animado(textwrap.fill(texto8))
        time.sleep(2)
    elif escolha == "2":
        texto9="""-Alguns nomes...a gente só aprende a silênciar.
        mas esquecer?isso é mentira que a gente conta pra dormir."""
        texto_animado(textwrap.fill(texto9))
        time.sleep(2)
    elif escolha == "3":
        texto10="""-Aprender é o que resta quando amar já não é possivel.
        que bom que você ainda tenta."""
        texto_animado(textwrap.fill(texto10))
        time.sleep(2)
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")  
        
    texto11="""O poeta se levanta devagar,pega uma folha solta do caderno e dobra com cuidado.
    ele entrega ao cavaleiro sem olhar nos olhos."""   
    texto_animado(textwrap.fill(texto11))
    time.sleep(2)

    os.system("cls" if os.name == "nt" else "clear")
    texto12="""POETA:
    -se um dia quiser entender...leia isso.
    mas só se quiser mesmo.
    ás vezes,guardar também é amar.
    ele vai até a porta,para por um instante e diz:"""
    texto_animado(textwrap.fill(texto12))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    textoa1="""-nem todo amor é para ser vivido.alguns vêm só pra ensinar a sentir. e partem...antes de se tornarem prisão"""
    texto_animado(textwrap.fill(textoa1))
    time.sleep(2)
    
    os.system("cls" if os.name == "nt" else "clear")
    print("""ESCOLHA FINAL:
    Você olha a carta nas mãos.ela está selada com vinho seco.deseja abrir?\n\n""")

    print("[1] ➤ sim,agora.                 ".center(50))
    print("[2] ➤ não,ainda não estou pronto.".center(50))
    escolha2 = input("Escolha uma opção: ")
    if escolha2 == "1": ### Opção de abrir a carta
        textoa2="""A carta diz:
        Nem todo amor é pra durar.
        alguns chegam como chuva de verão:
        intensos,inesperados,inesqueciveis.
        mas se tentarmos segura-los...
        escorrem pelos dedos.
        isso não os torna menos verdadeiros
        só menos permanentes"""
        texto_animado(textwrap.fill(textoa2))
        time.sleep(2)
    elif escolha2 == "2":
        textoa3="""você guarda a carta junto ao peito.
        talvez um dia leia.
        talvez nunca precise.
        mas saber que ela está ali...conforta."""
        texto_animado(textwrap.fill(textoa3))
        time.sleep(2)
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        
    textoa4="""A taberna se esvazia.o taberneiro recolhe os copos.
    e no fogo,uma folha queimada dança no ar.
    o cavaleiro pensa:
    talvez amar...seja mesmo aprender a deixar ir"""   
    texto_animado(textwrap.fill(textoa4))
    time.sleep(2) 
    
    
    


if __name__ == "__main__":
    cap5()