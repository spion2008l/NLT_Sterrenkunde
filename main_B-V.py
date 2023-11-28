import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Import
data = pd.read_table('asu_unlimited.txt', delimiter=';', skiprows=[1,2])
print(data.head())

# , En ' ' vervangen
data['Vmag'] = data['Vmag'].str.replace(' ', '')
data['Vmag'] = data['Vmag'].str.replace(',', '.')

data['Plx'] = data['Plx'].str.replace(' ', '')
data['Plx'] = data['Plx'].str.replace(',', '.')

data['B-V'] = data['B-V']
data['B-V'] = data['B-V']

# NaN en float
data['Vmag'] = pd.to_numeric(data['Vmag'], errors='coerce')
data['Plx'] = pd.to_numeric(data['Plx'], errors='coerce')
data['B-V'] = pd.to_numeric(data['B-V'], errors='coerce')

# Data
vmag = data['Vmag']
plx = data['Plx']
BV = data['B-V']

# Plotten
plt.scatter((BV), (vmag-5*(np.log10((1000/plx)/10))), s=1)
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('Absolute magnitude')
plt.title('HR-Diagram')
plt.show()