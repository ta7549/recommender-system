from initDataAnalysis import new_df
from mlxtend.frequent_patterns import fpgrowth

# implementing fpgrowth algorithm and generating itemsets with min support greater than 0.05
frequentItemsets2 = fpgrowth(new_df, min_support = 0.05, use_colnames=True)
frequentItemsets2['length'] = frequentItemsets2['itemsets'].apply(lambda x: len(x))
print("\nAll itemsets generated using Fpgrowth Algorithm: ")
print(frequentItemsets2)

# generating itemsets of length 2
print("\n Itemsets of length 2: ")
print(frequentItemsets2[ (frequentItemsets2['length'] == 2) &
                   (frequentItemsets2['support'] >= 0.1) ])

# implementing fpgrowth algorithm and generating itemsets with min support greater than 0.01
frequentItemsets2 = fpgrowth(new_df, min_support=0.01, use_colnames=True)
frequentItemsets2['length'] = frequentItemsets2['itemsets'].apply(lambda x: len(x))
print(frequentItemsets2)

# generating itemsets of length 2 that do not contain postage item
print(frequentItemsets2[~frequentItemsets2["itemsets"].str.contains("POSTAGE", regex=False) &
                (frequentItemsets2['length'] == 2)].head())
