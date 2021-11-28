import matplotlib.pyplot as plt
import seaborn as sns
from initialDataAnalysis import Online_Retail_g

print("\nColumns in original dataset")
print(Online_Retail_g.columns)

# Adding transaction amount column to serve the purpose of calculating monetary values
print("\ntransanction amount = unit price * quantity")
Online_Retail_g['TransanctionAmount'] = Online_Retail_g['Quantity'] * Online_Retail_g['UnitPrice']
print(Online_Retail_g.columns)

print("\nOriginal Dataset with Transactional Amount column added: ")
print(Online_Retail_g.head(4))

#Calculating monetary value
Online_Retail_g_monetary = Online_Retail_g
Online_Retail_g_monetary = Online_Retail_g_monetary.groupby(by='CustomerID',as_index=False)['TransanctionAmount'].sum()
Online_Retail_g_monetary.columns = ['CustomerID','Monetary']
print("\nMonetary dataframe head(10)")
print(Online_Retail_g_monetary.head(10))

print("\nMonetary dataframe tail(10)")
print(Online_Retail_g_monetary.tail(10))

# plotting histogram graph for calculated monetary values
plt.figure(figsize = (20,12))
sns.histplot(data = Online_Retail_g_monetary,x="Monetary", binwidth=5000)
plt.savefig("../fig/monetaryBarChart.png")