import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
from initialDataAnalysis import Online_Retail_g


# Recency : As the term states, by calculating it we can tell about the customers recent purchase date.
# i.e how many days it has been since their last purchase
# (means iff the value iss less that recently customers purchased)

print("Least recent timestamp in the data:", end=" ")
print(Online_Retail_g['InvoiceDate'].min())

print("Most recent timestamp in the data:", end=" ")
print(Online_Retail_g['InvoiceDate'].max())

# Setting reference time for recency value calculation
X_date = dt.datetime(2011,12,11)

# Calculating Recency
Online_Retail_g_recency = Online_Retail_g
Online_Retail_g_recency = Online_Retail_g_recency.groupby(by = 'CustomerID',as_index=False)['InvoiceDate'].max()
Online_Retail_g_recency.columns = ['CustomerID','latest_date']

Online_Retail_g_recency['Recency'] = Online_Retail_g_recency['latest_date'].apply(lambda date: (X_date - date).days)
Online_Retail_g_recency.drop('latest_date', inplace=True,axis=1 )
print("\nRecency dataframe head: ")
print(Online_Retail_g_recency[['CustomerID','Recency']].head(10))

print("columns in recency dataframe: ")
print(Online_Retail_g_recency.columns)

#sorting values by the recency column
print("\nsorting values by the recency column\n")
Online_Retail_g_recency = Online_Retail_g_recency.sort_values(by = 'Recency')

print("\n After sorting by recency - head(10)")
print(Online_Retail_g_recency.head(10))

print("\n After sorting by recency - tail(10)")
print(Online_Retail_g_recency.tail(10))

# plotting histogram graph for calculated recency values
plt.figure(figsize = (20,12))
sns.histplot(data = Online_Retail_g_recency,x="Recency", binwidth=100)
plt.savefig("../fig/recencyBarChart.png")

