import sys
import time


#Função para texto animado
def texto_animado(texto):
   for letra in texto:
      print(letra, end='')
      sys.stdout.flush()
      time.sleep(0.1)
   print()  