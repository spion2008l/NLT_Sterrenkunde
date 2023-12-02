import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math
import tkinter as tk
from tkinter.filedialog import askopenfilename


#Import
tk.Tk().withdraw()

fn = askopenfilename()

data = pd.read_table(fn, delimiter=';', skiprows=[1,2], comment='#')

#NaN en float
data['Vmag'] = pd.to_numeric(data['Vmag'], errors='coerce')
data['Plx'] = pd.to_numeric(data['Plx'], errors='coerce')
data['B-V'] = pd.to_numeric(data['B-V'], errors='coerce')

#Data
vmag = data['Vmag']
plx = data['Plx']
BV = data['B-V']

#Plotten
fig, ax = plt.subplots(figsize=(9,6))

ax.scatter((BV), (vmag-5*(np.log10((1000/plx)/10))), s=2)
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('Absolute magnitude')
plt.title('HR-Diagram')

#Slider as
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.05])

#Point Size
def update_size(val):
    scatter = ax.collections[-1]
    scatter.set_sizes([val] * len(scatter.get_sizes()))
    plt.draw()

slider = Slider(ax_slider, "Point Size:", valmin=0.001, valmax=0.1, valinit=0.01, valstep=0.001)
slider.on_changed(update_size)

plt.show()
