import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv(r'C:\University\Traffic-control\SUMO szimulaciok\Marosvasaryhely_nagy_forgalom\kozpont.txt', header=None, names=['value'])
data2 = pd.read_csv(r'C:\University\Traffic-control\SUMO szimulaciok\Marosvasaryhely_nagy_forgalom\kozpont_fuzzy.txt', header=None, names=['value'])

data1['time'] = data1.index
data2['time'] = data2.index

plt.figure(figsize=(10, 5))
plt.plot(data1['time'], data1['value'], label='Alap beállítással')
plt.plot(data2['time'], data2['value'], 'red', label='Fuzzy szabályozással')

plt.xlabel('Idő [s]')
plt.ylabel('Járművek száma')
plt.title('Kereszteződésen áthaladt járművek')
plt.grid(True)
plt.legend()

plt.show()