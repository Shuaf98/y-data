# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import os
df = pd.read_csv('purchase_data.csv')
input = open('e1_input.txt').read()
prod1, prod2 = input.split()

members = list(df['memberID'].unique())


# %%
all_members = []
for x in members:
    test = df[df['memberID'] == x]
    if int(prod1) in test['productID'].values and int(prod2) in test['productID'].values:
        all_members.append(x)
if all_members != []:
    for x in all_members:
        print(x)
else:
    print( 0)



# %%
