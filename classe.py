class gato:
    def __init__(self,fome=0,sono=0,brincar=0,dias=0,estado=''):
        self.fome = fome
        self.sono = sono
        self.brincar = brincar
        self.dias = dias
        self.estado = estado
        
        
        
    def inicio(self):
        self.estado ='normal'
        self.sono=0
        self.fome=0
        self.dias=0
        self.brincar=0
        print('você acaba de ganhar um gato, huuummmmm')
        self.status(self)
    def alimentar(self):
        print('''
                -----oções de comidas-----
                1- comida de panela: 30 pontos
                2- ração: 50 pontos
                3- mortandela: 70 pontos
                4- a mistuda da comida do dono: 100 pontos''')
        op = int(input('opção:  '))
        if op ==1:
            print('''
                    alimentado com comida de panela
                    fome {} >> {}
                    fadiga {} >> {}'''.format(self.fome, self.fome-30,self.sono,self.sono+10))
            self.fome -= 30
            self.sono += 10
        if op ==2:
            print('''
                    alimentado com ração basica de gatos
                    fome {} >> {}
                    fadiga {} >> {}'''.format(self.fome, self.fome-50,self.sono,self.sono+15))
            self.fome -=50
            self.sono += 15
        if op ==3:
            print('''
                    alimentado com mortandela
                    fome {} >> {}
                    fadiga {} >> {}'''.format(self.fome, self.fome-70,self.sono,self.sono+30))
            self.sono -=70
            self.sono += 30
        if op ==4:
            print('''
                    você deu sua mistura para o gato
                    fome {} >> {}
                    fadiga {} >> {}'''.format(self.fome, self.fome-100,self.sono,self.sono+50))
            self.sono -=100
            self.sono += 50
            self.estado = 'gato gordo do pai'
        self.status(self)
        
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
                    alisou o gato:
                    diversão {} >> {}
                    fadiga {} >> {}
                    fome {} >> {}'''.format(self.brincar,self.brincar +20, self.sono, self.sono+15, self.fome,self.fome+30))
            self.brincar +=20
            self.sono += 15
            self.fome += 30
        if op ==3:
            print('''
                    fez o gato perseguir um laser:
                    diversão {} >> {}
                    fadiga {} >> {}
                    fome {} >> {}'''.format(self.brincar,self.brincar +40, self.sono, self.sono+30, self.fome,self.fome+50))
            self.brincar +=40
            self.sono += 30
            self.fome += 50
        if op ==4:
            print('''
                    vc amarrou o gato a um foguete... ele morreu!!:
                    diversão {} >> {}
                    fadiga {} >> {}
                    fome {} >> {}'''.format(self.brincar,self.brincar +1000, self.sono, self.sono+100, self.fome,self.fome+100))
            self.brincar +=1000
            self.sono += 100
            self.fome += 100
            self.estado = 'quase morto'
        self.status(self)
            
    def dormir(self):
        mimir = self.sono
        self.sono -=80
        if self.sono <0:
            self.sono = 0
        self.dias +=1
            
        self.fome +=60
        print('seu gato dormiu e retirou 80 pontos de fadiga')
        print('fadiga {} >> {}'.format(mimir,self.sono))
        print('fome {} >> {}'.format(self.fome - 60,self.fome))
        print('dias {} >> {}'.format(self.dias-1,self.dias))
        print('..............................................')
        self.status(self)
        
    def status(self):
        if self.sono < 0:
            self.sono =0
        if self.fome < 0:
            self.fome =0
        if self.fome > 100:
            self.fome =100
        if self.sono > 100:
            self.sono =100
        print('''
                -----status-----
                fadiga: {}
                fome: {}
                diversão: {}
                dias: {}
                status do gato: {}'''.format(self.sono,self.fome,self.brincar,self.dias,self.estado))
        print('.............................')