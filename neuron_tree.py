import glob
import pandas as pd
import networkx as nx
import math
import matplotlib.pyplot as plt

#collect neuron swc files
files = glob.glob('swc\\*')
df = pd.DataFrame(columns=['ID','type','x','y','z','radius','parent','neuron_class'])

#create combined dataframe
for i,file in enumerate(files):
    data = pd.read_csv(file, names=['ID','type','x','y','z','radius','parent'],sep=' ')
    data['neuron_class'] = file[4:-4]
    #replace -1 for parent with (-1 - index) to differentiate neurons
    data.loc[data['parent'] == -1, 'parent'] = -1-i
    df = df.append(pd.DataFrame(data))

#df.to_csv('neuron_csv.csv')
print(df.head(5))

#create graph for all neurons and neurite segments
G = nx.Graph()
for index,node in df.iterrows(): 
    parent = df[df['ID']==node['parent']]
    if not parent.empty:
        #calculate length via xyz
        l = math.sqrt((parent['x'].values[0]-node['x'])**2+(parent['y'].values[0]-node['y'])**2+(parent['z'].values[0]-node['z'])**2)
        G.add_edge(node['ID'], node['parent'], length=l)

#this will create the tree for ID:-1, the first parsed neurons' parent, based on the graph
#after the tree is created, the radius can be calculated, along with the electrical properties and fed back into the dataframe
tree = nx.bfs_tree(G, df[df['parent']==-1]['ID'].values[0])
#tree needs to be spread out more, its hard to see
nx.draw(tree)
plt.savefig('bfs_image.png')


#unfinished:
#calculate radius based on tree depth
#calculate resistance/conductance
#Ri = 60 ohm-cm, R = Ri*L/(pi*r^2)
#rm = Rm/(2*pi*r), Rm = 40000 ohm-cm^2
#cm = Cm*2*pi*r, Cm = 1uF/cm^2
#(https://en.wikipedia.org/wiki/Cable_theory)