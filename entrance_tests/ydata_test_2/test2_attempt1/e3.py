import pandas as pd
import os
import numpy as np

os.chdir(r"C:\Users\sfrie\Ydata_practice\Test_2")
df = pd.read_csv('purchase_data.csv')

members = list(df['memberID'].unique())

def find_common(prod1, prod2):
    all_members = []
    for x in members:
        test = df[df['memberID'] == x]
        if int(prod1) in test['productID'].values and int(prod2) in test['productID'].values:
            all_members.append(x)
    if all_members != []:
        return all_members
    else:
        return 0

def similarity (product_1, product_2):  
    common = find_common(product_1, product_2) 
    sum_mult =0
    sum_sq_1=0
    sum_sq_2=0
    for member in common:  
        prod1_count = len(df[(df['memberID'] == member) & (df['productID'] == int(product_1))])
        prod2_count = len(df[(df['memberID'] == member) & (df['productID'] == int(product_2))])
        prod1_score = int(df[df['productID'] == int(product_1)]['productScore'].unique())
        prod2_score = int(df[df['productID'] == int(product_2)]['productScore'].unique())
        sum_mult += (prod1_count - prod1_score) *  (prod2_count - prod2_score)  
        sum_sq_1 += pow((prod1_count - prod1_score), 2)
        sum_sq_2 += pow((prod2_count - prod2_score), 2)
    similarity = sum_mult / (np.sqrt(sum_sq_1) * np.sqrt(sum_sq_2))
    if similarity != np.nan:
        return round(similarity, 2)
    else:
        return 'NA'


def predicted_count (new_member, candidate_product): #candidate product is a loop of each product in the excel
    sum_mult = 0
    sum_similarities = 0
    predicted_count = 0
 
    for line in new_member:
        bought_product, amount = int(line[0]), int(line[1])
        sim = similarity(candidate_product, bought_product)

        sum_mult += sim * amount  
        sum_similarities += abs(sim)  
    predicted_count = (sum_mult / sum_similarities)
    return predicted_count
        



new_member = open(r"C:\Users\sfrie\Ydata_practice\Test_2\e3_input").readlines()
new_member = [x.split() for x in new_member]
candidate_products = df['productID'].unique()
dict = {}
for candidate_product in candidate_products:
    dict[candidate_product] = predicted_count(new_member, candidate_product)
print(max(dict.sortedKeys, key = dict.get))


    
     


