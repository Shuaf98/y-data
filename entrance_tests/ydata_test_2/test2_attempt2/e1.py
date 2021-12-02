# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#How to solve:
#1) Make a dictionary of unique Ids, and update a dictionary (either with all products, or with True or Falses)
#2) Iterate through the date fram by unique Id's, select all products for each Id. Then, check if two products in one column.
import pandas as pd
df = pd.read_csv('purchase_data (1).csv')

file = open('e_input.txt').read().split(' ')
prod1, prod2 = [int(x) for x in file]

# %%
#memberID is int64 type. We need to convert our str file into int.


# %%

# def find_common(prod1, prod2):
#     prod1_frame = df[df.productID == prod1].memberID
#     prod2_frame = df[df.productID == prod2].memberID
#     result = set(prod1_frame) & set(prod2_frame)
#     if len(result) == 0:
#         return [0]
#     return result


#%%
def find_common(prod1, prod2):
    checked_customers = set()
    customers = []
    for id in df['memberID'].unique():
        if id not in customers:
            check_frame = df[df['memberID'] == id]
            
            if prod1 in check_frame['productID'].to_list() and prod2 in check_frame['productID'].to_list():
                customers.append(id)
            checked_customers.add(id)
    if len(customers) == 0:
        return [0]
    else:
        return sorted(customers)


# df = df[['memberID', 'productID']]
for x in find_common(prod1, prod2):
    print(x)



