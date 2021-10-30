from classe import gato
gato.inicio(gato)
while True:
    
    print('''
          ---painel de escolhas---
          1- alimentar
          2- brincar
          3- dormir
          4- status
          5- sair''')
    op = int(input('opção: '))
    if op ==5:
        break
    if op ==1:
        gato.alimentar(gato)
    if op ==2:
        gato.interagir(gato)
    if op ==3:
        gato.dormir(gato)
    if op ==4:
        gato.status(gato)