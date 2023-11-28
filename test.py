import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the txt file from windows
data = pd.read_table('hipparcos_200.txt', delimiter=';')
print(data.head())