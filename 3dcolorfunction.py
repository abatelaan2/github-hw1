import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.cm as cm
import matplotlib as mpl

empty = {}
df = pd.DataFrame(empty)

step=0.1
x_list=[]
y_list=[]
z_list=[]
n=-1
while n<=1:
    x = n
    m=-1
    while m<=1:
        y = m
        l=-1
        while l<=1:
            z = l
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
            l+=step
        m+=step
    n+=step

df["x"]=x_list
df["y"]=y_list
df["z"]=z_list

color_list=[]
n=0
while n<=len(df["x"])-1:
    function = df["x"][n]**2+df["y"][n]**2+df["z"][n]**2
    if function < 0:
        function = 0
        color_list.append(function)
    elif function > 1:
        function = 1
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