
import pandas as pd
import math


file = open('e_input.txt').read().split(' ')
prod1, prod2 = [int(x) for x in file]

df = pd.read_csv('purchase_data (1).csv')  
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


def similarity(prod1, prod2):
    common = find_common(prod1, prod2)
    if len(common) >=2:
        sum_mult =0
        sum_sq_1 = 0
        sum_sq_2 = 0 
        for member in common: 
            prod1_count = len(df[(df['memberID'] == member) & (df['productID'] == prod1)])
            prod2_count = len(df[(df['memberID'] == member) & (df['productID'] == prod2)])
            prod1_score = int(df[df['productID'] == prod1]['productScore'].unique())
            prod2_score = int(df[df['productID']== prod2]['productScore'].unique())

            sum_mult += (prod1_count - prod1_score ) * (prod2_count - prod2_score)   
            sum_sq_1 += (prod1_count - prod1_score)**2  
            sum_sq_2 += (prod2_count - prod2_score)**2  
        similarity = round( sum_mult / (math.sqrt(sum_sq_1) * math.sqrt(sum_sq_2)), 2)
        if similarity != 0:
            return similarity
        else:
            return 'NA'
    else:
        return 'NA'
print(similarity(prod1, prod2))