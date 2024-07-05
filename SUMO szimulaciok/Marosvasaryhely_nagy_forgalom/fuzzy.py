import matplotlib.pyplot as plt
import numpy as np

class InputMembership:
    def __init__(self, width1, center1, width2, center2):
        self.width1 = width1
        self.center1 = center1
        self.dom1 = [0.0] * 5
        self.width2 = width2
        self.center2 = center2
        self.dom2 = [0.0] * 5

    def left_all(self, u, w, c):
        if u < c:
            return 1.0
        else:
            return max(0, (1 - (u - c) / w))

    def right_all(self, u, w, c):
        if u >= c:
            return 1.0
        else:
            return max(0, (1 - (c - u) / w))

    def triangle(self, u, w, c):
        if u >= c:
            return max(0, (1 - (u - c) / w))
        else:
            return max(0, (1 - (c - u) / w))

    def fuzzify(self, U1, U2):
        self.dom1[0] = self.left_all(U1, self.width1, self.center1[0])
        self.dom2[0] = self.left_all(U2, self.width2, self.center2[0])
        for i in range(1, 4):
            self.dom1[i] = self.triangle(U1, self.width1, self.center1[i])
            self.dom2[i] = self.triangle(U2, self.width2, self.center2[i])
        self.dom1[4] = self.right_all(U1, self.width1, self.center1[4])
        self.dom2[4] = self.right_all(U2, self.width2, self.center2[4])

class OutputMembership:
    def __init__(self):
        self.pos = {-4: 0, -2: 0, 0: 0, 2: 0, 4: 0}

    @staticmethod
    def area_trapezoid(b, h):
        #Haromszog magassaga = 1
        #a-kisalap - kiszamitjuk
        #b-nagyalap
        #h-vagas amivel levagjuk a haromszog tetejet
        a = (1 - h) * b
        area = (a + b) * h / 2
        return area

    def inf_defuzz(self):
        weighted_sum = 0
        total_weight = 0

        for rule, value in self.pos.items():
            # A szabály súlya maga a szabály értéke
            #weighted_sum += value * rule
            #total_weight += value
            if value > 0:
                area = self.area_trapezoid(2, value)
                weighted_sum += area * rule
                total_weight += area

        if total_weight != 0:
            return weighted_sum / total_weight
        else:
            return None

