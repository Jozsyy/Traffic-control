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
    Fuzzy_System.Emem.Width1 = 5
    Fuzzy_System.Emem.Width2 = 2

    for i in range(0, 5):
        Fuzzy_System.Emem.Center1[i]=5*i
        Fuzzy_System.Emem.Center2[i]=2*(i)-4

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
    print(Mem.Dom1)
    print(Mem.Dom2)

def rules(i, j):    #i jeloli a sor hosszat, j pedig a valtozast
    #i=0
    if i==0 and j==0:
        return -4
    elif i==0 and j==1:
        return -4
    elif i==0 and j==2:
        return -2
    elif i==0 and j==3:
        return 0
    elif i==0 and j==4:
        return 2
    #i=1
    elif i==1 and j==0:
        return -4
    elif i==1 and j==1:
        return -2
    elif i==1 and j==2:
        return 0
    elif i==1 and j==3:
        return 0
    elif i==1 and j==4:
        return 2
    #i=2
    elif i==2 and j==0:
        return -2
    elif i==2 and j==1:
        return 0
    elif i==2 and j==2:
        return 2
    elif i==2 and j==3:
        return 2
    elif i==2 and j==4:
        return 4
    #i=3
    elif i==3 and j==0:
        return 0
    elif i==3 and j==1:
        return 2
    elif i==3 and j==2:
        return 2
    elif i==3 and j==3:
        return 4
    elif i==3 and j==4:
        return 4
    #i=4
    elif i==4 and j==0:
        return 2
    elif i==4 and j==1:
        return 2
    elif i==4 and j==2:
        return 4
    elif i==4 and j==3:
        return 4
    elif i==4 and j==4:
        return 4
    

def Match(Emem):
    Pos = {-4:0, -2:0, 0:0, 2:0, 4:0}

    for i in range(0,5):
        for j in range(0,5):
            if Emem.Dom1[i]!=0 and Emem.Dom2[j]!=0:
                rule=rules(i,j)
                value=min(Emem.Dom1[i], Emem.Dom2[j])
                if Pos[rule]!=0:
                    Pos[rule]=max(value,Pos[rule])
                else:
                    Pos[rule]=value

    print("Pos="+str(Pos))
    return Pos

#Sulyozott atlag
def Inf_Defuzz(Pos):
    weighted_sum = 0
    total_weight = 0

    for rule, value in Pos.items():
        # A szabály súlya maga a szabály értéke
        weighted_sum += value * rule
        total_weight += value

    print(weighted_sum)
    print(total_weight)

    if total_weight != 0:
        defuzzified_value = weighted_sum / total_weight
        return defuzzified_value
    else:
        return None  

def Fuzzy_Control(e1, e2, Fuzzy_System):
    Fuzzyify(e1, e2, Fuzzy_System.Emem)
    Pos=Match(Fuzzy_System.Emem)
    return Inf_Defuzz(Pos)

'''
# Teszt
Fuzzy_System = Fuz_Sys()
Fuzzy_Init(Fuzzy_System)
e1 = 30
e2 = 6
print("Fuzzy control:", Fuzzy_Control(e1, e2, Fuzzy_System))

'''