class IN_MEM:
    def __init__(self):
        self.Width = 0.0
        self.Center = [0.0] * 9
        self.Dom = [0.0] * 9

class OUT_MEM:
    def __init__(self):
        self.Width = 0.0
        self.Center = [0.0] * 9

class Fuz_Sys:
    def __init__(self):
        self.street1 = IN_MEM()
        self.street2 = IN_MEM()
        #4 bemenet - street 1,2,3,4
        self.street3 = IN_MEM()
        self.street4 = IN_MEM()
        self.green_time = OUT_MEM()

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
    Fuzzy_System.street1.Width = 0.05
    Fuzzy_System.street2.Width = 0.025
    Fuzzy_System.street3.Width = 0.15
    Fuzzy_System.street4.Width = 0.1
    Fuzzy_System.green_time.Width = 0.05
    for i in range(1, 8):
        Fuzzy_System.street1.Center[i] = (i - 4) * Fuzzy_System.street1.Width
        Fuzzy_System.street2.Center[i] = (i - 4) * Fuzzy_System.street2.Width
        Fuzzy_System.street3.Center[i] = (i - 4) * Fuzzy_System.street3.Width
        Fuzzy_System.street4.Center[i] = (i - 4) * Fuzzy_System.street4.Width
        Fuzzy_System.green_time.Center[i] = (i - 4) * Fuzzy_System.green_time.Width
    
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
    
def Fuzzyify(U, Mem):
    Mem.Dom[1] = LeftAll(U, Mem.Width, Mem.Center[1])
    for i in range(2, 7):
        Mem.Dom[i] = Triangle(U, Mem.Width, Mem.Center[i])
    Mem.Dom[7] = RightAll(U, Mem.Width, Mem.Center[7])

def Match(street1, street2, street3, street4, Pos):
    for i in range(1, 8):
        if street1.Dom[i] != 0:
            Pos[0] = i
            break
    for i in range(1, 8):
        if street2.Dom[i] != 0:
            Pos[1] = i
            break
    for i in range(1, 8):
        if street3.Dom[i] != 0:
            Pos[2] = i
            break
    for i in range(1, 8):
        if street4.Dom[i] != 0:
            Pos[3] = i
            break

def Inf_Defuzz(street1, street2, street3, street4, green_time, Pos):
    Atot = 0
    WAtot = 0
    for I in range(1, 5):
        for J in range(1, 5):
            if (Pos[0] + I - 1 <= 7) and (Pos[1] + J - 1 <= 7):
                Out_Index = Pos[0] + I - 1 + Pos[1] + J - 1
                if Out_Index < 5:
                    Out_Index = 5
                elif Out_Index > 11:
                    Out_Index = 11
                Out_Index = Out_Index - 4
                OutDom = min(street1.Dom[Pos[0] + I - 1], street2.Dom[Pos[1] + J - 1], street3.Dom[Pos[2] + I - 1], street4.Dom[Pos[1] + J - 1])
                Area = 2 * green_time.Width * (OutDom - (OutDom * OutDom) / 2)
                Atot += Area
                WAtot += Area * green_time.Center[Out_Index]

    return WAtot / Atot

def Fuzzy_Control(s1, s2, s3, s4, Fuzzy_System):
    Pos = [0] * 4
    Fuzzyify(s1, Fuzzy_System.street1)
    Fuzzyify(s2, Fuzzy_System.street2)
    Fuzzyify(s3, Fuzzy_System.street3)
    Fuzzyify(s4, Fuzzy_System.street4)
    Match(Fuzzy_System.street1, Fuzzy_System.street2,Fuzzy_System.street3, Fuzzy_System.street4, Pos)
    return Inf_Defuzz(Fuzzy_System.street1, Fuzzy_System.street2,Fuzzy_System.street3, Fuzzy_System.street4, Fuzzy_System.green_time, Pos)

# Teszt
Fuzzy_System = Fuz_Sys()
Fuzzy_Init(Fuzzy_System)
s1 = 0.5
s2 = 0.3
s3 = 0.2
s4 = 0.4
print("Fuzzy control:", Fuzzy_Control(s1, s2, s3, s4, Fuzzy_System))