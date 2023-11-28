import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Import
data = pd.read_table('hipparcos_200.txt', delimiter=';', skiprows=[1,2])
print(data.head())

# , En ' ' vervangen
data['Vmag'] = data['Vmag'].str.replace(' ', '')
data['Vmag'] = data['Vmag'].str.replace(',', '.')

data['Plx'] = data['Plx'].str.replace(' ', '')
data['Plx'] = data['Plx'].str.replace(',', '.')

data['BTmag'] = data['BTmag'].str.replace(' ', '')
data['BTmag'] = data['BTmag'].str.replace(',', '.')

data['VTmag'] = data['VTmag'].str.replace(' ', '')
data['VTmag'] = data['VTmag'].str.replace(',', '.')

# NaN en float
data['Vmag'] = pd.to_numeric(data['Vmag'], errors='coerce')
data['Plx'] = pd.to_numeric(data['Plx'], errors='coerce')
data['BTmag'] = pd.to_numeric(data['BTmag'], errors='coerce')
data['VTmag'] = pd.to_numeric(data['VTmag'], errors='coerce')

# Data
vmag = data['Vmag']
plx = data['Plx']
btmag = data['BTmag']
vtmag = data['VTmag']

# Plotten
plt.scatter((vmag-5*(np.log10((1000/plx)/10))), (btmag-vtmag))
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('Absolute magnitude')
plt.title('HR-Diagram')
plt.show()

# Debug
print(data.head())