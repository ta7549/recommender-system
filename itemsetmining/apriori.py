import numpy as np
from initDataAnalysis import new_df
from mlxtend.frequent_patterns import apriori

# implementing apriori algorithm and generating itemsets with min support greater than 0.1
print("\n~~~~~~~~with 10% min support~~~~~~~~~~~~~~~")
frequentItemsets = apriori(new_df, min_support=0.1, use_colnames=True)
frequentItemsets['length'] = frequentItemsets['itemsets'].apply(lambda x: len(x))
print("\nAll itemsets generated using Apriori Algorithm: ")
print(frequentItemsets)

# generating itemsets of length 2 with min support greater than 0.1
print("\n Itemsets of length 2: ")
print(frequentItemsets[ (frequentItemsets['length'] == 2) &
                   (frequentItemsets['support'] >= 0.1) ])
# generating itemsets of length 3 with min support greater than 0.1
print("\n Itemsets of length 3: ")
print(frequentItemsets[ (frequentItemsets['length'] == 3) &
                   (frequentItemsets['support'] >= 0.1) ])


print("\n ~~~~~~~~~~~~~~~~~~~~~~~")


# Conviction Metric - RABBIT NIGHT LIGHT(1), RED TOADSTOOL LED NIGHT LIGHT(2)
# Conviction(𝑋→𝑌) = Support(𝑋:a)Support(𝑌¯:b) [num]/Support(𝑋&𝑌¯-A&B)[den]
# Performed the evaluation based on the above mentioned formulae

support_AB = np.logical_and(new_df['RABBIT NIGHT LIGHT'], new_df['RED TOADSTOOL LED NIGHT LIGHT']).mean()
support_A = new_df['RABBIT NIGHT LIGHT'].mean()
support_notB = 1.0 - new_df['RED TOADSTOOL LED NIGHT LIGHT'].mean()
support_A_notB_den = support_A - support_AB

support_num = (support_A * support_notB)
conviction = support_num / support_A_notB_den
print("Conviction value: %.4f " % conviction)


# implementing apriori algorithm and generating itemsets with min support greater than 0.01
print("~~~~~~~~with 1% min support~~~~~~~~~~~~~~~")

frequentItemsets = apriori(new_df, min_support=0.01, use_colnames=True)
frequentItemsets['length'] = frequentItemsets['itemsets'].apply(lambda x: len(x))
print("\nAll itemsets generated using Apriori Algorithm: ")
print(frequentItemsets)

# generating itemsets of length 2 with min support greater than 0.01
print("\n Itemsets of length 2: ")
print(frequentItemsets[ (frequentItemsets['length'] == 2) &
                   (frequentItemsets['support'] >= 0.01) ])

# generating itemsets of length 3 with min support greater than 0.01
print("\n Itemsets of length 3: ")
print(frequentItemsets[ (frequentItemsets['length'] == 3) &
                   (frequentItemsets['support'] >= 0.01) ])

print("\n ~~~~~~~~~~~~~~~~~~~~~~~")

# generating itemsets of length 2 after removing POSTAGE item with min support greater than 0.01
print("\n Itemsets of length 2 after removing POSTAGE item: ")
print(frequentItemsets[~frequentItemsets["itemsets"].str.contains("POSTAGE", regex=False) &
                (frequentItemsets['length'] == 2)].head())

# generating itemsets of length 3 after removing POSTAGE item with min support greater than 0.01
print("\n Itemsets of length 3 after removing POSTAGE item: ")
print(frequentItemsets[~frequentItemsets["itemsets"].str.contains("POSTAGE", regex=False) &
                (frequentItemsets['length'] == 3)].head())



