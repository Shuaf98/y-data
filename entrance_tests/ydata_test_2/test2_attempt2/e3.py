
import pandas as pd
import math


# file = open('e_input.txt').read().strip().split(' ')
# prod1, prod2 = [int(x) for x in file]

df = pd.read_csv('purchase_data (1).csv')  

csv = open("purchase_data (1).csv").read().strip().split('\n')
members = []
products = []
scores = []
productCount = {}
productScore = {}
for line in csv[1:]:
    line = line.split(',')
    memid = int(line[1])
    prodid = int(line[2])
    productScore[prodid] = int(line[3])
    
    count = productCount.get((memid, prodid), 0)
    productCount[(memid, prodid)] = count+1

    members.append(memid)
    products.append(prodid)
    scores.append(scores)

#%%
def find_common(prod1, prod2):
    customers = []
    for id in set(members):
        if (id, prod1) in productCount.keys() and (id, prod2) in productCount.keys():
            customers.append(id)
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
        for member in sorted(common): 
            sum_mult += (productCount[(member, prod1)] - productScore[prod1]) * (productCount[(member, prod2)] - productScore[prod2]) 
            sum_sq_1 += (productCount[(member, prod1)] - productScore[prod1])**2  
            sum_sq_2 += (productCount[(member, prod2)] - productScore[prod2])**2
        similarity = sum_mult / (math.sqrt(sum_sq_1) * math.sqrt(sum_sq_2))
        if similarity != 0:
            return similarity
        else:
            return 'NA'
    else:
        return 'NA'


def input(new_member):
    bought_products = []
    for line in new_member:
        line = line.split(' ')
        bought_product, prod_count = [int(x) for x in line]
        bought_products.append(bought_product)
    return bought_products

def predict_count(bought_products):   
    for candidate_product in products:
        sum_mult = 0
        sum_similarities = 0
        for line in new_member:
            line = line.split(' ')
            bought_product, prod_count = [int(x) for x in line]

            similar_result = similarity(candidate_product, bought_product)
            if similar_result == 'NA':
                break
            if bought_product != candidate_product:
                sum_mult += similar_result * prod_count  
                sum_similarities += abs(similar_result)
        if sum_similarities == 0:
            predicted_count == 0  
        else:
            predicted_count = (sum_mult / sum_similarities)
        if predicted_count >0 and candidate_product not in bought_products: 
            all_counts[candidate_product] = predicted_count
    return max(all_counts, key = all_counts.get)


new_member = open('e3_input.txt').read().strip().split('\n')
products = set(list(df['productID']))
all_counts = {}
print(predict_count(input(new_member)))
