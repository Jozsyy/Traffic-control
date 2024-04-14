import matplotlib.pyplot as plt
import numpy as np

class IN_MEM:
    def __init__(self):
        self.Width1 = 0.0
        self.Center1 = [0.0] * 5
        self.Dom1 = [0.0] * 5
        self.Width2 = 0.0
        self.Center2 = [0.0] * 5
        self.Dom2 = [0.0] * 5

class OUT_MEM:
    def __init__(self):
        self.value=0.0

class Fuz_Sys:
    def __init__(self):
        self.Emem = IN_MEM()
        self.Edotmem = IN_MEM()
        self.Imem = IN_MEM()
        self.Outmem = OUT_MEM()

def MAX(a,b):
    if a>b:
        return a
    else:
        return b

def MIN(a,b):
    if a<b:
        return a
    else:
        return b
    
def Fuzzy_Init(Fuzzy_System):
    Fuzzy_System.Emem.Width1 = 10
    Fuzzy_System.Emem.Width2 = 4
    Fuzzy_System.Edotmem.Width1 = 10
    Fuzzy_System.Edotmem.Width2 = 4
    Fuzzy_System.Imem.Width1 = 10
    Fuzzy_System.Imem.Width2 = 4

    for i in range(0, 5):
        Fuzzy_System.Emem.Center1[i]=5*(i+1)
        Fuzzy_System.Emem.Center2[i]=2*(i)-4
        Fuzzy_System.Edotmem.Center1[i]=5*(i+1)
        Fuzzy_System.Edotmem.Center2[i]=2*-4
        Fuzzy_System.Imem.Center1[i]=5*(i+1)
        Fuzzy_System.Imem.Center2[i]=2*-4

def LeftAll(u,w,c):
    if u<c:
        return 1.0
    else:
        return max(0,(1-(u-c)/w))

def RightAll(u,w,c):
    if u>=c:
        return 1.0
    else:
        return max(0,(1-(c-u)/w))
    
def Triangle(u,w,c):
    if u>=c:
        return max(0,(1-(u-c)/w))
    else:
        return max(0,(1-(c-u)/w))
    
def Fuzzyify(U1, U2, Mem):
    Mem.Dom1[0] = LeftAll(U1, Mem.Width1, Mem.Center1[0])
    Mem.Dom2[0] = LeftAll(U2, Mem.Width2, Mem.Center2[0])
    for i in range(1, 4):
        Mem.Dom1[i] = Triangle(U1, Mem.Width1, Mem.Center1[i])
        Mem.Dom2[i] = Triangle(U2, Mem.Width2, Mem.Center2[i])
    Mem.Dom1[4] = RightAll(U1, Mem.Width1, Mem.Center1[4])
    Mem.Dom2[4] = RightAll(U2, Mem.Width2, Mem.Center2[4])

def Match(Emem, Edotmem, Imem, Pos):

    Pos1 = [0]*5
    for i in range(0,5):
        if Emem.Dom1[i] != 0 and Emem.Dom2[i]:
            Pos1[i]=min(Emem.Dom1[i], Emem.Dom2[i])
        else:
            Pos1[i]=0

    #Sulyozott atlag
    Pos[0]=(Pos1[0]*5+Pos1[1]*10+Pos1[2]*15+Pos1[3]*20+Pos1[4]*25)/(5+10+15+20+25)
    print(Emem.Dom1, Emem.Dom2)
    print(Pos1)

    Pos2 = [0]*5
    for i in range(0,5):
        if Edotmem.Dom1[i] != 0 and Edotmem.Dom2[i]:
            Pos2[i]=min(Edotmem.Dom1[i], Edotmem.Dom2[i])
        else:
            Pos2[i]=0

    Pos[1]=(Pos2[0]*5+Pos2[1]*10+Pos2[2]*15+Pos2[3]*20+Pos2[4]*25)/(5+10+15+20+25)
    print(Pos2)
    Pos3 = [0]*5
    for i in range(0,5):
        if Imem.Dom1[i] != 0 and Imem.Dom2[i]:
            Pos3[i]=min(Imem.Dom1[i], Imem.Dom2[i])
        else:
            Pos3[i]=0
    Pos[2]=(Pos3[0]*5+Pos3[1]*10+Pos3[2]*15+Pos3[3]*20+Pos3[4]*25)/(5+10+15+20+25)
    print(Pos3)
    print(Pos)

#Sulyozott atlag
def Inf_Defuzz(Pos):
    res=max(Pos[0], Pos[1], Pos[2])
    print(res)
    if res <= 0.2:
        return -5
    elif res > 0.2 and res <= 0.4:
        return -2
    elif res > 0.4 and res <= 0.6:
        return 0
    elif res > 0.6 and res <= 0.8:
        return 2
    elif res > 0.8:
        return 5
    else:
         return 0

def Fuzzy_Control(e1, e2, edot1, edot2, inp1, inp2, Fuzzy_System):
    Pos = [0] * 3
    Fuzzyify(e1, e2, Fuzzy_System.Emem)
    Fuzzyify(edot1, edot2, Fuzzy_System.Edotmem)
    Fuzzyify(inp1, inp2, Fuzzy_System.Imem)
    Match(Fuzzy_System.Emem, Fuzzy_System.Edotmem,Fuzzy_System.Imem, Pos)
    return Inf_Defuzz(Pos)

# Teszt
'''
Fuzzy_System = Fuz_Sys()
Fuzzy_Init(Fuzzy_System)
e1 = 10
e2 = -2
edot1 = 15
edot2 = 2
inp1 = 20
inp2 = 1
print("Fuzzy control:", Fuzzy_Control(e1, e2, edot1, edot2, inp1, inp2, Fuzzy_System))
'''
