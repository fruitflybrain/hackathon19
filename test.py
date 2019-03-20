import glob
import pandas as pd

files = glob.glob('swc\\*')
df = pd.DataFrame(columns=['ID','type','x','y','z','radius','parent','neuron_class'])

for file in files:
    data = pd.read_csv(file, names=['ID','type','x','y','z','radius','parent'],sep=' ')
    data['neuron_class'] = file[4:-4]
    df = df.append(pd.DataFrame(data))

print(df.groupby('type')['neuron_class'].nunique())

df.to_csv('neuron_csv.csv')

print(df.head(100))