import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv(r'C:\University\Traffic-control\SUMO szimulaciok\Marosvasaryhely_nagy_forgalom\Meresek\kozpont.txt', header=None, names=['value'])
data2 = pd.read_csv(r'C:\University\Traffic-control\SUMO szimulaciok\Marosvasaryhely_nagy_forgalom\Meresek\kozpont_fuzzy.txt', header=None, names=['value'])

data1['time'] = data1.index*2.5+2.5
data2['time'] = data2.index*2.5+2.5

plt.figure(figsize=(10, 5))
plt.plot(data1['time'], data1['value'], marker='o', linestyle='solid', label='Fix időzítéssel')
plt.plot(data2['time'], data2['value'], 'red', marker='o', linestyle='solid', label='Fuzzy szabályozással')

plt.xlabel('Idő [min]')
plt.ylabel('Járművek száma')
plt.title('Kereszteződésben 5 percenként áthaladt járművek száma')
plt.grid(True)
plt.legend()

plt.show()