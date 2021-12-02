# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import os
os.chdir(r"C:\Users\sfrie\Ydata_practice\Test_2")


# %%
df= pd.read_csv('F1_schools_done.csv')

 #[int(x.strip('%')) for x in df['Average Proficiency Score']]
df['Average Proficiency Score'] = df['Average Proficiency Score'].str.replace('%', '').apply(pd.to_numeric)
df['District'].dtype
input = open('f3_input.txt').read().split()
input = list(map(int, input))


# %%
df = df[(df['District'] == input[0]) & (df['Average Proficiency Score'] >= input[1]) & (df['Average Proficiency Score'] <= input[2])]
df.head()


# %%
print(round(df['Student Achievement Rating'].mean(), 2))


# %%



# %%
df


