# -*- coding: utf-8 -*-

import geopandas
import pickle
import matplotlib.pyplot as plt

with open('world_data.pkl', 'rb') as f:
    gdf = pickle.load(f)
    
ax=gdf.plot(column='1/25/20', cmap='Reds', scheme='UserDefined', classification_kwds={'bins': [1, 10, 100, 500, 1000, 5000]}, 
            figsize=(25,10), legend=True, legend_kwds={'loc':'lower left'})
plt.show()

gdf.at['Trinidad and Tobago', '1/25/20'] = 1000

ax=gdf.plot(column='1/25/20', cmap='Reds', scheme='UserDefined', classification_kwds={'bins': [1, 10, 100, 500, 1000, 5000]}, 
            figsize=(25,10), legend=True, legend_kwds={'loc':'lower left'})
plt.show()