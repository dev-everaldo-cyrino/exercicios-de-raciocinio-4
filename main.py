class gato:
    def __init__(self,fome=0,sono=0,brincar=0):
        self.fome = fome
        self.sono = sono
        self.brincar = brincar
        print('você acaba de ganhar um gato, huuummmmm')
        
        def alimentar(self):
            print('''
                  -----oções de comidas-----
                  1- comida de panela: 30 pontos
                  2- ração: 50 pontos
                  3- mortandela: 70 pontos
                  4- a mistuda da comida do dono: 100 pontos''')
            op = int(input('opção:  '))
            if op ==1:
                self.fome -=30
                self.sono += 10
            if op ==2:
                self.fome -=50
                self.sono += 15
            if op ==3:
                self.sono -=70
                self.sono += 30
            if op ==4:
                self.sono -=100
                self.sono += 50
        
        def interagir(self):
            print('''
                  -----opções de brincadeiras-----
                  1- pega pega: 15 pontos
                  2- alisar: 20 pontos
                  3- fazer ele caçar o laizer 40 pontos
                  4- gato ajato: 1000 pontos''')
            op = int(input('opção:  '))
            if op ==1:
                print('''
                      brincou de pega pega:
                      diversão {} >> {}
                      fadiga {} >> {}
                      fome {} >> {}'''.format(self.brincar,self.brincar +15, self.sono, self.sono+10, self.fome,self.fome+20))
                self.brincar +=15
                self.sono += 10
                self.fome += 20
            if op ==2:
                print('''
                      brincou de pega pega:
                      diversão {} >> {}
                      fadiga {} >> {}
                      fome {} >> {}'''.format(self.brincar,self.brincar +20, self.sono, self.sono+15, self.fome,self.fome+30))
                self.brincar +=20
                self.sono += 15
                self.fome += 30
            if op ==3:
                print('''
                      brincou de pega pega:
                      diversão {} >> {}
                      fadiga {} >> {}
                      fome {} >> {}'''.format(self.brincar,self.brincar +40, self.sono, self.sono+30, self.fome,self.fome+50))
                self.brincar +=40
                self.sono += 30
                self.fome += 50
            if op ==4:
                print('''
                      brincou de pega pega:
                      diversão {} >> {}
                      fadiga {} >> {}
                      fome {} >> {}'''.format(self.brincar,self.brincar +1000, self.sono, self.sono+100, self.fome,self.fome+100))
                self.brincar +=1000
                self.sono += 100
                self.fome += 100
            
        def dormir(self):
            mimir = self.sono
            self.sono -=80
            if self.sono <0:
                self.sono = 0
            print('seu gato dormiu e retirou 80 pontos de fadiga')
            print('fadiga {} >> {}'.format(mimir,self.sono))
            print('..............................................')
        