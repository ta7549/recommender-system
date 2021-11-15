import matplotlib.pyplot as plt
import seaborn as sns
from initialDataAnalysis import Online_Retail_g

Online_Retail_g_frequency = Online_Retail_g
Online_Retail_g_frequency = Online_Retail_g_frequency.groupby(by='CustomerID',as_index=False)['InvoiceNo'].nunique()
Online_Retail_g_frequency.columns = ['CustomerID','Frequency']
print("\n Frequency dataframe head(10) ")
print(Online_Retail_g_frequency.head())

print("\n Frequency dataframe tail(10) ")
print(Online_Retail_g_frequency.head())

plt.figure(figsize = (20,12))
sns.histplot(data = Online_Retail_g_frequency,x="Frequency", binwidth=5)
plt.savefig("../fig/frequencyBarChart.png")