from create_3d_gif import pd_to_gif
import pandas as pd

# example 1
data = pd.read_excel('example1.xlsx', index_col=0)
pd_to_gif(data,['x','y','z'],'example_gif_1','colors')

# example 2
data = pd.read_excel('example2.xlsx', index_col=0)
pd_to_gif(data,['x','y','z'],'example_gif_2','colors')

# example 3
data = pd.read_excel('example3.xlsx', index_col=0)
pd_to_gif(data,['x','y','z'],'example_gif_3','colors')
