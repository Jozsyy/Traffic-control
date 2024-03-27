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
        self.Emem = IN_MEM()
        self.Edotmem = IN_MEM()
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
    Fuzzy_System.Emem.Width = 0.05
    Fuzzy_System.Edotmem.Width = 0.025
    Fuzzy_System.Outmem.Width = 0.05
    for i in range(1, 8):
        Fuzzy_System.Emem.Center[i] = (i - 4) * Fuzzy_System.Emem.Width
        Fuzzy_System.Edotmem.Center[i] = (i - 4) * Fuzzy_System.Edotmem.Width
        Fuzzy_System.Outmem.Center[i] = (i - 4) * Fuzzy_System.Outmem.Width
    
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

def Match(Emem, Edotmem, Pos):
    for i in range(1, 8):
        if Emem.Dom[i] != 0:
            Pos[0] = i
            break
    for i in range(1, 8):
        if Edotmem.Dom[i] != 0:
            Pos[1] = i
            break

def Inf_Defuzz(Emem, Edotmem, Outmem, Pos):
    Atot = 0
    WAtot = 0
    for I in range(1, 3):
        for J in range(1, 3):
            if (Pos[0] + I - 1 <= 7) and (Pos[1] + J - 1 <= 7):
                Out_Index = Pos[0] + I - 1 + Pos[1] + J - 1
                if Out_Index < 5:
                    Out_Index = 5
                elif Out_Index > 11:
                    Out_Index = 11
                Out_Index = Out_Index - 4
                OutDom = MIN(Emem.Dom[Pos[0] + I - 1], Edotmem.Dom[Pos[1] + J - 1])
                Area = 2 * Outmem.Width * (OutDom - (OutDom * OutDom) / 2)
                Atot += Area
                WAtot += Area * Outmem.Center[Out_Index]

    return WAtot / Atot

def Fuzzy_Control(e, edot, Fuzzy_System):
    Pos = [0] * 2
    Fuzzyify(e, Fuzzy_System.Emem)
    Fuzzyify(edot, Fuzzy_System.Edotmem)
    Match(Fuzzy_System.Emem, Fuzzy_System.Edotmem, Pos)
    return Inf_Defuzz(Fuzzy_System.Emem, Fuzzy_System.Edotmem, Fuzzy_System.Outmem, Pos)

# Teszt
Fuzzy_System = Fuz_Sys()
Fuzzy_Init(Fuzzy_System)
e = 0.5
edot = 0.3
print("Fuzzy control:", Fuzzy_Control(e, edot, Fuzzy_System))