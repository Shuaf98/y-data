# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#How to solve:
#1) Make a dictionary of unique Ids, and update a dictionary (either with all products, or with True or Falses)
#2) Iterate through the date fram by unique Id's, select all products for each Id. Then, check if two products in one column.
import pandas as pd
import math
df = pd.read_csv('purchase_data (1).csv')
df['memberID'].describe


# %%
file = open("e_input.txt").read().strip().split(' ')
prod1, prod2 = [int(x) for x in file]


# %%
def find_common(prod1, prod2):
    prod1_df = df[df['productID'] == prod1]['memberID']
    prod2_df = df[df['productID'] == prod2]['memberID']
    result = set(prod2_df) & set(prod1_df)
    if len(result) == 0:
        return 0
    return result


# %%
print(sorted(find_common(prod1, prod2)))


# %%
def similarity(prod1, prod2):
    common = find_common(prod1, prod2)
    sum_mult=0
    sum_sq_1=0
    sum_sq_2=0  
    for member in common:
        prod1_count = len(df[(df['memberID']== member) & (df['productID']== prod1)])
        prod2_count = len(df[(df['memberID']== member) & (df['productID']== prod2)])
        prod1_score = int(df[df['productID'] == prod1].productScore.unique())
        prod2_score = int(df[df['productID'] == prod2].productScore.unique())
        sum_mult += (prod1_count - prod1_score) * (prod2_count - prod2_score)  
        sum_sq_1 += (prod1_count - prod1_score)**2  
        sum_sq_2 += (prod2_count - prod2_score)**2  
    similarity = sum_mult / (math.sqrt(sum_sq_1) * math.sqrt(sum_sq_2))
    return round(similarity, 2)
print(similarity(prod1, prod2))

