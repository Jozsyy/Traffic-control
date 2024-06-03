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
        self.Pos = {-4:0, -2:0, 0:0, 2:0, 4:0}
        self.Width =[0.0] * 5

class Fuz_Sys:
    def __init__(self):
        self.Emem = IN_MEM()
        self.Outmem = OUT_MEM()
    
def Fuzzy_Init(Fuzzy_System):
    Fuzzy_System.Emem.Width1 = 5
    Fuzzy_System.Emem.Width2 = 2
    Fuzzy_System.Outmem.Width = 2

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
    #print(Mem.Dom1)
    #print(Mem.Dom2)

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
    

def Match(Emem,Outmem):
    for i in range(0,5):
        for j in range(0,5):
            if Emem.Dom1[i]!=0 and Emem.Dom2[j]!=0:
                rule=rules(i,j)
                value=min(Emem.Dom1[i], Emem.Dom2[j])     
                Outmem.Pos[rule]=max(value,Outmem.Pos[rule])

    #print("Pos="+str(Outmem.Pos))

def area_trapezoid(b,h):
    #Haromszog magassaga = 1
    #a-kisalap - kiszamitjuk
    #b-nagyalap
    #h-vagas amivel levagjuk a haromszog tetejet

    a = (1-h)*b
    area=(a+b)*h/2
    return area

#Sulyozott atlag
def Inf_Defuzz(Outmem):
    weighted_sum = 0
    total_weight = 0

    for rule, value in Outmem.Pos.items():
        # A szabály súlya maga a szabály értéke
        #weighted_sum += value * rule
        #total_weight += value

        if value > 0:
            area=area_trapezoid(2,value)
            weighted_sum += area * rule
            total_weight += area

    #print(weighted_sum)
    #print(total_weight)

    if total_weight != 0:
        defuzzified_value = weighted_sum / total_weight
        return defuzzified_value
    else:
        return None  
    


def Fuzzy_Control(e1, e2, Fuzzy_System):
    Fuzzyify(e1, e2, Fuzzy_System.Emem)
    Match(Fuzzy_System.Emem, Fuzzy_System.Outmem)
    return Inf_Defuzz(Fuzzy_System.Outmem)

def plot_membership_functions(Fuzzy_System):
    x = np.linspace(-10, 30, 500)
    
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    for i in range(5):
        y1 = [LeftAll(val, Fuzzy_System.Emem.Width1, Fuzzy_System.Emem.Center1[i]) if i == 0 else 
              RightAll(val, Fuzzy_System.Emem.Width1, Fuzzy_System.Emem.Center1[i]) if i == 4 else 
              Triangle(val, Fuzzy_System.Emem.Width1, Fuzzy_System.Emem.Center1[i]) for val in x]
        axs[0].plot(x, y1, label=f'Közeppont1[{i}] = {Fuzzy_System.Emem.Center1[i]}')
    
    axs[0].set_title('Tagsági függvények az 1. bemenetre')
    axs[0].legend()
    axs[0].grid(True)
    
    for i in range(5):
        y2 = [LeftAll(val, Fuzzy_System.Emem.Width2, Fuzzy_System.Emem.Center2[i]) if i == 0 else 
              RightAll(val, Fuzzy_System.Emem.Width2, Fuzzy_System.Emem.Center2[i]) if i == 4 else 
              Triangle(val, Fuzzy_System.Emem.Width2, Fuzzy_System.Emem.Center2[i]) for val in x]
        axs[1].plot(x, y2, label=f'Közeppont2[{i}] = {Fuzzy_System.Emem.Center2[i]}')
    
    axs[1].set_title('Tagsági függvények a 2. bemenetre')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

# Teszt
Fuzzy_System = Fuz_Sys()
Fuzzy_Init(Fuzzy_System)
e1 = 20
e2 = 3
print("Fuzzy control:", Fuzzy_Control(e1, e2, Fuzzy_System))

#plot_membership_functions(Fuzzy_System)