class FuzzySystem:
    def __init__(self):
        width1 = 5
        width2 = 2
        center1 = [0.0] * 5
        center2 = [0.0] * 5

        for i in range(0, 5):
            center1[i] = 5 * i
            center2[i] = 2 * i - 4

        self.inmem = InputMembership(width1, center1, width2, center2)
        self.outmem = OutputMembership()

    @staticmethod   #Nem fuggnek az osztaly peldanyaitol vagy osztaly belso allapotatol
    def rules(i, j):    #i jeloli a sor hosszat, j pedig a valtozast
        rules_matrix = [
            [-4, -4, -2, 0, 2],
            [-4, -2, 0, 0, 2],
            [-2, 0, 2, 2, 4],
            [0, 2, 2, 4, 4],
            [2, 2, 4, 4, 4]
        ]
        return rules_matrix[i][j]

    def match(self):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.inmem.dom1[i] != 0 and self.inmem.dom2[j] != 0:
                    rule = self.rules(i, j)
                    value = min(self.inmem.dom1[i], self.inmem.dom2[j])
                    self.outmem.pos[rule] = max(value, self.outmem.pos[rule])

    def fuzzy_control(self, e1, e2):
        self.inmem.fuzzify(e1, e2)
        self.match()
        return self.outmem.inf_defuzz()

    def plot_input_membership_functions(self):
        x = np.linspace(-10, 30, 500)

        fig, axs = plt.subplots(2, 1, figsize=(12, 8))

        val1=["NR", "R", "K", "H", "NH"]
        for i in range(5):
            y1 = [self.inmem.left_all(val, self.inmem.width1, self.inmem.center1[i]) if i == 0 else
                  self.inmem.right_all(val, self.inmem.width1, self.inmem.center1[i]) if i == 4 else
                  self.inmem.triangle(val, self.inmem.width1, self.inmem.center1[i]) for val in x]
            axs[0].plot(x, y1, label=f'{val1[i]} = {self.inmem.center1[i]}')

        axs[0].set_title('Tagsági függvények az első bemenetre')
        axs[0].legend()
        axs[0].grid(True)
        axs[0].set_xlabel("Járművek száma", loc="right")

        val2=["NCS", "CS", "NV", "N", "NN"]
        for i in range(5):
            y2 = [self.inmem.left_all(val, self.inmem.width2, self.inmem.center2[i]) if i == 0 else
                  self.inmem.right_all(val, self.inmem.width2, self.inmem.center2[i]) if i == 4 else
                  self.inmem.triangle(val, self.inmem.width2, self.inmem.center2[i]) for val in x]
            axs[1].plot(x, y2, label=f'{val2[i]} = {self.inmem.center2[i]}')

        axs[1].set_title('Tagsági függvények a második bemenetre')
        axs[1].legend()
        axs[1].grid(True)
        axs[1].set_xlabel("Járművek számának változása", loc="right")
        
        plt.tight_layout()
        plt.show()

    def plot_output_membership_functions(self):
        x = np.linspace(-10, 10, 500)
        fig, ax = plt.subplots(figsize=(10, 5))

        val=["NCS", "CS", "NV", "N", "NN"]
        i=0
        for pos in self.outmem.pos.keys():
            y = [self.inmem.left_all(val, 2, pos) if pos == -4 else
                 self.inmem.right_all(val, 2, pos) if pos == 4 else
                 self.inmem.triangle(val, 2, pos) for val in x]
            ax.plot(x, y, label=f'{val[i]} = {pos}')
            i += 1

        ax.set_title('Kimeneti tagsági függvények')
        ax.legend()
        ax.grid(True)

        plt.xlabel("Zöld időtartam módosítása [s]", loc="right")
        plt.tight_layout()
        plt.show()

    def plot_input_rule_cut_membership_functions(self, input_values, input_points):
        x = np.linspace(-10, 30, 500)
        
        fig, axs = plt.subplots(2, 1, figsize=(12, 8))

        val1=["NR", "R", "K", "H", "NH"]
        for i in range(5):
            y1 = [self.inmem.left_all(val, self.inmem.width1, self.inmem.center1[i]) if i == 0 else
                self.inmem.right_all(val, self.inmem.width1, self.inmem.center1[i]) if i == 4 else
                self.inmem.triangle(val, self.inmem.width1, self.inmem.center1[i]) for val in x]
            cut_y1 = [min(y1_val, input_values[0][i]) for y1_val in y1]
            axs[0].plot(x, y1, label=f'{val1[i]} = {self.inmem.center1[i]}')
            axs[0].fill_between(x, cut_y1, color='black', alpha=0.5)
        
        axs[0].axvline(input_points[0], color='red', linestyle='--', linewidth=1)
        axs[0].set_title('Levágott tagsági függvények az első bemenetre')
        axs[0].legend()
        axs[0].grid(True)
        axs[0].set_xlabel("Járművek száma", loc="right")

        val2=["NCS", "CS", "NV", "N", "NN"]
        for i in range(5):
            y2 = [self.inmem.left_all(val, self.inmem.width2, self.inmem.center2[i]) if i == 0 else
                self.inmem.right_all(val, self.inmem.width2, self.inmem.center2[i]) if i == 4 else
                self.inmem.triangle(val, self.inmem.width2, self.inmem.center2[i]) for val in x]
            cut_y2 = [min(y2_val, input_values[1][i]) for y2_val in y2]
            axs[1].plot(x, y2, label=f'{val2[i]} = {self.inmem.center2[i]}')
            axs[1].fill_between(x, cut_y2, color='black', alpha=0.5)
        
        axs[1].axvline(input_points[1], color='red', linestyle='--', linewidth=1)
        axs[1].set_title('Levágott tagsági függvények a második bemenetre')
        axs[1].legend()
        axs[1].grid(True)
        axs[1].set_xlabel("Járművek számának változása", loc="right")

        plt.tight_layout()
        plt.show()

    def plot_output_rule_cut_membership_functions(self):
        x = np.linspace(-10, 10, 500)
        
        fig, ax = plt.subplots(figsize=(10, 5))

        val = ["NCS", "CS", "NV", "N", "NN"]
        i = 0
        for pos, dom_value in self.outmem.pos.items():
            y = [self.inmem.left_all(val, 2, pos) if pos == -4 else
                self.inmem.right_all(val, 2, pos) if pos == 4 else
                self.inmem.triangle(val, 2, pos) for val in x]
            cut_y = [min(y_val, dom_value) for y_val in y]
            ax.plot(x, y, label=f'{val[i]} = {pos}')
            ax.fill_between(x, cut_y, color='black', alpha=0.5)
            i += 1

        ax.set_title('Levágott kimeneti tagsági függvények')
        ax.legend()
        ax.grid(True)

        plt.xlabel("Zöld időtartam módosítása [s]", loc="right")
        plt.tight_layout()
        plt.show()

'''
# Teszt
fuzzy_system = FuzzySystem()
e1=13
e2=-2
print(fuzzy_system.fuzzy_control(e1, e2))
fuzzy_system.plot_input_membership_functions()
fuzzy_system.plot_output_membership_functions()
input_values = (fuzzy_system.inmem.dom1, fuzzy_system.inmem.dom2)
input_points = (e1,e2)
fuzzy_system.plot_input_rule_cut_membership_functions(input_values, input_points)
fuzzy_system.plot_output_rule_cut_membership_functions()
'''