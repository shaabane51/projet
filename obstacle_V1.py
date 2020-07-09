import numpy as np
import matplotlib.colors as mlc
import matplotlib.pyplot as mlp
import matplotlib.pyplot as plt

abscisse = ['0', '1', '2', '3','4','5','6','7','8','9','10']
ordonnee = [9, 3, (), 3, 2,(),(),7,(),0]

abscisse = len(abscisse)
ordonnee_len = len(ordonnee)

img = np.zeros((abscisse, ordonnee_len), dtype=float)

for i, s in enumerate(ordonnee):
    img[s, i] = 1

figure, ax = mlp.subplots() 

color_map = mlc.LinearSegmentedColormap.from_list('ColorMap', [(1.000, 1.000, 1.000), (1, 0, 0)])
ax.imshow(img, cmap=color_map, interpolation='none')

grid_x_ticks = np.arange(1)
grid_y_ticks = np.arange(1)


ax.set_xticks(np.arange(0.5, 10, 1));
ax.set_yticks(np.arange(0.5, 10, 1));


plt.grid()
plt.show()
