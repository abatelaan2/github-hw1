import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.cm as cm
import matplotlib as mpl

empty = {}
df = pd.DataFrame(empty)

number= 10000
df["x"]= np.random.uniform(low=-1., high=1., size=(number,))
df["y"]= np.random.uniform(low=-1., high=1., size=(number,))
df["z"]= np.random.uniform(low=-1., high=1., size=(number,))

color_list=[]
n=0
while n<=len(df["x"])-1:
    function = df["x"][n]**2+df["y"][n]**2+df["z"][n]**2
    if function < 0.:
        function = 0.
        color_list.append(function)
    elif function > 1.:
        function = 1.
        color_list.append(function)
    else:
        color_list.append(function)
    n+=1

df["color"]=color_list

data_df = pd.read_excel(r"data.xlsx", sheet_name=0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

norm=mpl.colors.Normalize(vmin=0,vmax=1)
ax.scatter(df['x'],df['y'],df['z'], color = cm.autumn(df["color"]), s=1)
ax.plot(data_df['x'],data_df['y'],data_df['z'])
plt.show()
plt.savefig("colorfunction.png")