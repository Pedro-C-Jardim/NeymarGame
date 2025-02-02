class Mapa:
    def __init__(self, fase): #800x1000 com 20 a mais em cada direcao por segurança
        self.matriz = [[0]*(100) for _ in range(120)]
        #0 = espaço vazio
        #1 = parede
        #2 = Objetivo

        if(fase == 1):          
            #posicionando o objetivo
            self.matriz[47][17] = 2

            #Inicializamos a matriz com o desenho do labirinto manualmente, 
            #1
            for i in range(0, 39): self.matriz[0][i] = 1
            #2
            for i in range(0, 31): self.matriz[11][i] = 1
            #3
            for i in range(0, 31): self.matriz[i][38] = 1
            #4
            for i in range(11, 31): self.matriz[i][30] = 1
            #Por exemplo temos o for 1 que vai de [0][0] até [0][38] e o 3 que vai de [0][38] até [30][38], formando um L


            for i in range(0, 15): self.matriz[30][16+i] = 1

            for i in range(0, 17):self.matriz[30][39+i] = 1

            for i in range(25, 48): self.matriz[41][i] = 1

            for i in range(30, 55):
                self.matriz[i][16] = 1
                self.matriz[i][56] = 1

            for i in range(41, 55):
                self.matriz[i][24] = 1
                self.matriz[i][48] = 1

            for i in range(0, 9):
                self.matriz[54][16+i] = 1
                self.matriz[54][48+i] = 1
        
        if(fase == 2):
            
            self.matriz[35][65] = 2

            for i in range(0, 12):
                self.matriz[34][i] = 1
                self.matriz[45][i] = 1
                self.matriz[34][61+i] = 1
                self.matriz[45][61+i] = 1
            
            for i in range(0, 16):
                self.matriz[34-i][12] = 1
                self.matriz[34-i][61] = 1
                self.matriz[45+i][12] = 1
                self.matriz[45+i][61] = 1

            #Nestes 2 For's inicializamos um retangulo 32X21, que pode ser contornado
            for i in range(0, 22):
                self.matriz[29 + i][20] = 1
                self.matriz[29 + i][53] = 1
            
            for i in range(0, 33):
                self.matriz[29][20+i] = 1
                self.matriz[50][20+i] = 1


            for i in range(0, 21):
                self.matriz[18][12+i] = 1
                self.matriz[18][41+i] = 1
                self.matriz[13][12+i] = 1
                self.matriz[13][41+i] = 1
                self.matriz[61][12+i] = 1
                self.matriz[61][41+i] = 1
                self.matriz[66][12+i] = 1
                self.matriz[66][41+i] = 1
            
            for i in range(0, 6):
                self.matriz[18-i][32] = 1
                self.matriz[18-i][40] = 1
                self.matriz[61+i][32] = 1
                self.matriz[61+i][40] = 1
            
            for i in range(0, 50):
                self.matriz[2][12+i] = 1
                self.matriz[77][12+i] = 1
            
            for i in range(0, 12):
                self.matriz[13-i][12] = 1
                self.matriz[13-i][61] = 1
                self.matriz[66+i][12] = 1
                self.matriz[66+i][61] = 1
                self.matriz[34+i][73] = 1

        
        if(fase == 3):
            self.matriz[5][12] = 2
            
            #Nesses 2 for's inicializamos um quadrado 800X750 que envolve o mapa inteiro 
            for i in range(0, 81):
                self.matriz[4][11+i] = 1
                self.matriz[79][11+i] = 1
            
            for i in range(0, 76):
                self.matriz[4+i][11] = 1
                self.matriz[4+i][91] = 1
            
            #Aqui 4 quadrados de mesmo tamanho que formam um caminho em forma de cruz
            for i in range(0,12):
                self.matriz[46+i][46] = 1
                self.matriz[46+i][27] = 1
                self.matriz[46+i][54] = 1
                self.matriz[46+i][75] = 1

            for i in range(0, 10):
                self.matriz[35-i][46] = 1
                self.matriz[35-i][27] = 1
                self.matriz[35-i][54] = 1
                self.matriz[35-i][75] = 1
            
            for i in range(0, 20):
                self.matriz[35][46-i] = 1
                self.matriz[26][46-i] = 1
                self.matriz[46][46-i] = 1
                self.matriz[57][46-i] = 1

            for i in range(0, 22):
                self.matriz[46][54+i] = 1
                self.matriz[57][54+i] = 1
                self.matriz[35][54+i] = 1
                self.matriz[26][54+i] = 1

            for i in range(0, 29):
                self.matriz[15][47 - i] = 1
                self.matriz[15][54 + i] = 1
                self.matriz[68][54 + i] = 1

            for i in range(0, 28):
                self.matriz[68][46 - i] = 1

            for i in range(0, 21):
                self.matriz[15+i][19] = 1
                self.matriz[15+i][83] = 1

            for i in range(0, 22):
                self.matriz[67-i][19] = 1
                self.matriz[67-i][83] = 1

            for i in range(0, 9):
                self.matriz[15][11+i] = 1
                self.matriz[15][47+i] = 1
                self.matriz[68][83+i] = 1
