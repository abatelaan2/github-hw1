import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.cm as cm
import matplotlib as mpl

# Create dataframe
empty = {}
df = pd.DataFrame(empty)

# Create a large number of random points in 3D space that will represent color
number= 10000
df["x"]= np.random.uniform(low=-1., high=1., size=(number,))
df["y"]= np.random.uniform(low=-1., high=1., size=(number,))
df["z"]= np.random.uniform(low=-1., high=1., size=(number,))

# Specify the function to have values between 0 and 1
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

# Import data to draw lines (Could be used to draw molecules later on)
data_df = pd.read_excel(r"data.xlsx", sheet_name=0)

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

norm=mpl.colors.Normalize(vmin=0,vmax=1)
ax.scatter(df['x'],df['y'],df['z'], color = cm.autumn(df["color"]), s=1)
ax.plot(data_df['x'],data_df['y'],data_df['z'])
ax.set_title('3D Color Function')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
plt.savefig("colorfunction.png")