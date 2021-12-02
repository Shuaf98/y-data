import pandas as pd
import math
file = open('input.txt').read().strip().split('\n')
id, month = [int(x) for x in file]


df = pd.read_csv('calls_data.csv')

# %%
def usage(id, month):
    df = pd.read_csv('calls_data.csv')
    df = df[(df['user_id'] == id) & (df['month'] == month)]
    df['duration'] = df['duration'].apply(math.ceil)
    sum = df['duration'].sum()
    if sum != 0:
        return sum
    return 0
print(usage(id, month))

# %%

# %%
