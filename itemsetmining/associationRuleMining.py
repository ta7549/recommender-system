import numpy as np
import pandas as pd
import math
import random
import seaborn as sns
import pandas_profiling as pp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from apriori import frequentItemsets
from fpgrowth import frequentItemsets2
from mlxtend.frequent_patterns import apriori,association_rules, fpgrowth


print("~~~~~~~~~~~~~~~~~~~Rules generated using Apriori~~~~~~~~~~~~~~~~~~~")
rules = association_rules(frequentItemsets, metric="lift", min_threshold=1.2)
rules["antecedents_length"] = rules["antecedents"].apply(lambda x: len(x))
rules["consequents_length"] = rules["consequents"].apply(lambda x: len(x))
print("\n Association Rules after sorting them by lift metric")
print(rules.sort_values("lift",ascending=False))

print("\n Association Rules after sorting them by Confidence metric")
print(rules.sort_values("confidence",ascending=False))

print("\n Removing Association Rules which contain POSTAGE as a consequent or antecedent")
print(rules[~rules["consequents"].str.contains("POSTAGE", regex=False) &
      ~rules["antecedents"].str.contains("POSTAGE", regex=False)].sort_values("confidence", ascending=False).head(7))

print(rules[~rules["antecedents"].str.contains("POSTAGE", regex=False)].sort_values("consequents_length", ascending=True).head(7))

print(rules[~rules["antecedents"].str.contains("POSTAGE", regex=False) &
     rules["consequents"].str.contains("POSTAGE", regex=False)].sort_values("consequents_length", ascending=True).head(7))

print(rules[rules["antecedents"].str.contains("POSTAGE", regex=False) &
     ~rules["consequents"].str.contains("POSTAGE", regex=False)].sort_values("antecedents_length", ascending=True).head(7))

print(rules[~rules["consequents"].str.contains("POSTAGE", regex=False)].sort_values("confidence", ascending=False).head(7))

print(rules[~rules["consequents"].str.contains("POSTAGE", regex=False) &
      ~rules["antecedents"].str.contains("POSTAGE", regex=False)].sort_values("antecedents_length", ascending=True).head(7))

print("~~~~~~~~~~~~~~~~~~~~~Rules generated using FPGROWTH~~~~~~~~~~~~~~~~~")

rules = association_rules(frequentItemsets2, metric="confidence", min_threshold=0.2).iloc[:,:-3]
rules["antecedents_length"] = rules["antecedents"].apply(lambda x: len(x))
rules["consequents_length"] = rules["consequents"].apply(lambda x: len(x))
print(rules.sort_values("confidence"))

print(rules[~rules["consequents"].str.contains("POSTAGE", regex=False) &
      ~rules["antecedents"].str.contains("POSTAGE", regex=False)].sort_values("confidence", ascending=False).head(10))